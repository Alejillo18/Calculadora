import pytest
from operaciones.funciones_avanzadas import resolver_sistema_ecuaciones

def test_resolver_sistema_2x2():
    ecuaciones = ["2x + 3y = 8", "4x - y = 2"]
    variables = ['x', 'y']
    solucion = resolver_sistema_ecuaciones(ecuaciones, variables)
    assert solucion == {'x': 1.0, 'y': 2.0}

def test_resolver_sistema_3x3():
    ecuaciones = ["x + y + z = 6", "2x + y + 3z = 14", "x - y + z = 2"]
    variables = ['x', 'y', 'z']
    solucion = resolver_sistema_ecuaciones(ecuaciones, variables)
    # Solución real: x=0, y=2, z=4
    assert solucion == {'x': 0.0, 'y': 2.0, 'z': 4.0}

def test_sistema_sin_solucion():
    ecuaciones = ["x + y = 1", "x + y = 2"]
    variables = ['x', 'y']
    solucion = resolver_sistema_ecuaciones(ecuaciones, variables)
    assert "No se encontró solución" in solucion.values()