prompt = input("Enter a prompt to analyze: ")

normalized_prompt = prompt.strip().lower()

upper_prompt = prompt.strip().upper()

prompt_length = len(prompt)

contains_injection_indicator = (
    "ignore previous instructions" in normalized_prompt
)

is_empty = len(normalized_prompt) == 0

is_deleted = len(upper_prompt) == 1

print("\n=== AI SECURITY INPUT ANALYZER ===")
print(f"Original prompt: {prompt}")
print(f"Normalized prompt: {normalized_prompt}")
print(f"Upper Case prompt: {upper_prompt}")
print(f"Prompt length: {prompt_length}")
print(f"Empty prompt: {is_empty}")
print(f"Deleted: {is_deleted}")
print(
    f"Known injection indicator: "
    f"{contains_injection_indicator}"
)

risk_score = 0

if contains_injection_indicator:
    risk_score += 50

if is_empty:
    risk_score += 5

if prompt_length > 500:
    risk_score += 10

print(f"Risk score: {risk_score}")

if risk_score >= 50:
    classification = "HIGH"
elif risk_score >= 20:
    classification = "MEDIUM"
else:
    classification = "LOW"
    
print(f"Classification: {classification}")
