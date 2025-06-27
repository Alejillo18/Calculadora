import pytest
from operaciones.operacionesAvanzadas import (
    calcular_derivada,
    calcular_integral,
    simplificar_expresion
)

def test_calculadora_avanzada():
    assert calcular_derivada("x^2", "x") == "2*x"
    assert calcular_integral("2*x", "x") == "x**2 + C"
    assert simplificar_expresion("(x+1)*(x-1)") == "x**2 - 1"