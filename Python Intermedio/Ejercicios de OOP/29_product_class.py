# Cree una clase Product con:
# Nombre, precio y cantidad
# Cree una clase Inventory que:
# Guarde productos en una lista
# Tenga métodos para:
# Agregar un producto
# Mostrar todos los productos
# Calcular el valor total del inventario

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory():
    def __init__(self):
        self.product_list = []
        
    def append_product (self, product):
        self.product_list.append(product)
        print(f"{product} was added to the inventory.")


    def show_product_list(self):
        for product in self.product_list:
            print(f"{product.name:<20} {product.price:<10} {product.quantity:<10}")


    def get_inventory_total_price(self):
        total = 0
        for product in self.product_list:
            total = total + (product.price * product.quantity)
        print(f"The total cost of inventory is {total}")
        

def main ():
    inventory = Inventory()
    inventory.append_product(Product("Pen", 1.00, 100))
    inventory.append_product(Product("Notebook", 1.75, 200))
    inventory.append_product(Product("Marker", 2.00, 50))
    inventory.show_product_list()
    inventory.get_inventory_total_price()


main()