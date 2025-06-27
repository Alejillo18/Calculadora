import numpy as np
from sympy import symbols, lambdify, sympify, SympifyError

def evaluar_expresion(expresion, variable='x', valor=0):
    """Evalúa una expresión en un punto dado"""
    try:
        x = symbols(variable)
        expr = sympify(expresion)
        f = lambdify(x, expr, modules=['numpy'])
        return float(f(valor))
    except SympifyError:
        raise ValueError("Expresión no válida para evaluación")
    except Exception as e:
        raise ValueError(f"Error al evaluar expresión: {str(e)}")

def resolver_sistema(ecuaciones):
    """Resuelve un sistema de ecuaciones (implementación básica)"""
    # Esta es una implementación simplificada
    # En una versión completa se usaría sympy.solve o numpy.linalg
    try:
        if len(ecuaciones) == 2:
            # Ejemplo simple para 2 ecuaciones lineales
            x, y = symbols('x y')
            soluciones = []
            for eq in ecuaciones:
                expr = sympify(eq)
                soluciones.append(expr)
            from sympy import solve
            sol = solve(soluciones, (x, y))
            return str(sol)
        else:
            return "Sistema no soportado (implementación básica)"
    except Exception as e:
        raise ValueError(f"Error al resolver sistema: {str(e)}")