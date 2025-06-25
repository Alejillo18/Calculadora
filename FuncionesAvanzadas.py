import math

def mostrar_menu():
    print("\nCalculadora Avanzada")
    print("1. Potencia (x^y)")
    print("2. Raíz cuadrada")
    print("3. Raíz enésima (n√x)")
    print("4. Logaritmo base 10")
    print("5. Logaritmo natural (ln)")
    print("6. Salir")

def calculadora():
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción (1-6): ")

        if opcion == "1":
            x = float(input("Base (x): "))
            y = float(input("Exponente (y): "))
            print(f"Resultado: {x} ^ {y} = {math.pow(x, y)}")

        elif opcion == "2":
            x = float(input("Número: "))
            if x < 0:
                print("Error: no se puede calcular raíz cuadrada de un número negativo.")
            else:
                print(f"Resultado: √{x} = {math.sqrt(x)}")

        elif opcion == "3":
            x = float(input("Número: "))
            n = float(input("Índice (n): "))
            if x < 0 and n % 2 == 0:
                print("Error: raíz par de un número negativo.")
            else:
                resultado = x ** (1 / n)
                print(f"Resultado: {n}√{x} = {resultado}")

        elif opcion == "4":
            x = float(input("Número (mayor que 0): "))
            if x <= 0:
                print("Error: el logaritmo solo está definido para números positivos.")
            else:
                print(f"Resultado: log10({x}) = {math.log10(x)}")

        elif opcion == "5":
            x = float(input("Número (mayor que 0): "))
            if x <= 0:
                print("Error: el logaritmo solo está definido para números positivos.")
            else:
                print(f"Resultado: ln({x}) = {math.log(x)}")

        elif opcion == "6":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intentá de nuevo.")

calculadora()
