decisions = [
    "ALLOW",
    "BLOCK",
    "BLOCK",
    "REVIEW",
    "ALLOW",
    "BLOCK",
    "REVIEW",
    "ALLOW"
]

categories = [
    "prompt_injection",
    "prompt_injection",
    "data_exposure",
    "prompt_injection",
    "output_handling",
    "data_exposure"
]

users = [
    "alice",
    "bob",
    "alice",
    "charlie",
    "bob",
    "bob"
]

severities = [
    "LOW",
    "HIGH",
    "MEDIUM",
    "HIGH",
    "CRITICAL",
    "LOW"
]

counts = {}

category_counts = {}

user_counts = {}

severity_counts = {}

for decision in decisions:
    
    counts[decision] = counts.get(decision, 0) + 1
          
for decision, count in counts.items():

    print(f"{decision}: {count}")
    
for category in categories:
    
    category_counts[category] = category_counts.get(category, 0) + 1
    
for category, category_count in category_counts.items():

    print(f"{category}: {category_count}")
    
for user in users:
    
    user_counts[user] = user_counts.get(user, 0) + 1
    
for user, user_count in user_counts.items():
    
    print(f"{user}: {user_count}")
    
for severity in severities:
    
    severity_counts[severity] = severity_counts.get(severity, 0) + 1
    
for severity, severity_count in severity_counts.items():
    
    print(f"{severity}: {severity_count}")
    
    
risk_weights = {
    "prompt_injection": 50,
    "data_exposure": 40,
    "output_handling": 30,
    "benign": 0
}

category = "prompt_injection"

score = risk_weights.get(category, 0)

print(score)
