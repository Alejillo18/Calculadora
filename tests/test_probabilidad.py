import pytest
from operaciones.funciones_avanzadas import permutaciones, combinaciones, factorial, distribucion_normal

def test_permutaciones():
    assert permutaciones(5, 2) == 20

def test_combinaciones():
    assert combinaciones(5, 2) == 10

def test_factorial():
    assert factorial(5) == 120

def test_distribucion_normal():
    # Valor conocido: en mu=0, sigma=1, x=0 -> 1/sqrt(2*pi) ≈ 0.3989
    assert distribucion_normal(0, 0, 1) == pytest.approx(0.3989, abs=1e-4)