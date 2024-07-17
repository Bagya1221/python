class Product:
    def __init__(self, product_id, name, initial_stock):
        self.product_id = product_id
        self.name = name
        self.stock = initial_stock

class InventorySystem:
    def __init__(self):
        self.products = {}  # Product ID to Product mapping

    def add_product(self, product):
        self.products[product.product_id] = product

    def update_stock(self, product_id, quantity):
        if product_id in self.products:
            self.products[product_id].stock += quantity
        else:
            print(f"Product with ID {product_id} not found.")

    def check_stock(self, product_id):
        if product_id in self.products:
            return self.products[product_id].stock
        else:
            print(f"Product with ID {product_id} not found.")
            return None

    def reorder_alert(self, product_id, threshold):
        stock_level = self.check_stock(product_id)
        if stock_level is not None and stock_level < threshold:
            print(f"Alert: Product {product_id} stock is below threshold ({threshold}).")

# Example usage
if __name__ == "__main__":
    inventory = InventorySystem()

    # Add products
    product1 = Product("P123", "Widget A", 100)
    product2 = Product("P456", "Widget B", 50)
    inventory.add_product(product1)
    inventory.add_product(product2)

    # Update stock levels
    inventory.update_stock("P123", -20)
    inventory.update_stock("P456", 10)

    # Check stock levels
    print("Widget A stock:", inventory.check_stock("P123"))
    print("Widget B stock:", inventory.check_stock("P456"))

    # Generate reorder alerts
    inventory.reorder_alert("P123", threshold=30)
    inventory.reorder_alert("P456", threshold=20)
