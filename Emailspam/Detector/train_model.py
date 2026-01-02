import pandas as pd
import pickle
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(BASE_DIR, "Detector", "spam_dataset.csv")

data = pd.read_csv(csv_path)


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['message_content'])
y = data['is_spam']

model = MultinomialNB()
model.fit(X, y)

# Save inside project root (same level as manage.py)
with open(os.path.join(BASE_DIR, "model.pkl"), "wb") as f:
    pickle.dump(model, f)

with open(os.path.join(BASE_DIR, "vectorizer.pkl"), "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model and vectorizer saved successfully")
