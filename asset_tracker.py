'''
1. Classes & objects
2. Encapsulation
3. Inheritance
4. Polymorphism
5. Polish
'''

import json 

# Use ClassName.x for things truly shared across all instances (like total_assets). Use self.x for things that belong to one specific object.

class Asset:
    total_assets = 0
    def __init__(self, asset_id, name, category, status="available"):
        self.asset_id = asset_id
        self.name = name
        self.category = category
        self.status = status # self._status = status would still prevent from allocating invalid statuses to existing objects, but would allow creation of objects with incorrect status
        Asset.total_assets += 1
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        # or means "if ANY of these is true" — and a value can't equal all three at once, so one branch is always true.
        acceptable_values = ["available", "assigned", "maintenance"]
        if value not in acceptable_values:
            print(f"Unauthorized status '{value}'. Defaulting to 'available'.")
            self._status = "available"
        else:
            self._status = value

    def __str__(self):
        return f"{self.asset_id} | {self.name} | {self.category} | {self.status}"
    
    def get_summary(self):
        return f"{self.name} is a {self.category} currently {self.status} under asset ID {self.asset_id}"
    
    def to_dict(self):
        return {"asset_id": self.asset_id, "name": self.name, "category": self.category, "status": self.status}

    
# parameters with defaults come after parameters without defaults:

class Laptop(Asset):
    def __init__(self, asset_id, name, category, status="available", assigned_user="unassigned"):
        super().__init__(asset_id, name, category, status)
        self.assigned_user = assigned_user

    def get_summary(self):
        # return super().get_summary()
        return f"{self.name} ({self.category}) assigned to {self.assigned_user} - status: {self.status}"
    
class NetworkDevice(Asset):
    def __init__(self, asset_id, name, category, status="available", ip_address="0.0.0.0"):
        super().__init__(asset_id, name, category, status)
        self.ip_address = ip_address

    def get_summary(self):
        return f"{self.name} ({self.category}) with the following IP address: {self.ip_address} - status: {self.status}"


class AssetManager:
    def __init__(self):
        self.assets = []
    def add_asset(self, asset):
        self.assets.append(asset)
    def list_assets(self):
        for item in self.assets:
            print(item)
    def find_asset(self, asset_id):
        for item in self.assets:
            if item.asset_id == asset_id:
                return item
        return "Asset not found."
# return outside of for loop to check everything and not give up after first item

    def save_to_file(self, filename): # flattens objects into dictionaries
        data = [asset.to_dict() for asset in self.assets]
        with open(filename, "w") as f:
            json.dump(data, f)

    def load_from_file(self, filename): # rebuilds objects from dictionaries
        with open(filename, "r") as f:
            data = json.load(f)
        for item in data:
            asset = Asset(item["asset_id"], item["name"], item["category"], item["status"])
            self.assets.append(asset)

'''
# create manager, add assets, save
manager = AssetManager()
manager.add_asset(Asset("A001", "Edmond's Mac", "laptop"))
manager.add_asset(Asset("A002", "Maia's iPad", "tablet"))
manager.save_to_file("data.json")

# reload from file and list
manager2 = AssetManager()
manager2.load_from_file("data.json")
manager2.list_assets()
'''

def main():
    manager = AssetManager()
    manager.load_from_file("data.json")

    while True:
        print("\n=== IT Tracker ===\n")
        print("1. Add asset")
        print("2. List all assets")
        print("3. Find asset by ID")
        print("4. Update asset status")
        print("5. Save & Quit")

        choice = input("Enter choice: ")

        if choice == "1":
            asset_id = input("Enter the Asset ID: ")
            name = input("Enter the asset name: ") 
            category = input("Enter the asset category: ")
            status = input("Enter the asset status: ")
            new_asset = Asset(asset_id, name, category, status)
            manager.add_asset(new_asset)
        elif choice == "2":
            manager.list_assets()
        elif choice == "3":
            asset_searched = input("Enter the asset ID you're looking for: ")
            print(manager.find_asset(asset_searched))
        elif choice == "4":
            asset_updated = input("Enter the asset ID you're looking for: ")
            asset = manager.find_asset(asset_updated)
            new_status = input("Enter the new asset status: ")
            asset.status = new_status
        elif choice == "5":
            manager.save_to_file("data.json")
            break
        else:
            continue

if __name__ == "__main__":
    main()
