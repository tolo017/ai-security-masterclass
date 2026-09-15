findings = [
    {
        "finding_id": "F001",
        "risk_score": 10,
        "decision": "ALLOW"
    },
    {
        "finding_id": "F002",
        "risk_score": 70,
        "decision": "BLOCK"
    },
    {
        "finding_id": "F003",
        "risk_score": 25,
        "decision": "REVIEW"
    }
]

high_risk_count = 0

for finding in findings:

    if finding["risk_score"] >= 50:
        high_risk_count += 1
        
print(f"High-risk findings: {high_risk_count}")
