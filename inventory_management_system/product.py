# product.py

class Product:
    def __init__(self, product_id, name, category, price, stock):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def __repr__(self):
        return f"Product(id={self.product_id}, name={self.name}, category={self.category}, price={self.price}, stock={self.stock})"
