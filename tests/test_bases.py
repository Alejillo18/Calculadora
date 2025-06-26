import pytest
from operaciones.funciones_avanzadas import calculos_base

def test_base_10_a_2():
    assert calculos_base('10', 10, 2) == '1010'

def test_base_2_a_10():
    assert calculos_base('1010', 2, 10) == '10'

def test_base_16_a_10():
    assert calculos_base('A', 16, 10) == '10'

def test_base_10_a_16():
    assert calculos_base('10', 10, 16) == 'A'

def test_base_8_a_10():
    assert calculos_base('12', 8, 10) == '10'

def test_base_10_a_8():
    assert calculos_base('10', 10, 8) == '12'