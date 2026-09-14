# asset_list_manager.py
# Manages a list of assets for the AI research lab.

class AssetListManager:
    def __init__(self):
        self.assets = []
    
    def add_asset(self, asset):
        """Add an asset to the inventory."""
        if asset in self.assets:
            print(f"⚠️  '{asset}' already exists. Skipping duplicate.")
            return
        self.assets.append(asset)
        print(f"✅ Added: {asset}")
    
    def remove_asset(self, asset):
        """Remove an asset by name."""
        if asset in self.assets:
            self.assets.remove(asset)
            print(f"🗑️  Removed: {asset}")
        else:
            print(f"❌ '{asset}' not found in inventory.")
    
    def list_assets(self):
        """Display all assets."""
        if not self.assets:
            print("📭 Inventory is empty.")
            return
        print("\n📋 Current Asset Inventory:")
        for i, asset in enumerate(self.assets, start=1):
            print(f"  {i}. {asset}")
    
    def show_top_n(self, n):
        """Show the first N assets (simulating a 'top N' view)."""
        top = self.assets[:n]
        print(f"\n🔝 Top {n} assets: {top}")
    
    def sort_assets(self, reverse=False):
        """Sort assets alphabetically."""
        self.assets.sort(reverse=reverse)
        order = "Z→A" if reverse else "A→Z"
        print(f"🔤 Sorted ({order}): {self.assets}")
    
    def find_asset(self, keyword):
        """Find assets containing a keyword."""
        matches = [a for a in self.assets if keyword.lower() in a.lower()]
        if matches:
            print(f"🔍 Matches for '{keyword}': {matches}")
        else:
            print(f"🔍 No assets match '{keyword}'.")
    
    def get_copy(self):
        """Return a safe copy of the asset list."""
        return self.assets.copy()


def main():
    manager = AssetListManager()
    
    # Seed with initial assets
    initial_assets = [
        "web-server-01",
        "db-server-02",
        "ai-model-api",
        "firewall-edge",
        "vpn-gateway",
        "mail-server-01"
    ]
    for asset in initial_assets:
        manager.add_asset(asset)
    
    # Demonstrate operations
    print("\n--- Initial Inventory ---")
    manager.list_assets()
    
    print("\n--- Adding New Assets ---")
    manager.add_asset("logging-server-01")
    manager.add_asset("backup-server-01")
    manager.add_asset("web-server-01")  # Duplicate test
    
    print("\n--- Removing an Asset ---")
    manager.remove_asset("mail-server-01")
    manager.remove_asset("nonexistent-server")
    
    print("\n--- Showing Top 3 ---")
    manager.show_top_n(3)
    
    print("\n--- Sorting A→Z ---")
    manager.sort_assets()
    
    print("\n--- Sorting Z→A ---")
    manager.sort_assets(reverse=True)
    
    print("\n--- Searching for 'server' ---")
    manager.find_asset("server")
    
    print("\n--- Demonstrating Safe Copy ---")
    copy = manager.get_copy()
    copy.append("malicious-injected-asset")
    print(f"Copy after modification: {copy}")
    print(f"Original unchanged: {manager.assets}")
    
    print("\n--- Final Inventory ---")
    manager.list_assets()


if __name__ == "__main__":
    main()
