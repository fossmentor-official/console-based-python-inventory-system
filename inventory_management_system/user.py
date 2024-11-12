# user.py

class Role:
    def __init__(self, role_name, permissions):
        self.name = role_name
        self.permissions = permissions  # permissions is a list of permission strings like ["view_products"]

    def __repr__(self):
        return f"Role(name={self.name}, permissions={self.permissions})"


class User:
    def __init__(self, user_id, username, password, role):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role

    def __repr__(self):
        return f"User(username={self.username}, role={self.role.name})"
