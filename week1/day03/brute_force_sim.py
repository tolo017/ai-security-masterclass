# brute_force_sim.py
# Simulates a brute-force attack with account lockout after 5 failures.

correct_password = "S3cure!Pass"
# Attacker's guess list (dictionary order)
guesses = [
    "123456", "password", "admin", "letmein", "S3cure!Pass",  # correct is 5th
    "qwerty", "iloveyou"
]

max_attempts = 5
attempts = 0
access_granted = False

print("🚨 Brute-Force Attack Simulation")
print("=" * 40)
while attempts < max_attempts and attempts < len(guesses):
    guess = guesses[attempts]
    print(f"Attempt {attempts+1}: trying '{guess}'")
    if guess == correct_password:
        print("✅ Access granted!")
        access_granted = True
        break
    else:
        print("❌ Incorrect.")
        attempts += 1
else:
    # The else block of a while loop runs if the loop ended without a break
    print("⛔ Account locked due to too many failed attempts.")

if not access_granted:
    print("Attack unsuccessful.")
