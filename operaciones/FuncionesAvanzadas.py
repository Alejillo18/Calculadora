import math


def potencia(x,y):
    return math.pow(x, y)


def raizCuadrada(x):
    if x < 0:
        return "error"
    else:
     return (math.sqrt(x))

def raizenesima(x,n):
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

