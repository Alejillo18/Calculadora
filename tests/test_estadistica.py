import pytest
from operaciones.funciones_avanzadas import calculos_estadisticos

def test_media():
    datos = [1, 2, 3, 4, 5]
    media = calculos_estadisticos(datos, 'media')
    assert media == pytest.approx(3.0)

def test_mediana():
    datos = [1, 2, 3, 4, 5]
    mediana = calculos_estadisticos(datos, 'mediana')
    assert mediana == 3.0

def test_desviacion_estandar():
    datos = [1, 2, 3, 4, 5]
    desv = calculos_estadisticos(datos, 'desv')
    assert desv == pytest.approx(1.414213, abs=1e-6)

def test_varianza():
    datos = [1, 2, 3, 4, 5]
    var = calculos_estadisticos(datos, 'var')
    assert var == pytest.approx(2.0)

def test_regresion_lineal():
    datos = [0, 2, 4, 6]  # y = 2*x (x: 0,1,2,3)
    reg = calculos_estadisticos(datos, 'reg_lin')
    assert reg[0] == pytest.approx(2.0)  # pendiente
    assert reg[1] == pytest.approx(0.0, abs=1e-12)  # intercepto