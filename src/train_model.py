import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Load logs
logs = []
labels = []

with open("../data/logs.txt", "r") as file:
    for line in file:
        log = line.strip()
        logs.append(log)

        if "ERROR" in log:
            labels.append("ERROR")
        elif "WARNING" in log:
            labels.append("WARNING")
        else:
            labels.append("INFO")

# Convert text to numbers using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(logs)

# Train ML model
model = LogisticRegression(max_iter=1000)
model.fit(X, labels)

# Save model and vectorizer
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model trained and saved successfully")
