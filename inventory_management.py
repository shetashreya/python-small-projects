class InventoryItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class InventoryManager:
    def __init__(self):
        self.inventory = []

    def add_item(self, name, quantity, price):
        item = InventoryItem(name, quantity, price)
        self.inventory.append(item)

    def view_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for item in self.inventory:
                print(f"Name: {item.name}, Quantity: {item.quantity}, Price: ${item.price:.2f}")

    def search_item(self, name):
        for item in self.inventory:
            if item.name.lower() == name.lower():
                print(f"Item found - Name: {item.name}, Quantity: {item.quantity}, Price: ${item.price:.2f}")
                return
        print("Item not found in inventory.")

def main():
    inventory_manager = InventoryManager()

    while True:
        print("\nMenu:")
        print("1. Add Item to Inventory")
        print("2. View Inventory")
        print("3. Search for Item")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per item: $"))
            inventory_manager.add_item(name, quantity, price)
            print("Item added to inventory.")

        elif choice == "2":
            inventory_manager.view_inventory()

        elif choice == "3":
            name = input("Enter item name to search: ")
            inventory_manager.search_item(name)

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
