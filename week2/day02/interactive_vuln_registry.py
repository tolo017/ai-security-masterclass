# interactive_vuln_registry.py
from vuln_registry import VulnRegistry

def main():
    reg = VulnRegistry()
    print("🛡️  Interactive Vulnerability Registry")
    print("Commands: add-asset, add-vuln, update, patch, find, filter, report, quit\n")

    while True:
        cmd = input("> ").strip().lower()

        if cmd == "quit":
            print("Stay secure, Defender! 🫡")
            break
        elif cmd == "add-asset":
            name = input("Asset name: ").strip()
            ip = input("IP: ").strip()
            owner = input("Owner (optional): ").strip() or "unassigned"
            reg.add_asset(name, ip, owner)
        elif cmd == "add-vuln":
            asset = input("Asset name: ").strip()
            cve = input("CVE ID: ").strip()
            sev = input("Severity (Critical/High/Medium/Low): ").strip()
            try:
                cvss = float(input("CVSS score: ").strip())
            except ValueError:
                print("Invalid CVSS. Using 0.0")
                cvss = 0.0
            reg.add_vuln(asset, cve, sev, cvss)
        elif cmd == "update":
            asset = input("Asset: ").strip()
            cve = input("CVE: ").strip()
            field = input("Field to update (severity/cvss/status): ").strip()
            value = input("New value: ").strip()
            if field == "cvss":
                try:
                    value = float(value)
                except ValueError:
                    print("Invalid CVSS.")
                    continue
            reg.update_vuln(asset, cve, **{field: value})
        elif cmd == "patch":
            reg.patch_vuln(input("Asset: ").strip(), input("CVE: ").strip())
        elif cmd == "find":
            for asset, meta in reg.find_cve(input("CVE ID: ").strip()):
                print(f"   → {asset}: {meta}")
        elif cmd == "filter":
            for asset, cve, meta in reg.filter_by_severity(input("Severity: ").strip()):
                print(f"   → {asset}: {cve} ({meta})")
        elif cmd == "report":
            reg.report()
        else:
            print("Unknown command. Try: add-asset, add-vuln, update, patch, find, filter, report, quit")


if __name__ == "__main__":
    main()
