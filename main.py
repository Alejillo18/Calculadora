#Aqui deben ir las importaciones, verificar rutas relativas
from operaciones.FuncionesAvanzadas import potencia,raizCuadrada,raizenesima,logbase10,lognatural

historial = []

# función para ver menú
def menu():
    print("\n=== Calculadora Científica ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Seno (sin)")
    print("6. Coseno (cos)")
    print("7. Logaritmo natural (ln)")
    print("8. Potencia (base^exponente)")
    print("9. Raiz Cuadrada")
    print("10. logaritmo en base 10'")
    print("11. Raiz 'Enesima'")
    print("12. Ver historial (sesión actual)")
    print("13. Ver historial completo desde archivo")
    print("14. Salir")
    print("15. Buscar en historial por fecha y/u operación")
    print("16. Recuperar operación por expresión exacta")
    print("17. Borrar historial completo")
    return input("Selecciona una opción (1-14): ")


# programa principal
while True:
    opcion = menu()

    if opcion == '1':
        print("hola")


    elif opcion == '7':
        lognatural()
    elif opcion == '8':
        potencia()
    elif opcion == '9':
        raizCuadrada()
    elif opcion == '10':
        logbase10()
    elif opcion == '11':
        raizenesima()
    else:
        print("Opción no válida. Intenta nuevamente.")