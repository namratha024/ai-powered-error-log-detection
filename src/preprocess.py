import pandas as pd

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

df = pd.DataFrame({
    "log_message": logs,
    "severity": labels
})

print(df)
