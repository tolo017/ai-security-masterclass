prompt = input("Enter your prompt: ")

length = 81

is_empty = False

contains_prompt_injection = "YES"

contains_secret_phrase = "NO"

contains_system_phrase = "YES"

risk_score = 40

classification = "MEDIUM"

print(f"Prompt: {prompt}")
print(f"Length: {length}")
print(f"Empty: {is_empty}")
print(f"Prompt injection phrase: {contains_prompt_injection}")
print(f"Secret-related phrase: {contains_secret_phrase}")
print(f"System-prompt phrase: {contains_system_phrase}")
print(f"Score: {risk_score}")
print(f"Classification: {classification}")
