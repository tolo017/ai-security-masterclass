findings = [
    {
        "finding_id": "F001",
        "user": "alice",
        "category": "benign",
        "risk_score": 5,
        "severity": "LOW",
        "decision": "ALLOW"
    },
    {
        "finding_id": "F002",
        "user": "bob",
        "category": "prompt_injection",
        "risk_score": 70,
        "severity": "HIGH",
        "decision": "BLOCK"
    },
    {
        "finding_id": "F003",
        "user": "charlie",
        "category": "system_prompt_request",
        "risk_score": 25,
        "severity": "MEDIUM",
        "decision": "REVIEW"
    },
    {
        "finding_id": "F004",
        "user": "alice",
        "category": "benign",
        "risk_score": 0,
        "severity": "LOW",
        "decision": "ALLOW"
    }
]

print(len(findings))

blocked = 0
high_severity = 0
highest_risk = 0
highest_risk_user = ""

for finding in findings:
    
    if finding["decision"] == "BLOCK":
        blocked += 1
        
    if finding["severity"] == "HIGH":
        high_severity += 1
        
    if finding["risk_score"] >= highest_risk:
        highest_risk = finding["risk_score"]
        highest_risk_user = finding["user"]
        
print(f"Blocked: {blocked}")
print(f"High severity: {high_severity}")
print(f"Highest risk user: {highest_risk_user}")

allow_count = 0
review_count = 0
block_count = 0

for finding in findings:

    if finding["decision"] == "ALLOW":
        allow_count += 1
        
    if finding["decision"] == "REVIEW":
        review_count += 1
        
    if finding["decision"] == "BLOCK":
        block_count += 1
        
print(f"ALLOW: {allow_count}")
print(f"REVIEW: {review_count}")
print(f"BLOCK: {block_count}")

injection_findings = []

for finding in findings:

    if finding["category"] == "prompt_injection":
        injection_findings.append(finding)
        
print(injection_findings)

alice_findings = []

for finding in findings:

    if finding["user"] == "alice":
        alice_findings.append(finding)
        
print(alice_findings)
