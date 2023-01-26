from paquete.compra import *
purchase = []

class Client:
    def  __init__(self, name, surname, id, payment):
        self.name = name
        self.surname = surname
        self.id = id
        self.payment = payment

    def __str__(self):
        return f'\nCliente: {self.name} {self.surname} con cedula: {self.id}. Pagará con: {self.payment}'
    
    def buy_item(self):
        show_items()
        intem, quantity = int(input("¿Que objeto va a comprar? ") or 0), int(input("Cantidad de ese objeto: ") or 0)
        if intem and quantity:
            item = get_items()[intem-1]
            print(f'{self.name} esta comprando {quantity} unidades de {item.name} en {self.payment}')
            item.buy(quantity)
            purchase.append({
                'articulo': f'{item.name}',
                'cantidad': f'{quantity}'
            })
        else:
            print("Solo se admiten numeros!")



def init_user():
    print(f'Creación de cliente \n')
    name = input("Ingresa tu nombre ")
    if name.isalpha():
        surname = input("Ingresa tu apellido ")
        if surname.isalpha():
            id = int(input("Ingresa tu cedula ") or None)
            if id:
                payment = input("¿Con qué va a pagar? ")
                if payment:
                    cliente = Client(name,surname,id,payment)
                    input(cliente)
                    return cliente
                else: 
                    print("Error")
            else: 
                print("Error")        
        else: 
            print("Error")
    else: 
        print("Error")


def purchases():
    for item in purchase:
        print(f' Compraste {item["cantidad"]} {item["articulo"]}')
