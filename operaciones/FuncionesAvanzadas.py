import math

def potencia(x, y):
    return math.pow(x, y)

def raizCuadrada(x):
    if x < 0:
        return "error"
    else:
        return math.sqrt(x)

def raizenesima(x, n):
    if x < 0 and n % 2 == 0:
        return "error"
    else:
        return x ** (1 / n)

def logbase10(x):
    if x <= 0:
        return "error"
    else:
        return math.log10(x)

def lognatural(x):
    if x <= 0:
        return "error"
    else:
        return math.log(x)

def derivada(f, x, h=1e-5):
    """
    Calcula la derivada numérica de una función en un punto x.
    
    Parámetros:
    f: función a derivar (debe aceptar un solo argumento)
    x: punto donde se evalúa la derivada
    h: tamaño del paso (opcional, por defecto 1e-5)
    
    Retorna:
    Valor aproximado de la derivada en x
    """
    return (f(x + h) - f(x - h)) / (2 * h)

def integral_definida(f, a, b, n=1000):
    """
    Calcula la integral definida de una función usando la regla del trapecio.
    
    Parámetros:
    f: función a integrar (debe aceptar un solo argumento)
    a: límite inferior de integración
    b: límite superior de integración
    n: número de subdivisiones (opcional, por defecto 1000)
    
    Retorna:
    Valor aproximado de la integral definida
    """
    if a == b:
        return 0
    h = (b - a) / n
    suma = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        suma += f(a + i * h)
    return suma * h