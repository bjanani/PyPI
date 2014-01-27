#A python program in defining classes#

class Product:

    def __init__(self, price, product,quantity):
        self.price = price
        self.pid = pid
        self.qty = qty

    def update_qty(self, qty, method='add'):
        if method == 'add':
            self.qty += qty
        elif method == 'subtract':
            self.qty = max(0, self.qty - qty)

    def print_product(self):
        print '%d\t%s\t%.02f each' % (self.pid, self.qty, self.price)

class Inventory:

    def __init__(self):
        self.products = [] # list to hold all products

    def add(self, product):
        self.products.append(product)

    def print_inventory(self):
        value = 0
        for product in self.products:
            print '%d\t%s\t%.02f each' % (product.pid,product.price)
            value += (product.price * product.qty)
        print '\nTotal value: %.02f' % value
if __name__ == '__main__':
    p1 = Product(1.4, 123, 5)
    p2 = Product(1, 3432, 100)
    p3 = Product(100.4, 2342, 99)
    i = Inventory()
    i.add(p1)
    i.add(p2)
    i.add(p3)
    i.print_inventory()

    p1.update_qty(10)
    i.print_inventory()
    
    p1.update_qty(10, method='subtract')
    i.print_inventory
