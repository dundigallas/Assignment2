#Project
#Sanjana_Dundigalla
#0934886



import json

class UserManagement:
    """"
    Load users, save users, register users, login user

    """
    def load_users():
        try:
            with open("users.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
    def save_users(users):
        with open("users.json", "w") as file:
            json.dump(users, file)
    def register_user(username, password):
        users = UserManagement.load_users()
        if username in users:
            print("Username already exists. Please choose another one.")
            return False
        users[username] = password
        UserManagement.save_users(users)
        print("Registration successful.")
        return True

    def login_user(username, password):
        users = UserManagement.load_users()
        if username in users and users[username] == password:
            print("Login successful.")
            return True
        print("Invalid username or password.")
        return False
    

    

class InventoryManagement:   
    
    """"
    load inventory, save inventory, display inventory, add iventory, delete inventory, 
    """

    def load_inventory():
        try:
            with open("inventory.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_inventory(inventory):
        with open("inventory.json", "w") as file:
            json.dump(inventory, file)

    def display_inventory(inventory):
        print("Current Inventory:")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")

    def add_inventory(item, quantity):
        inventory = InventoryManagement.load_inventory()
        if item in inventory:
            inventory[item] += quantity
        else:
            inventory[item] = quantity
        InventoryManagement.save_inventory(inventory)

    def delete_inventory(item):
        inventory = InventoryManagement.load_inventory()
        if item in inventory:
            del inventory[item]
            InventoryManagement.save_inventory(inventory)
            print(f"{item} deleted from inventory.")
        else:
            print(f"{item} not found in inventory.")

    

def main():
    user_manager = UserManagement()
    inventory_manager = InventoryManagement()
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Display Inventory")
        print("4. Add Inventory")
        print("5. Delete Inventory")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter new username: ")
            password = input("Enter password: ")
            UserManagement.register_user(username, password)

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if UserManagement.login_user(username, password):
                while True:
                    print("\nWELCOME...")
                    print("\nInventory menu:")
                    print("\n1. Display Inventory")
                    print("2. Add Inventory")
                    print("3. Delete Inventory")
                    print("4. Logout")
                    choice = input("Enter your choice: ")
                    if choice == "1":
                        inventory = InventoryManagement.load_inventory()
                        InventoryManagement.display_inventory(inventory)
                    elif choice == "2":
                        item = input("Enter item name: ")
                        quantity = int(input("Enter quantity: "))
                        InventoryManagement.add_inventory(item, quantity)
                    elif choice == "3":
                        item = input("Enter item name to delete: ")
                        InventoryManagement.delete_inventory(item)
                    elif choice == "4":
                        break
                    else:
                        print("Invalid choice, please try again.")

        elif choice == "3":
            inventory = InventoryManagement.load_inventory()
            InventoryManagement.display_inventory(inventory)

        elif choice == "4":
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            InventoryManagement.add_inventory(item, quantity)

        elif choice == "5":
            item = input("Enter item name to delete: ")
            InventoryManagement.delete_inventory(item)

        elif choice == "9":
            print("Thank you...")
            break

        else:
            print("Invalid choice, please try again.")
    

if __name__ == "__main__":
    main()