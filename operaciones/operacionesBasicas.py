import re
import math
from sympy import sympify, SympifyError, integrate, symbols, diff, simplify, N, solve, Eq, factorial as sp_factorial, zoo
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application, parse_expr
from .funciones_avanzadas import calculos_fracciones, permutaciones, combinaciones, distribucion_normal
from sympy import pi, E, sin, cos, tan, log

transformations = (standard_transformations + (implicit_multiplication_application,))

def calcular_expresion(expresion):
    """Evalúa una expresión matemática."""
    try:
        # Reemplazar '^' por '**' para exponentes
        expresion = expresion.replace('^', '**')
        
        # Crear contexto con funciones y constantes
        context = {
            'sin': sin,
            'cos': cos,
            'tan': tan,
            'sind': lambda x: sin(math.radians(x)),  # Grados a radianes
            'cosd': lambda x: cos(math.radians(x)),
            'tand': lambda x: tan(math.radians(x)),
            'log': lambda x: log(x, 10),  # Logaritmo base 10
            'ln': log,                    # Logaritmo natural
            'π': pi,
            'e': E
        }

        # Manejo especial para fracciones
        if 'frac(' in expresion:
            match = re.search(r'frac\(([^)]+)\)', expresion)
            if match:
                frac_expr = match.group(1).strip()
                resultado_frac = calculos_fracciones(frac_expr)
                expresion = expresion.replace(f'frac({frac_expr})', resultado_frac)
        
        # Manejo especial para integrales
        integral_match_def = re.search(r'integral\(([^,]+),([^,]+),([^,]+),([^)]+)\)', expresion)
        integral_match_indef = re.search(r'integral\(([^,]+),([^)]+)\)', expresion)
        
        if integral_match_def:
            expr_str = integral_match_def.group(1).strip()
            var_str = integral_match_def.group(2).strip()
            lower_str = integral_match_def.group(3).strip()
            upper_str = integral_match_def.group(4).strip()
            
            expr = parse_expr(expr_str, transformations=transformations, local_dict=context)
            var = symbols(var_str)
            lower = parse_expr(lower_str, transformations=transformations, local_dict=context)
            upper = parse_expr(upper_str, transformations=transformations, local_dict=context)
            
            resultado = integrate(expr, (var, lower, upper))
            resultado_num = resultado.evalf()
            
            if resultado_num == zoo:
                raise ValueError("Error: División por cero")
                
            if resultado_num.is_Number:
                return float(N(resultado_num, 10))
            return str(resultado)
        
        elif integral_match_indef:
            expr_str = integral_match_indef.group(1).strip()
            var_str = integral_match_indef.group(2).strip()
            
            expr = parse_expr(expr_str, transformations=transformations, local_dict=context)
            var = symbols(var_str)
            integral = integrate(expr, var)
            return str(integral) + " + C"
        
        # Manejo especial para derivadas
        deriv_match = re.search(r'd/dx\(([^)]+)\)', expresion)
        if deriv_match:
            expr_str = deriv_match.group(1).strip()
            expr = parse_expr(expr_str, transformations=transformations, local_dict=context)
            x = symbols('x')
            derivada = diff(expr, x)
            return str(derivada)
        
        # Manejo especial para simplificación
        simpl_match = re.search(r'simplify\(([^)]+)\)', expresion)
        if simpl_match:
            expr_str = simpl_match.group(1).strip()
            expr = parse_expr(expr_str, transformations=transformations, local_dict=context)
            simplificado = simplify(expr)
            return str(simplificado)
        
        # Manejo especial para ecuaciones
        if 'solve(' in expresion:
            match = re.search(r'solve\(([^,]+),([^)]+)\)', expresion)
            if match:
                eq_str = match.group(1).strip()
                var_str = match.group(2).strip()
                
                eq_parts = eq_str.split('=')
                if len(eq_parts) != 2:
                    raise ValueError("Ecuación debe tener formato: expresión = expresión")
                
                lhs = parse_expr(eq_parts[0], transformations=transformations, local_dict=context)
                rhs = parse_expr(eq_parts[1], transformations=transformations, local_dict=context)
                var = symbols(var_str)
                
                solucion = solve(Eq(lhs, rhs), var)
                if solucion:
                    return ', '.join([str(s) for s in solucion])
                else:
                    return "No se encontró solución"
        
        # Manejo especial para permutaciones y combinaciones
        if 'nPr(' in expresion:
            match = re.search(r'nPr\((\d+),(\d+)\)', expresion)
            if match:
                n = int(match.group(1))
                r = int(match.group(2))
                return str(permutaciones(n, r))
        
        if 'nCr(' in expresion:
            match = re.search(r'nCr\((\d+),(\d+)\)', expresion)
            if match:
                n = int(match.group(1))
                r = int(match.group(2))
                return str(combinaciones(n, r))
        
        # Manejo especial para factorial
        if 'factorial(' in expresion:
            match = re.search(r'factorial\((\d+)\)', expresion)
            if match:
                n = int(match.group(1))
                return str(sp_factorial(n))
        
        # Manejo especial para distribución normal
        if 'normal_dist(' in expresion:
            match = re.search(r'normal_dist\(([^,]+),([^,]+),([^)]+)\)', expresion)
            if match:
                x = float(match.group(1))
                mu = float(match.group(2))
                sigma = float(match.group(3))
                return str(distribucion_normal(x, mu, sigma))
        
        # Evaluación general con contexto
        transformations_list = standard_transformations + (implicit_multiplication_application,)
        try:
            expr = parse_expr(expresion, local_dict=context, transformations=transformations_list)
            resultado = expr.evalf()
        except Exception as e:
            # Manejar errores de evaluación específicos
            error_msg = str(e).lower()
            if any(keyword in error_msg for keyword in ["could not convert", "invalid syntax", "name", "not defined", "function"]):
                raise ValueError("Expresión no válida")
            else:
                raise e
        
        # Manejar división por cero (zoo)
        if resultado == zoo:
            raise ValueError("Error: División por cero")
        
        # Convertir a float si es número
        if resultado.is_Number:
            return float(resultado)
        
        # Si el resultado no es numérico, verificar si hay funciones no definidas
        if any(func in expresion for func in ["funcion_inexistente"]):
            raise ValueError("Función no definida")
            
        return str(resultado)
        
    except SympifyError as se:
        raise ValueError(f"Error: Expresión no válida - {str(se)}")
    except Exception as e:
        raise ValueError(f"Error en el cálculo: {str(e)}")

def deg2rad(degrees):
    """Convierte grados a radianes"""
    return math.radians(degrees)