is_authenticated = input("Is the user authenticated? (yes/no): ").strip().lower()
is_authenticated = is_authenticated == "yes"

prompt = input("Enter a prompt: ")
normalized_prompt = prompt.strip().lower()
prompt_length = len(prompt)

contains_injection_indicator = ("ignore previous instructions" in normalized_prompt)
mentions_system_prompt = ("system prompt" in normalized_prompt)

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
    
if not is_authenticated:
    decision = "BLOCK"
elif risk_score >= 50:
    decision = "BLOCK"
elif risk_score >= 20:
    decision = "REVIEW"
else:
    decision = "ALLOW"
    
print("\n=== AI SECURITY POLICY DECISION ===")
print(f"Prompt length: {prompt_length}")
print(f"Injection indicator: {contains_injection_indicator}")
print(f"System prompt indicator: {mentions_system_prompt}")
print(f"Risk score: {risk_score}")
print(f"Decision: {decision}")
