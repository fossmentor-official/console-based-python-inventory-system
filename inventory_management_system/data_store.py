# data_store.py

from user import User, Role
from product import Product

class DataStore:
    def __init__(self):
        self.users = []
        self.roles = []
        self.products = []
        self.initialize_data()

    def initialize_data(self):
        # Initialize roles
        admin_role = Role("admin", ["view_products", "manage_products", "view_users", "manage_users"])
        account_role = Role("accountant", ["view_products", "view_users"])
        viewer_role = Role("user", ["view_products"])

        # Initialize users with default admin2
        self.roles.extend([admin_role, viewer_role])
        self.users.append(User(1, "admin", "admin", admin_role))
        self.users.append(User(2, "account", "account", account_role))
        self.users.append(User(3, "user", "user", viewer_role))

        # Initialize products
        self.products.append(Product(1, "Laptop", "Computer", 1500.00, 10))
        self.products.append(Product(2, "Mouse", "Accessory", 25.00, 100))
        self.products.append(Product(3, "Keyboard", "Accessory", 45.00, 50))
