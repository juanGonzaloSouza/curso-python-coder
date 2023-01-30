class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f'{self.name} - ${self.price} - Stock: {self.stock}'

    def buy(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            print(f'Producto comprado, nuevo stock: {self.stock} ')
        else:
            print(f'No hay suficiente stock. Stock actual: {self.stock}!')

def get_items():
    item1 = Item("Laptop", 1000, 10)
    item2 = Item("Monitor", 200, 5)
    item3 = Item("Mouse", 20, 15)
    item4 = Item("Teclado", 40, 12)
    item5 = Item("Impresora", 80, 7)
    item6 = Item("Disco duro externo", 80, 20)
    item7 = Item("Bocinas", 50, 10)
    item8 = Item("Webcam", 30, 8)
    items = [item1, item2, item3, item4, item5, item6, item7, item8]
    return items

def show_items():
    for i, item in enumerate(get_items()):
        print(i+1,item)
    print(f'\n')

