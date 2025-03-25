class Item:
    item_id_counter = 1 
    
    def __init__(self, name, description, price):
        self.id = Item.item_id_counter
        self.name = name
        self.description = description
        self.price = price
        Item.item_id_counter += 1

class ItemManager:
    def __init__(self):
        self.items = []
    
    def create_item(self):
        try:
            name = input("Enter item name: ").strip()
            if not name:
                raise ValueError("Name cannot be empty.")
            
            description = input("Enter item description: ").strip()
            if not description:
                raise ValueError("Description cannot be empty.")
            
            price = float(input("Enter item price: "))
            if price <= 0:
                raise ValueError("Price must be a positive number.")
            
            new_item = Item(name, description, price)
            self.items.append(new_item)
            print("Item added successfully!")
        except ValueError as e:
            print("Error:", e)
    
    def read_items(self):
        if not self.items:
            print("No items available.")
            return
        for item in self.items:
            print(f"\n\nID: {item.id} \nName: {item.name} \nDescription: {item.description} \nPrice: {item.price}")
    
    def update_item(self):
        try:
            item_id = int(input("Enter item ID to update: "))
            for item in self.items:
                if item.id == item_id:
                    name = input("Enter new name (enter to keep current): ").strip()
                    if name:
                        item.name = name
                    
                    description = input("Enter new description (enter to keep current): ").strip()
                    if description:
                        item.description = description
                    
                    price_input = input("Enter new price (enter to keep current): ").strip()
                    if price_input:
                        price = float(price_input)
                        if price <= 0:
                            raise ValueError("Price must be a positive number.")
                        item.price = price
                    
                    print("Item updated successfully!")
                    return
            print("Item not found.")
        except ValueError as e:
            print("Error:", e)
    
    def delete_item(self):
        try:
            item_id = int(input("Enter item ID to delete: "))
            for item in self.items:
                if item.id == item_id:
                    self.items.remove(item)
                    print("Item deleted successfully!")
                    return
            print("Item not found.")
        except ValueError:
            print("Invalid input. Please enter a valid ID.")

def main():
    manager = ItemManager()
    while True:
        print("\nItem Management System")
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        if choice == "1":
            manager.create_item()
        elif choice == "2":
            manager.read_items()
        elif choice == "3":
            manager.update_item()
        elif choice == "4":
            manager.delete_item()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
