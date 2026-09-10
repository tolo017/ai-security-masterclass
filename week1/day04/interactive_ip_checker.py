# interactive_ip_checker.py
from ip_reputation_checker import classify_ip

def main():
    print("🛡️  Interactive IP Reputation Checker")
    print("Type 'quit' to exit.\n")
    while True:
        ip = input("Enter an IP address: ").strip()
        if ip.lower() == "quit":
            print("Goodbye, Defender!")
            break
        category, reason = classify_ip(ip)
        print(f"→ {category}: {reason}\n")

if __name__ == "__main__":
    main()
