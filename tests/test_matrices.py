import pytest
import numpy as np
from operaciones.funciones_avanzadas import operaciones_matriciales

def test_determinante():
    matriz = [[1, 2], [3, 4]]
    det = operaciones_matriciales([np.array(matriz)], 'det')
    assert det == pytest.approx(-2.0)

def test_inversa():
    matriz = [[1, 2], [3, 4]]
    inversa_esperada = np.linalg.inv(matriz)
    inversa_calculada = operaciones_matriciales([np.array(matriz)], 'inv')
    assert np.allclose(inversa_calculada, inversa_esperada)

def test_suma_matrices():
    matriz1 = [[1, 2], [3, 4]]
    matriz2 = [[5, 6], [7, 8]]
    suma_esperada = np.array([[6, 8], [10, 12]])
    suma_calculada = operaciones_matriciales([np.array(matriz1), np.array(matriz2)], 'add')
    assert np.array_equal(suma_calculada, suma_esperada)

def test_multiplicacion_matrices():
    matriz1 = [[1, 2], [3, 4]]
    matriz2 = [[5, 6], [7, 8]]
    mult_esperada = np.array([[19, 22], [43, 50]])
    mult_calculada = operaciones_matriciales([np.array(matriz1), np.array(matriz2)], 'mult')
    assert np.array_equal(mult_calculada, mult_esperada)