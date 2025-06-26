import os
import pytest
from historial.func_historial import (
    guardar_operacion,
    cargar_historial,
    limpiar_historial,
    exportar_pdf
)

def test_historial_operaciones():
    # Limpiar cualquier historial previo
    if os.path.exists("historial_operaciones.json"):
        os.remove("historial_operaciones.json")
    
    guardar_operacion("2+2", 4)
    historial = cargar_historial()
    assert len(historial) == 1
    assert historial[0]["expresion"] == "2+2"
    assert historial[0]["resultado"] == "4"
    
    limpiar_historial()
    assert len(cargar_historial()) == 0

def test_exportar_pdf(tmp_path):
    guardar_operacion("3*4", 12)
    pdf_path = tmp_path / "historial.pdf"
    assert exportar_pdf(str(pdf_path)) is True
    assert os.path.exists(pdf_path)