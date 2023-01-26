from paquete.cliente import *

opcion = 99
cliente = None


def menu():
	print("Selecciona una opción")
	print("\t1 | Mostrar Items")
	print("\t2 | Comprar Item")
	print("\t3 | Ver productos comprados")
	print("\t9 | Salir")

while True:
    if cliente:
        menu()
        opcionMenu = int(input("inserta un numero valor >> ") or 0)

        match opcionMenu:
            case 1:
                show_items()
                input(" ")
            case 2:
                cliente.buy_item()
                input(" ")
            case 3:
                purchases()
                print(" ")
            case 9:            
                print("Saliendo...")
                break
            case _:
                input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

    else:
        cliente = init_user()