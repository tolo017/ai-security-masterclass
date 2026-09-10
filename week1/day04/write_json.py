import json

with open("event.json", "r") as file:
    event = json.load(file)

print(event)
print(event["user"])
print(event["risk_score"])
print(event["decision"])
