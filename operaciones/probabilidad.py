import math
import random
from scipy.stats import norm  # Requiere pip install scipy

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
    """Calcula la distribución normal"""
    return norm.pdf(x, mu, sigma)

def random_number(a, b):
    """Genera un número aleatorio entre a y b"""
    return random.uniform(a, b)