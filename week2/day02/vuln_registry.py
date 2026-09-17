# vuln_registry.py
# A nested-dictionary vulnerability registry for the AI research lab.

class VulnRegistry:
    """Manages assets and their vulnerabilities using nested dictionaries."""

    def __init__(self):
        # Structure: { asset_name: { "ip": str, "owner": str, "vulnerabilities": { cve: {...} } } }
        self.registry = {}

    # ---------- Asset Operations ----------
    def add_asset(self, name, ip, owner="unassigned"):
        if name in self.registry:
            print(f"⚠️  Asset '{name}' already exists.")
            return
        self.registry[name] = {
            "ip": ip,
            "owner": owner,
            "vulnerabilities": {}
        }
        print(f"✅ Asset added: {name} ({ip})")

    def remove_asset(self, name):
        asset = self.registry.pop(name, None)
        if asset is None:
            print(f"❌ Asset '{name}' not found.")
        else:
            print(f"🗑️  Asset removed: {name}")

    # ---------- Vulnerability Operations ----------
    def add_vuln(self, asset_name, cve_id, severity, cvss, status="Open"):
        asset = self.registry.get(asset_name)
        if asset is None:
            print(f"❌ Asset '{asset_name}' not found. Add it first.")
            return
        asset["vulnerabilities"][cve_id] = {
            "severity": severity,
            "cvss": cvss,
            "status": status
        }
        print(f"✅ Vuln added: {cve_id} ({severity}) → {asset_name}")

    def update_vuln(self, asset_name, cve_id, **fields):
        vuln = (self.registry
                .get(asset_name, {})
                .get("vulnerabilities", {})
                .get(cve_id))
        if vuln is None:
            print(f"❌ Vuln '{cve_id}' not found on '{asset_name}'.")
            return
        vuln.update(fields)
        print(f"🔄 Updated {cve_id}: {fields}")

    def patch_vuln(self, asset_name, cve_id):
        self.update_vuln(asset_name, cve_id, status="Patched")

    # ---------- Queries ----------
    def find_cve(self, cve_id):
        """Find everywhere a CVE appears across all assets."""
        hits = []
        for asset_name, asset in self.registry.items():
            if cve_id in asset.get("vulnerabilities", {}):
                hits.append((asset_name, asset["vulnerabilities"][cve_id]))
        return hits

    def filter_by_severity(self, severity):
        results = []
        for asset_name, asset in self.registry.items():
            for cve, meta in asset.get("vulnerabilities", {}).items():
                if meta.get("severity", "").lower() == severity.lower():
                    results.append((asset_name, cve, meta))
        return results

    def filter_open(self):
        return [(a, c, m) for a, asset in self.registry.items()
                for c, m in asset.get("vulnerabilities", {}).items()
                if m.get("status") == "Open"]

    def asset_summary(self, asset_name):
        asset = self.registry.get(asset_name)
        if asset is None:
            print(f"❌ Asset '{asset_name}' not found.")
            return
        vulns = asset.get("vulnerabilities", {})
        counts = {}
        for meta in vulns.values():
            sev = meta.get("severity", "Unknown")
            counts[sev] = counts.get(sev, 0) + 1
        print(f"\n📊 Summary for {asset_name} ({asset.get('ip', 'N/A')}, owner: {asset.get('owner')})")
        print(f"   Total vulns: {len(vulns)}")
        for sev, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
            print(f"   {sev}: {count}")

    def report(self):
        print("\n" + "=" * 62)
        print("🛡️  VULNERABILITY REGISTRY REPORT")
        print("=" * 62)
        if not self.registry:
            print("No assets registered.")
            return

        total_vulns = 0
        severity_totals = {}

        for asset_name, asset in self.registry.items():
            vulns = asset.get("vulnerabilities", {})
            total_vulns += len(vulns)
            print(f"\n🖥️  {asset_name}  ({asset.get('ip', 'N/A')})  owner: {asset.get('owner')}")
            if not vulns:
                print("   ✅ No vulnerabilities.")
                continue
            for cve, meta in vulns.items():
                total_vulns_sev = meta.get("severity", "Unknown")
                severity_totals[total_vulns_sev] = severity_totals.get(total_vulns_sev, 0) + 1
                icon = {"Critical": "🔴", "High": "🟠", "Medium": "🟡", "Low": "🟢"}.get(total_vulns_sev, "⚪")
                print(f"   {icon} {cve} | CVSS {meta.get('cvss')} | {meta.get('severity')} | {meta.get('status')}")

        print("\n" + "-" * 62)
        print(f"📈 Total vulnerabilities: {total_vulns}")
        for sev, count in sorted(severity_totals.items(), key=lambda x: x[1], reverse=True):
            print(f"   {sev}: {count}")
        print("=" * 62)


def main():
    reg = VulnRegistry()

    # Seed assets
    reg.add_asset("web-server-01", "10.0.0.5", "platform-team")
    reg.add_asset("db-server-02", "10.0.0.6", "data-team")
    reg.add_asset("ai-model-api", "10.0.0.7", "ml-team")
    reg.add_asset("web-server-01", "10.0.0.5")  # duplicate test

    # Seed vulnerabilities
    reg.add_vuln("web-server-01", "CVE-2024-3094", "Critical", 10.0)
    reg.add_vuln("web-server-01", "CVE-2023-44487", "High", 7.5, status="Patched")
    reg.add_vuln("db-server-02", "CVE-2022-22965", "Critical", 9.8)
    reg.add_vuln("ai-model-api", "CVE-2024-1234", "Medium", 5.3)
    reg.add_vuln("ghost-server", "CVE-2024-9999", "Low", 2.1)  # asset missing test

    # Update & patch
    reg.update_vuln("ai-model-api", "CVE-2024-1234", cvss=6.1, status="In Progress")
    reg.patch_vuln("web-server-01", "CVE-2024-3094")

    # Queries
    print("\n🔍 Search for CVE-2024-3094 across all assets:")
    for asset, meta in reg.find_cve("CVE-2024-3094"):
        print(f"   → {asset}: {meta}")

    print("\n🔍 Critical vulns:")
    for asset, cve, meta in reg.filter_by_severity("Critical"):
        print(f"   → {asset}: {cve} (CVSS {meta.get('cvss')})")

    print("\n🔍 All Open vulns:")
    for asset, cve, meta in reg.filter_open():
        print(f"   → {asset}: {cve} ({meta.get('severity')})")

    reg.asset_summary("web-server-01")

    # Full report
    reg.report()


if __name__ == "__main__":
    main()
