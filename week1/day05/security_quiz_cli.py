import random

questions = [
    {
        "question": "What does 'phishing' refer to?",
        "options": [
            "A. Sending malware via USB drives",
            "B. Tricking users into revealing sensitive information",
            "C. Exploiting unpatched software",
            "D. Overloading a server with traffic"
        ],
        "answer": 1,
        "explanation": "Phishing tricks users into revealing credentials or sensitive data, often via fake emails or websites."
    },
    {
        "question": "What is the principle of least privilege?",
        "options": [
            "A. Giving every user admin rights",
            "B. Granting only the minimum access needed to perform a task",
            "C. Sharing passwords across teams",
            "D. Disabling all firewalls"
        ],
        "answer": 1,
        "explanation": "Least privilege means users get only the access required for their role — nothing more."
    },
    {
        "question": "What does 'prompt injection' mean in the context of LLMs?",
        "options": [
            "A. Injecting SQL into a database",
            "B. Overriding an LLM's instructions via malicious user input",
            "C. Sending a virus through email",
            "D. Physically injecting code into a server"
        ],
        "answer": 1,
        "explanation": "Prompt injection manipulates an LLM by embedding malicious instructions in user input, overriding system prompts."
    },
    {
        "question": "What is multi-factor authentication (MFA)?",
        "options": [
            "A. Using two passwords",
            "B. Combining two or more verification methods (e.g., password + OTP)",
            "C. Logging in from two devices",
            "D. Using a VPN"
        ],
        "answer": 1,
        "explanation": "MFA requires multiple independent credentials — something you know, have, or are."
    },
    {
        "question": "What is the OWASP Top 10 for LLMs?",
        "options": [
            "A. A list of the 10 best LLM models",
            "B. A ranking of the 10 most critical LLM security risks",
            "C. A Python library for LLM development",
            "D. A certification for AI engineers"
        ],
        "answer": 1,
        "explanation": "OWASP Top 10 for LLMs is a community-driven list of the most critical security risks in LLM applications."
    }
]

random.shuffle(questions)

def ask_question(q, index):
    """Display a question, get validated input, return True if correct."""
    print(f"\nQuestion {index + 1}: {q['question']}")
    for opt in q["options"]:
        print(f"  {opt}")
        
    while True:
       choice = input("Your answer (A/B/C/D): ").strip().upper()
       if choice in ["A", "B", "C", "D"]:
           break
       print("Invalid input. Please enter A, B, C, or D.")
       
     # Convert letter to index
    choice_index = ord(choice) - ord("A")
    correct = (choice_index == q["answer"])
    
    if correct:
        print("✅ Correct!")
    else:
        correct_letter = chr(ord("A") + q["answer"])
        print(f"❌ Incorrect. The correct answer was {correct_letter}.")
    print(f"💡 {q['explanation']}")
    
    return correct
    
def main():
    name = input("Enter your name: ").strip() or "Agent"
    print(f"Welcome, {name}!")
    
    print("🔐 Security Awareness Quiz")
    print("=" * 50)
    print("Answer 5 questions to test your security knowledge.\n")
    
    score = 0
    total = len(questions)
    
    for i, q in enumerate(questions):
        if ask_question(q, i):
            score += 1
    
    # Final results
    print("\n" + "=" * 50)
    print(f"🏁 Final Score: {score}/{total}")
    
    if score == total:
        print("🏆 Security Champion! Perfect score.")
    elif score >= 4:
        print("✅ Solid performance. Review the ones you missed.")
    elif score >= 3:
        print("⚠️ Needs improvement. Revisit the fundamentals.")
    else:
        print("🚨 Please retake — security fundamentals matter, especially for AI systems.")
    
    print("=" * 50)
    print(f"Congratulations {name}, continue sharpening your skills.")
    print("Thank you for playing! Stay secure. 🛡️")

if __name__ == "__main__":
    main()

