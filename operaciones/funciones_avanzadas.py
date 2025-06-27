import numpy as np
from sympy import symbols, lambdify, sympify, solve, Eq, Matrix, integrate, diff, simplify
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application, parse_expr
import math
import random

def resolver_sistema_ecuaciones(ecuaciones, variables):
    """Resuelve sistemas de ecuaciones lineales"""
    try:
        # Transformaciones para manejar multiplicación implícita
        transformations = standard_transformations + (implicit_multiplication_application,)
        
        vars_sym = symbols(' '.join(variables))
        eqs = []
        for eq in ecuaciones:
            # Normalizar espacios alrededor del signo igual
            eq = eq.replace(' = ', '=')
            parts = eq.split('=')
            if len(parts) != 2:
                raise ValueError("Formato de ecuación incorrecto. Use: expresión = expresión")
            
            # Parsear con transformaciones para multiplicación implícita
            lhs = parse_expr(parts[0].strip(), transformations=transformations)
            rhs = parse_expr(parts[1].strip(), transformations=transformations)
            eqs.append(Eq(lhs, rhs))

        solucion = solve(eqs, vars_sym)
        if not solucion:
            return {"Solución": "No se encontró solución"}

        # Convertir a diccionario simple
        if isinstance(solucion, dict):
            return {str(k): float(v.evalf()) if hasattr(v, 'evalf') else v for k, v in solucion.items()}
        elif isinstance(solucion, list):
            return {f"Solución {i+1}": str(sol) for i, sol in enumerate(solucion)}
        else:
            return {"Solución": str(solucion)}
    except Exception as e:
        raise ValueError(f"Error al resolver sistema: {str(e)}")

def operaciones_matriciales(matrices, operacion):
    """Realiza operaciones con matrices"""
    try:
        if operacion == 'det':
            return np.linalg.det(matrices[0])
        elif operacion == 'inv':
            return np.linalg.inv(matrices[0])
        elif operacion == 'mult':
            return np.dot(matrices[0], matrices[1])
        elif operacion == 'add':
            return np.add(matrices[0], matrices[1])
    except Exception as e:
        raise ValueError(f"Error en operación matricial: {str(e)}")

def calculos_estadisticos(datos, operacion):
    """Realiza cálculos estadísticos"""
    try:
        if operacion in ['media', 'mediana', 'desv', 'var']:
            # Para estas operaciones, datos es una lista de números
            datos = [float(d) for d in datos]
            if operacion == 'media':
                return np.mean(datos)
            elif operacion == 'mediana':
                return np.median(datos)
            elif operacion == 'desv':
                return np.std(datos, ddof=1)  # Desviación muestral
            elif operacion == 'var':
                return np.var(datos, ddof=1)  # Varianza muestral

        elif operacion == 'reg_lin':
            # Asegurarse de que los datos son arrays 1D
            x = np.array(datos[0]).flatten()
            y = np.array(datos[1]).flatten()
            
            # Ajuste lineal
            coefs = np.polyfit(x, y, 1)
            slope = float(coefs[0])  # Convertir a float nativo
            intercept = float(coefs[1])  # Convertir a float nativo
            
            # Calcular correlación si hay suficientes datos
            if len(x) > 2:
                correlation_matrix = np.corrcoef(x, y)
                r = float(correlation_matrix[0, 1])
            else:
                # Para 2 puntos, la correlación es perfecta
                r = 1.0 if slope >= 0 else -1.0
            
            return {'slope': slope, 'intercept': intercept, 'r': r}

    except Exception as e:
        raise ValueError(f"Error en cálculo estadístico: {str(e)}")
    
def format_regresion(coeficientes):
    """Formatea los coeficientes de regresión como una ecuación legible"""
    pendiente = coeficientes[0]
    intercepto = coeficientes[1]
    signo = '+' if intercepto >= 0 else '-'
    return f"y = {pendiente:.4f}x {signo} {abs(intercepto):.4f}"

def calculos_base(numero, base_entrada, base_salida):
    """Convierte entre bases numéricas"""
    try:
        # Convertir a decimal primero
        if base_entrada == 2:
            decimal = int(str(numero), 2)
        elif base_entrada == 8:
            decimal = int(str(numero), 8)
        elif base_entrada == 16:
            decimal = int(str(numero), 16)
        else:
            decimal = int(numero)
        
        # Convertir a base de salida
        if base_salida == 2:
            return bin(decimal)[2:]
        elif base_salida == 8:
            return oct(decimal)[2:]
        elif base_salida == 16:
            return hex(decimal)[2:].upper()
        else:
            return str(decimal)
    except Exception as e:
        raise ValueError(f"Error en conversión de base: {str(e)}")

def calculos_fracciones(expresion):
    """Maneja cálculos con fracciones"""
    from fractions import Fraction
    try:
        return str(Fraction(expresion).limit_denominator())
    except:
        try:
            partes = expresion.split()
            entero = int(partes[0])
            fraccion = Fraction(partes[1])
            return str(entero + fraccion) if fraccion > 0 else str(entero - abs(fraccion))
        except:
            raise ValueError("Formato de fracción no válido")

def permutaciones(n, r):
    """Calcula permutaciones nPr"""
    if n < r:
        raise ValueError("n debe ser mayor o igual que r")
    return math.factorial(n) // math.factorial(n - r)

def combinaciones(n, r):
    """Calcula combinaciones nCr"""
    if n < r:
        raise ValueError("n debe ser mayor o igual que r")
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

def factorial(n):
    """Calcula factorial de un número"""
    return math.factorial(int(n))

def distribucion_normal(x, mu=0, sigma=1):
    """Calcula la distribución normal usando fórmula matemática"""
    if sigma == 0:
        raise ValueError("sigma no puede ser cero")
    return (1.0 / (sigma * math.sqrt(2 * math.pi))) * math.exp(- (x - mu)**2 / (2 * sigma**2))

def random_number(a, b):
    """Genera un número aleatorio entre a y b"""
    return random.uniform(a, b)