from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))
    date = db.Column(db.DateTime, default=db.func.current_date())

    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description
