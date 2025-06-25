# Lista global para almacenar el historial
historial = []

def agregar_al_historial(operacion, resultado):
    if len(historial) >= 5:
        historial.pop(0)  # elimina la operación más antigua
    historial.append(f"{operacion} = {resultado}")

def mostrar_historial():
    if historial:
        print("\nÚltimas 5 operaciones:")
        for operacion in historial:
            print(f"- {operacion}")
    else:
        print("\nNo hay historial disponible.")

def borrar_historial():
    historial.clear()
    print("\nHistorial borrado correctamente.")
