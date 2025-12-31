import pandas as pd
import matplotlib.pyplot as plt

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

df = pd.DataFrame({"severity": labels})

# Plot severity distribution
df["severity"].value_counts().plot(kind="bar")
plt.title("Log Severity Distribution")
plt.xlabel("Severity Level")
plt.ylabel("Count")
plt.show()
