# intelligent-expense-tracker
Overview
The Intelligent Expense Tracker is a Flask web application designed to help users track, categorize, and analyze their expenses efficiently. By leveraging machine learning models, the application automatically categorizes expenses and provides insightful data visualizations to help users manage their finances better. The app also includes features like real-time notifications and budget suggestions, making financial management both smart and simple.

Features
Expense Categorization: Automatically categorizes expenses with 85% accuracy using machine learning models (scikit-learn, TensorFlow).
Real-Time Notifications: Provides real-time notifications to keep users updated on their spending.
Data Visualization: Visualizes spending patterns with Matplotlib, including total amounts per category and monthly trends.
Database Management: Uses SQLite for efficient data storage and management.
Scalability: Deployed on Heroku, ensuring the app can scale to handle increased user traffic.
User Engagement: Enhances user interaction with actionable financial insights and spending alerts.

Project Structure
intelligent-expense-tracker/
│
├── main.py                  # Main Flask application
├── models.py                # Database models for SQLite
├── mlmodel.py               # Machine learning model training script
├── index.html               # Frontend form for user input
├── expense_labels2.csv      # Dataset containing labeled expense data
├── expense_model.pkl        # Pre-trained expense categorization model
├── vectorizer.pkl           # Fitted CountVectorizer for text vectorization
├── total_amount_per_category.png  # Example data visualization
└── README.md                # Project documentation
