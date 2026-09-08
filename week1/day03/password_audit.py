# password_audit.py
# Audits a list of common passwords and flags weak ones.

common_passwords = [
    "123456", "password", "admin", "letmein", "welcome1",
    "Password123", "Secure@2024", "P@ssw0rd", "qwerty", "iloveyou"
]

def password_strength(pwd):
    """Return a strength score (0-4)."""
    score = 0
    # Length check
    if len(pwd) >= 8:
        score += 1
    # Uppercase check
    if any(c.isupper() for c in pwd):
        score += 1
    # Digit check
    if any(c.isdigit() for c in pwd):
        score += 1
    # Special character check
    if any(not c.isalnum() for c in pwd):
        score += 1
    return score

def main():
    weak_count = 0
    print("🔍 Password Audit Report")
    print("=" * 40)
    for pwd in common_passwords:
        score = password_strength(pwd)
        if score <= 1:
            strength = "VERY WEAK"
            weak_count += 1
        elif score == 2:
            strength = "WEAK"
            weak_count += 1
        elif score == 3:
            strength = "MODERATE"
        else:
            strength = "STRONG"
        print(f"{pwd:15} -> {strength} (score {score}/4)")
    print("=" * 40)
    print(f"Summary: {len(common_passwords)} passwords checked, {weak_count} are weak or very weak.")

if __name__ == "__main__":
    main()
