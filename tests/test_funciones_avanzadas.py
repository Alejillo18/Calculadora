import pytest
import numpy as np
from operaciones.funciones_avanzadas import (
    resolver_sistema_ecuaciones,
    operaciones_matriciales,
    calculos_estadisticos,
    calculos_base,
    permutaciones,
    combinaciones
)

def test_sistema_ecuaciones():
    ecuaciones = ["2*x + y = 5", "x - y = 1"]
    variables = ["x", "y"]
    solucion = resolver_sistema_ecuaciones(ecuaciones, variables)
    assert solucion["x"] == pytest.approx(2)
    assert solucion["y"] == pytest.approx(1)

def test_operaciones_matriciales():
    matriz = np.array([[1, 2], [3, 4]])
    det = operaciones_matriciales([matriz], 'det')
    assert det == pytest.approx(-2)
    
    suma = operaciones_matriciales([matriz, matriz], 'add')
    assert np.array_equal(suma, np.array([[2, 4], [6, 8]]))

def test_estadisticas():
    datos = [1, 2, 3, 4, 5]
    assert calculos_estadisticos(datos, 'media') == 3
    assert calculos_estadisticos(datos, 'mediana') == 3
    assert calculos_estadisticos(datos, 'desv') == pytest.approx(1.4142, 0.001)

def test_conversion_base():
    assert calculos_base("1010", 2, 10) == "10"
    assert calculos_base("12", 10, 2) == "1100"
    assert calculos_base("A", 16, 10) == "10"

def test_combinatoria():
    assert permutaciones(5, 2) == 20
    assert combinaciones(5, 2) == 10