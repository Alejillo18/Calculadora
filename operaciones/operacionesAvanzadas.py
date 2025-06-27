from sympy import symbols, diff, integrate, simplify, sympify, SympifyError
from sympy.parsing.sympy_parser import parse_expr

def calcular_derivada(expresion, variable='x'):
    """Calcula la derivada de una expresión respecto a una variable"""
    try:
        # Reemplazar '^' por '**' para exponentes
        expresion = expresion.replace('^', '**')
        x = symbols(variable)
        expr = parse_expr(expresion)
        derivada = diff(expr, x)
        return str(derivada)
    except SympifyError:
        raise ValueError("Expresión no válida para derivación")
    except Exception as e:
        raise ValueError(f"Error al calcular derivada: {str(e)}")

def calcular_integral(expresion, variable='x'):
    """Calcula la integral indefinida de una expresión respecto a una variable"""
    try:
        x = symbols(variable)
        expr = parse_expr(expresion)
        integral = integrate(expr, x)
        return str(integral) + " + C"
    except SympifyError:
        raise ValueError("Expresión no válida para integración")
    except Exception as e:
        raise ValueError(f"Error al calcular integral: {str(e)}")

def simplificar_expresion(expresion):
    """Simplifica una expresión algebraica"""
    try:
        expr = parse_expr(expresion)
        simplificado = simplify(expr)
        return str(simplificado)
    except SympifyError:
        raise ValueError("Expresión no válida para simplificación")
    except Exception as e:
        raise ValueError(f"Error al simplificar expresión: {str(e)}")