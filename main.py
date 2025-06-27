import sys
import tkinter as tk
from interfaz.interfaz_grafica import iniciar_interfaz_grafica, mostrar_resultado_cli
from operaciones.operacionesBasicas import calcular_expresion
from operaciones.funciones_avanzadas import resolver_sistema_ecuaciones, calculos_base

def main():
    if len(sys.argv) > 1:
        # Modo CLI
        expresion = ' '.join(sys.argv[1:])
        
        # Comandos especiales
        if expresion.startswith('solve:'):
            partes = expresion[6:].split(';')
            ecuaciones = partes[0].split(',')
            variables = partes[1].split(',') if len(partes) > 1 else ['x']
            try:
                solucion = resolver_sistema_ecuaciones(ecuaciones, variables)
                print("Solución:")
                for var, val in solucion.items():
                    print(f"{var} = {val}")
            except Exception as e:
                print(f"Error: {str(e)}")
        
        elif expresion.startswith('base:'):
            partes = expresion[5:].split(';')
            if len(partes) == 3:
                try:
                    resultado = calculos_base(partes[0], int(partes[1]), int(partes[2]))
                    print(f"Resultado: {resultado}")
                except Exception as e:
                    print(f"Error: {str(e)}")
            else:
                print("Formato: base:numero;base_entrada;base_salida")
        
        else:
            try:
                resultado = calcular_expresion(expresion)
                mostrar_resultado_cli(expresion, resultado)
            except Exception as e:
                print(f"Error: {str(e)}")
    else:
        # Modo GUI
        try:
            iniciar_interfaz_grafica()
        except Exception as e:
            tk.messagebox.showerror("Error Inesperado", f"Se produjo un error al iniciar la aplicación:\n{str(e)}")

if __name__ == "__main__":
    main()