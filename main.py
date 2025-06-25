#Aqui deben ir las importaciones, verificar rutas relativas


historial = []

# función para ver menú
def menu():
    print("\n=== Calculadora Científica ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("1. Seno (sin)")
    print("2. Coseno (cos)")
    print("3. Logaritmo natural (ln)")
    print("4. Potencia (base^exponente)")
    print("5. Ver historial (sesión actual)")
    print("6. Ver historial completo desde archivo")
    print("7. Salir")
    print("8. Buscar en historial por fecha y/u operación")
    print("9. Recuperar operación por expresión exacta")
    print("10. Borrar historial completo")
    return input("Selecciona una opción (1-10): ")


# programa principal
while True:
    opcion = menu()

    if opcion == '1':
        print("hola")
    else:
        print("Opción no válida. Intenta nuevamente.")