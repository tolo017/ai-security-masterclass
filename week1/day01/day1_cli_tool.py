"""
Day 1 - CVSS Severity Calculator
This script asks the user for a CVSS base score and returns the severity rating.
"""

def main():
    # Ask user for input
    user_input = input("Enter a CVSS base score (0.0 - 10.0): ")

    # Validate and convert to float
    try:
        score = float(user_input)
    except ValueError:
        print("Error: Invalid number. Please enter a numeric value.")
        return

    # Check if score is within valid CVSS range
    if score < 0.0 or score > 10.0:
        print("Error: Score must be between 0.0 and 10.0.")
        return

    # Determine severity
    if score == 0.0:
        severity = "None"
    elif score < 4.0:
        severity = "Low"
    elif score < 7.0:
        severity = "Medium"
    elif score < 9.0:
        severity = "High"
    else:
        severity = "Critical"

    # Output result
    print(f"CVSS Score: {score:.1f} -> Severity: {severity}")

if __name__ == "__main__":
    main()
