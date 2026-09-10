import json

with open("security_event.json", "r") as file:
    events = json.load(file)

for event in events:
    print(event["user"])
    print(event["risk_score"])
    print(event["decision"])
    print("---")
