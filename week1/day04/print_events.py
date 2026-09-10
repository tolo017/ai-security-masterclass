import csv

with open("events.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row)
              
print(row["user"])
print(row["risk_score"])
print(row["decision"])
