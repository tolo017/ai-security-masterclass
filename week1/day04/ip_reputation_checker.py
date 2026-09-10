# ip_reputation_checker.py
# Classifies IP addresses based on allowlists, denylists, and suspicious subnets.

# --- Configuration ---
DENYLIST = [
    "10.0.0.5",
    "192.168.1.100",
    "203.0.113.42",
    "198.51.100.7"
]

ALLOWLIST = [
    "10.0.0.1",
    "10.0.0.2",
    "10.0.0.10",
    "192.168.0.1"
]

# Suspicious subnets (prefix match)
SUSPICIOUS_PREFIXES = [
    "203.0.113.",
    "198.51.100.",
    "192.0.2."
]

# --- Helper Functions ---
def is_valid_ip(ip):
    """Return True if ip is a valid IPv4 address."""
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if not (0 <= int(part) <= 255):
            return False
    return True

def classify_ip(ip):
    """Return (category, reason) for a given IP."""
    # 1. Validate format
    if not is_valid_ip(ip):
        return ("INVALID", "Not a valid IPv4 address.")
    
    # 2. Denylist check
    if ip in DENYLIST:
        return ("MALICIOUS", "Found in denylist.")
    
    # 3. Allowlist check
    if ip in ALLOWLIST:
        return ("TRUSTED", "Found in allowlist.")
    
    # 4. Suspicious subnet check
    for prefix in SUSPICIOUS_PREFIXES:
        if ip.startswith(prefix):
            return ("SUSPICIOUS", f"Matches suspicious subnet {prefix}0/24.")
    
    # 5. Default
    return ("UNKNOWN", "No match found.")

# --- Main Execution ---
def main():
    # Sample list of IPs to test
    ip_list = [
        "10.0.0.1",       # trusted
        "10.0.0.5",       # malicious
        "203.0.113.42",   # malicious (also suspicious subnet)
        "203.0.113.99",   # suspicious subnet
        "8.8.8.8",        # unknown
        "999.999.999.999",# invalid
        "192.168.1.100",  # malicious
        "192.168.0.1",    # trusted
        "198.51.100.7",   # malicious
        "198.51.100.55",  # suspicious
        "1.2.3",          # invalid
        "10.0.0.10"       # trusted
    ]
    
    print("🛡️  IP Reputation Checker")
    print("=" * 60)
    print(f"{'IP Address':<18} {'Category':<12} Reason")
    print("-" * 60)
    
    for ip in ip_list:
        category, reason = classify_ip(ip)
        # Optionally add emoji for fun
        if category == "MALICIOUS":
            icon = "🔴"
        elif category == "SUSPICIOUS":
            icon = "🟠"
        elif category == "TRUSTED":
            icon = "🟢"
        elif category == "INVALID":
            icon = "⚫"
        else:
            icon = "⚪"
        print(f"{ip:<18} {icon} {category:<10} {reason}")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
