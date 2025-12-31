import pickle

# Load trained model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict_log(log_message):
    vector = vectorizer.transform([log_message])
    prediction = model.predict(vector)
    return prediction[0]

print("Log Prediction System (type 'exit' to quit)")

while True:
    log_input = input("Enter log message: ")
    if log_input.lower() == "exit":
        break
    result = predict_log(log_input)
    print("Predicted Severity:", result)
