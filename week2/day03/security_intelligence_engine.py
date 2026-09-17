events = [
    {
        "event_id": "E001",
        "user": "alice",
        "category": "benign",
        "severity": "LOW",
        "risk_score": 5,
        "decision": "ALLOW"
    },
    {
        "event_id": "E002",
        "user": "bob",
        "category": "prompt_injection",
        "severity": "HIGH",
        "risk_score": 70,
        "decision": "BLOCK"
    },
    {
        "event_id": "E003",
        "user": "alice",
        "category": "data_exposure",
        "severity": "MEDIUM",
        "risk_score": 40,
        "decision": "REVIEW"
    },
    {
        "event_id": "E004",
        "user": "charlie",
        "category": "prompt_injection",
        "severity": "HIGH",
        "risk_score": 75,
        "decision": "BLOCK"
    }
]

decision_counts = {}

for event in events:

    decision = event["decision"]

    decision_counts[decision] = (
        decision_counts.get(decision, 0) + 1
    )
    
print("Decision counts:")

for decision, count in decision_counts.items():
    
    print(f"{decision}: {count}")
    
user_counts = {}

for event in events:

    user = event["user"]

    user_counts[user] = (
        user_counts.get(user, 0) + 1
    )
    
user_risk = {}

for event in events:

    user = event["user"]
    risk = event["risk_score"]

    user_risk[user] = (
        user_risk.get(user, 0) + risk
    )
    
highest_user_risk = 0
highest_risk_user = None

for user, risk in user_risk.items():

    if risk > highest_user_risk:
        highest_user_risk = risk
        highest_risk_user = user
        
print(
    f"Highest aggregate risk: "
    f"{highest_risk_user} "
    f"({highest_user_risk})"
)

severity_counts = {}

for event in events:

    severity = event["severity"]

    severity_counts[severity] = (
        severity_counts.get(severity, 0) + 1
    )
    
events_by_user = {}

for event in events:

    user = event["user"]

    events_by_user.setdefault(user, [])
    events_by_user[user].append(event)
    
for user, user_events in events_by_user.items():

    print(f"\nUser: {user}")

    for event in user_events:
        print(
            f"  {event['event_id']} - "
            f"{event['decision']}"
        )
        
events_by_category = {}

for event in events:

    category = event["category"]

    events_by_category.setdefault(category, [])
    events_by_category[category].append(event)
    
category_risk = {}

for event in events:

    category = event["category"]
    risk = event["risk_score"]

    category_risk[category] = (
        category_risk.get(category, 0) + risk
    )
    
severity_weight = {
    "LOW": 1,
    "MEDIUM": 2,
    "HIGH": 3,
    "CRITICAL": 4
}

weight = severity_weight.get(
    event["severity"],
    0
)

weighted_risk = event["risk_score"] * weight
