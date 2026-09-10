import json
import csv
from datetime import datetime

timestamp = datetime.now().isoformat()

prompts = []

with open("input_prompts.txt", "r") as file:

    for line in file:
        prompt = line.strip()

        if prompt == "":
            continue

        prompts.append(prompt)
        
print(f"Loaded {len(prompts)} prompts.")

results = []

for prompt in prompts:

    normalized_prompt = prompt.strip().lower()

    prompt_length = len(prompt)

    contains_injection_indicator = (
        "ignore previous instructions"
        in normalized_prompt
    )

    mentions_system_prompt = (
        "system prompt"
        in normalized_prompt
    )

    risk_score = 0

    if contains_injection_indicator:
        risk_score += 50

    if mentions_system_prompt:
        risk_score += 20

    if prompt_length > 500:
        risk_score += 10

    if risk_score >= 50:
        decision = "BLOCK"
    elif risk_score >= 20:
        decision = "REVIEW"
    else:
        decision = "ALLOW"
            
result = {
    "prompt": prompt,
    "length": prompt_length,
    "injection_indicator": contains_injection_indicator,
    "system_prompt_indicator": mentions_system_prompt,
    "risk_score": risk_score,
    "decision": decision
}

results.append(result)
    
with open("scan_results.json", "w") as file:
    json.dump(results, file, indent=4)
    
allow_count = 0
review_count = 0
block_count = 0
highest_risk = 0

for result in results:

    if result["decision"] == "ALLOW":
        allow_count += 1

    elif result["decision"] == "REVIEW":
        review_count += 1

    elif result["decision"] == "BLOCK":
        block_count += 1

    if result["risk_score"] > highest_risk:
        highest_risk = result["risk_score"]
        
report = f"""
AI SECURITY SCAN REPORT
=======================

Scan time: {timestamp}
Input: input_prompts.txt
Scanner version: 0.1

Total prompts: {len(results)}

ALLOW: {allow_count}
REVIEW: {review_count}
BLOCK: {block_count}

Highest risk score: {highest_risk}
"""

with open("security_report.txt", "w") as file:
    file.write(report)
    
with open("security_findings.txt", "w") as file:

    for result in results:

        if result["decision"] in ["REVIEW", "BLOCK"]:

            file.write(
                f"Prompt: {result['prompt']}\n"
            )

            file.write(
                f"Risk: {result['risk_score']}\n"
            )

            file.write(
                f"Decision: {result['decision']}\n"
            )

            file.write("-" * 50 + "\n")
            
with open("security_findings.csv", "w", newline="") as csv_file:
    
    fieldnames = [
        "prompt",
        "length",
        "injection_indicator",
        "system_prompt_indicator",
        "risk_score",
        "decision"
    ]
    
    writer = csv.DictWriter(csv_file, fieldnames= fieldnames)
    
    writer.writeheader()
    
    writer.writerows(results)
    
print("Successfully saved results in CSV format")
