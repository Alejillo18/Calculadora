import pytest
from operaciones.operacionesBasicas import calcular_expresion

def test_calculos_aritmeticos():
    assert calcular_expresion("2 + 3") == 5
    assert calcular_expresion("5 - 3") == 2
    assert calcular_expresion("4 * 3") == 12
    assert calcular_expresion("10 / 2") == 5
    assert calcular_expresion("2^3") == 8

def test_funciones_trigonometricas():
    assert calcular_expresion("sin(0)") == pytest.approx(0)
    assert calcular_expresion("cos(0)") == pytest.approx(1)
    assert calcular_expresion("tan(0)") == pytest.approx(0)
    assert calcular_expresion("sind(90)") == pytest.approx(1)
    assert calcular_expresion("cosd(180)") == pytest.approx(-1)

def test_logaritmos():
    assert calcular_expresion("log(100)") == pytest.approx(2)
    assert calcular_expresion("ln(e)") == pytest.approx(1)

def test_constantes():
    assert calcular_expresion("π") == pytest.approx(3.1415926535)
    assert calcular_expresion("e") == pytest.approx(2.7182818284)

def test_errores():
    # Expresión totalmente inválida
    with pytest.raises(ValueError, match="Expresión no válida"):
        calcular_expresion("@#$%^&")
    
    # Expresión con sintaxis incorrecta
    with pytest.raises(ValueError, match="Expresión no válida"):
        calcular_expresion("2 + * 3")
    
    # División por cero
    with pytest.raises(ValueError, match="División por cero"):
        calcular_expresion("5 / 0")
    
    # Función no definida
    with pytest.raises(ValueError, match="(Expresión no válida|Función no definida)"):
        calcular_expresion("funcion_inexistente(5)")