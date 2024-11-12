# inventory_system.py

# inventory_system.py

from data_store import DataStore
from product import Product
from user import User, Role
import getpass

class InventorySystem:
    LOW_STOCK_THRESHOLD = 5  # Set a low stock threshold for restocking alerts

    def __init__(self):
        self.data_store = DataStore()
        self.current_user = None

    def login(self):
        print("\n--- Login ---")
        username = input("Username: ")
        password = getpass.getpass("Password: ")

        for user in self.data_store.users:
            if user.username == username and user.password == password:
                self.current_user = user
                print(f"\nWelcome, {self.current_user.username}!")
                self.show_main_menu()
                return

        print("Invalid username or password.")

    def show_main_menu(self):
        while self.current_user:

            if self.current_user.role.name == "admin":
                print("\n--- Main Menu ---")
                print("1. View Products")
                print("2. View Users")
                print("3. View Roles & Permissions")
                print("4. Logout")
            else:
                print("\n--- Main Menu ---")
                print("1. View Products")
                print("4. Logout")  

            choice = input("Choose an option: ")
            if choice == "1":
                self.view_products()
            elif choice == "2":
                self.view_users()
            elif choice == "3":
                self.view_roles_permissions()
            elif choice == "4":
                self.logout()
            else:
                print("Invalid choice. Please try again.")

    # Product methods
    def view_products(self):
        if "view_products" not in self.current_user.role.permissions:
            print("Access denied: You do not have permission to view products.")
            return

        print("\n--- Product List ---")
        for product in self.data_store.products:
            stock_alert = " (Low stock! Consider restocking)" if int(product.stock) <= InventorySystem.LOW_STOCK_THRESHOLD else ""
            print(f"ID: {product.product_id}, Name: {product.name}, Category: {product.category}, Price: ${product.price}, Stock: {product.stock}{stock_alert}")

        if self.current_user.role.name == "admin":
            print("\n1. Add New Product")
            print("2. Update Product")
            print("3. Delete Product")
            print("4. Search Products")
            print("5. Filter Products by Stock Level")
            print("6. Adjust Stock Levels")
            print("7. Back to Main Menu")
        else:
            print("4. Search Products")
            print("7. Back to Main Menu")   

        choice = input("Choose an option: ")
        if choice == "1":
            self.add_product()
        elif choice == "2":
            self.update_product()
        elif choice == "3":
            self.delete_product()
        elif choice == "4":
            self.search_products()
        elif choice == "5":
            self.filter_products_by_stock()
        elif choice == "6":
            self.adjust_stock_levels()
        elif choice == "7":
            return
        else:
            print("Invalid choice. Please try again.")

    def add_product(self):
        name = input("Enter product name: ")
        category = input("Enter product category: ")
        price = float(input("Enter product price: "))
        while True:
            try:
                stock = int(input("Enter product stock level: "))
                break
            except ValueError:
                print("Please enter a valid integer for stock.")

        product_id = len(self.data_store.products) + 1
        new_product = Product(product_id, name, category, price, stock)
        self.data_store.products.append(new_product)
        print("Product added successfully.")

    def update_product(self):
        product_id = int(input("Enter product ID to update: "))
        product = next((p for p in self.data_store.products if p.product_id == product_id), None)
        if product:
            product.name = input(f"Enter new name (current: {product.name}): ") or product.name
            product.category = input(f"Enter new category (current: {product.category}): ") or product.category
            product.price = float(input(f"Enter new price (current: {product.price}): ") or product.price)

            while True:
                try:
                    product.stock = int(input(f"Enter new stock level (current: {product.stock}): ") or product.stock)
                    break
                except ValueError:
                    print("Please enter a valid integer for stock.")

            print("Product updated successfully.")
        else:
            print("Product not found.")

    def delete_product(self):
        product_id = int(input("Enter product ID to delete: "))
        product = next((p for p in self.data_store.products if p.product_id == product_id), None)
        if product:
            self.data_store.products.remove(product)
            print("Product deleted successfully.")
        else:
            print("Product not found.")

    def search_products(self):
        search_name = input("Enter product name to search: ").lower()
        search_category = input("Enter product category to search: ").lower()
        filtered_products = [
            p for p in self.data_store.products
            if search_name in p.name.lower() or search_category in p.category.lower()
        ]

        print("\n--- Search Results ---")
        for product in filtered_products:
            print(f"ID: {product.product_id}, Name: {product.name}, Category: {product.category}, Price: ${product.price}, Stock: {product.stock}")

    def filter_products_by_stock(self):
        stock_limit = int(input("Enter minimum stock level to filter by: "))
        filtered_products = [p for p in self.data_store.products if p.stock >= stock_limit]

        print("\n--- Filtered Product List ---")
        for product in filtered_products:
            print(f"ID: {product.product_id}, Name: {product.name}, Price: ${product.price}, Stock: {product.stock}")

    def adjust_stock_levels(self):
        product_id = int(input("Enter product ID to adjust stock: "))
        product = next((p for p in self.data_store.products if p.product_id == product_id), None)
        if product:
            adjustment = int(input("Enter amount to adjust stock (positive to add, negative to reduce): "))
            product.stock += adjustment
            print(f"Stock adjusted. New stock level for {product.name} is {product.stock}.")
        else:
            print("Product not found.")

    # User methods
    def view_users(self):
        if "view_users" not in self.current_user.role.permissions:
            print("Access denied: You do not have permission to view users.")
            return

        print("\n--- User List ---")
        for user in self.data_store.users:
            #print(f"ID: {user.user_id}, Username: {user.username}, Role: {user.role.name}")
            print(f"ID: {user.user_id}, Username: {user.username}, Role: {user.role.name}")

        print("\n1. Add New User")
        print("2. Update User")
        print("3. Delete User")
        print("4. Filter Users by Role")
        print("5. Back to Main Menu")

        choice = input("Choose an option: ")
        if choice == "1":
            self.add_user()
        elif choice == "2":
            self.update_user()
        elif choice == "3":
            self.delete_user()
        elif choice == "4":
            self.filter_users_by_role()
        elif choice == "5":
            return
        else:
            print("Invalid choice. Please try again.")

    def add_user(self):
        try:
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            role_name = input("Enter role admin/accountant/user: ")
            role = next((r for r in self.data_store.roles if r.name == role_name), None)
            print(role)
            if role:
                user_id = len(self.data_store.users) + 1
                new_user = User(user_id, username, password, role)
                self.data_store.users.append(new_user)
                print("User added successfully.")
            else:
                print("Error: Role not found. Please enter a valid role.")

        except Exception as e:
            print(f"An error occurred: {e}")

    def update_user(self):
        try:
            user_id = int(input("Enter user ID to update: "))
            user = next((u for u in self.data_store.users if u.user_id == user_id), None)

            if user:
                user.username = input(f"Enter new username (current: {user.username}): ") or user.username
                password = getpass.getpass(f"Enter new password (current: {user.password}): ")
                user.password = password if password else user.password
                role_name = input(f"Enter new role (current: {user.role.name}): ").capitalize() or user.role.name
                role = next((r for r in self.data_store.roles if r.name == role_name), None)

                if role:
                    user.role = role
                    print("User updated successfully.")
                else:
                    print("Error: Role not found.")
            else:
                print("Error: User not found.")

        except ValueError:
            print("Invalid input. Please enter a numeric value for user ID.")

    def delete_user(self):
        try:
            user_id = int(input("Enter user ID to delete: "))
            user = next((u for u in self.data_store.users if u.user_id == user_id), None)

            if user:
                self.data_store.users.remove(user)
                print("User deleted successfully.")
            else:
                print("Error: User not found.")

        except ValueError:
            print("Invalid input. Please enter a numeric value for user ID.")

    def filter_users_by_role(self):
        role_name = input("Enter role name to filter by: ").capitalize()
        filtered_users = [u for u in self.data_store.users if u.role.name == role_name]

        print("\n--- Filtered User List ---")
        for user in filtered_users:
            print(f"ID: {user.user_id}, Username: {user.username}, Role: {user.role.name}")

    # Role & Permission methods
    def view_roles_permissions(self):
        if "view_roles" not in self.current_user.role.permissions:
            print("Access denied: You do not have permission to view roles and permissions.")
            return

        print("\n--- Roles & Permissions ---")
        for role in self.data_store.roles:
            print(f"Role: {role.name}, Permissions: {', '.join(role.permissions)}")

        print("\n1. Add New Role")
        print("2. Update Role Permissions")
        print("3. Delete Role")
        print("4. Filter Roles by Permission")
        print("5. Back to Main Menu")

        choice = input("Choose an option: ")
        if choice == "1":
            self.add_role()
        elif choice == "2":
            self.update_role_permissions()
        elif choice == "3":
            self.delete_role()
        elif choice == "4":
            self.filter_roles_by_permission()
        elif choice == "5":
            return
        else:
            print("Invalid choice. Please try again.")

    def add_role(self):
        role_name = input("Enter role name: ").capitalize()
        permissions = input("Enter permissions (comma-separated): ").split(',')

        new_role = Role(role_name, [perm.strip() for perm in permissions])
        self.data_store.roles.append(new_role)
        print("Role added successfully.")

    def update_role_permissions(self):
        role_name = input("Enter role name to update: ").capitalize()
        role = next((r for r in self.data_store.roles if r.name == role_name), None)

        if role:
            permissions = input(f"Enter new permissions (current: {', '.join(role.permissions)}): ").split(',')
            role.permissions = [perm.strip() for perm in permissions]
            print("Permissions updated successfully.")
        else:
            print("Error: Role not found.")

    def delete_role(self):
        role_name = input("Enter role name to delete: ").capitalize()
        role = next((r for r in self.data_store.roles if r.name == role_name), None)

        if role:
            self.data_store.roles.remove(role)
            print("Role deleted successfully.")
        else:
            print("Error: Role not found.")

    def filter_roles_by_permission(self):
        permission = input("Enter permission to filter roles by: ").strip()
        filtered_roles = [r for r in self.data_store.roles if permission in r.permissions]

        print("\n--- Filtered Roles ---")
        for role in filtered_roles:
            print(f"Role: {role.name}, Permissions: {', '.join(role.permissions)}")

    def logout(self):
        self.current_user = None
        print("Logged out successfully.\n")
