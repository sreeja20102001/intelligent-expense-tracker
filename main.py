from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Expense
import joblib
import matplotlib.pyplot as plt
import time


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

model=joblib.load('expense_model.pkl')
vectorizer=joblib.load('vectorizer.pkl')


@app.route('/', methods=["GET","POST"])
def index():
    if request.method=="POST":
        amount=request.form["amount"]
        category=request.form["category"]
        desc=request.form["description"]
        if not category:
            description_vec=vectorizer.transform([desc])
            category=model.predict(description_vec)[0]
        form=Expense(amount=amount, category=category, description=desc)
        db.session.add(form)
        db.session.commit()
        flash("Your response has been submitted")
        return redirect(url_for('index'))
    try:
        expenses = Expense.query.all()
    except Exception as e:
        print(f"Error fetching expenses: {str(e)}")
        expenses = []  # Handle the error condition

    return render_template('index.html', expenses=expenses)


@app.route('/visualize', methods=['GET'])
def visualize():
    # Query expenses grouped by category and sum of amounts
    query_result = db.session.query(Expense.category, db.func.sum(Expense.amount).label('total_amount')) \
        .group_by(Expense.category) \
        .all()

    categories = [result[0] for result in query_result]
    total_amounts = [result[1] for result in query_result]

    # Create a bar chart using Matplotlib
    plt.figure(figsize=(10, 6))
    plt.bar(categories, total_amounts, color='skyblue')
    plt.xlabel('Categories')
    plt.ylabel('Total Amount Spent ($)')
    plt.title('Total Amount Spent per Category')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot to a static file in the 'static' folder with cache-busting timestamp
    timestamp = int(time.time())
    plot_file = f'total_amount_per_category_{timestamp}.png'  # Append timestamp to filename
    plt.savefig(f'static/{plot_file}')
    plt.close()

    # Return HTML with the image embedded or link to the image
    return f'<h1>Total Amount Spent per Category</h1><img src="/static/{plot_file}" alt="Total Amount per Category">'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)

