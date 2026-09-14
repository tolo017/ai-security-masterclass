# interactive_asset_manager.py
from asset_list_manager import AssetListManager

def main():
    manager = AssetListManager()
    print("🛡️  AI Lab Asset Manager")
    print("Commands: add, remove, list, sort, top, find, quit\n")
    
    while True:
        command = input("Enter command: ").strip().lower()
        
        if command == "quit":
            print("Goodbye, Defender! 🫡")
            break
        elif command == "add":
            asset = input("Asset name: ").strip()
            manager.add_asset(asset)
        elif command == "remove":
            asset = input("Asset name to remove: ").strip()
            manager.remove_asset(asset)
        elif command == "list":
            manager.list_assets()
        elif command == "sort":
            order = input("Reverse? (y/n): ").strip().lower() == "y"
            manager.sort_assets(reverse=order)
        elif command == "top":
            try:
                n = int(input("How many? "))
                manager.show_top_n(n)
            except ValueError:
                print("Please enter a number.")
        elif command == "find":
            keyword = input("Keyword: ").strip()
            manager.find_asset(keyword)
        else:
            print("Unknown command. Try: add, remove, list, sort, top, find, quit")


if __name__ == "__main__":
    main()
