menu = 0
while (menu != 3):
    print("""
    MINI MENU
    1. Opcion 1
    2. Opcion 2
    3. salir
    """)
    menu = input("Ingrese una opción: ")

    if menu.isdigit():
        if int(menu) == 1: 
            print("opcion 1")
        elif int(menu) == 2: 
            print("opción 2")
        elif int(menu) == 3:
            quit()
    else:
        print("Ingrese una opcion valida")