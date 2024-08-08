from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

import joblib

# Load labeled data
df = pd.read_csv('expense_labels2.csv')
X = df['description']
y = df['category']

# Vectorize text data
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vec, y)

# Save model and vectorizer

joblib.dump(model, 'expense_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')
