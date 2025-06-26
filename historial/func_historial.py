import json
import os
from datetime import datetime
from fpdf import FPDF  # Requiere pip install fpdf

HISTORIAL_FILE = "historial_operaciones.json"
MAX_HISTORIAL = 50

def guardar_operacion(expresion, resultado):
    """Guarda una operación en el historial"""
    historial = cargar_historial()
    
    operacion = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "expresion": expresion,
        "resultado": str(resultado)
    }
    
    historial.insert(0, operacion)
    historial = historial[:MAX_HISTORIAL]
    
    with open(HISTORIAL_FILE, 'w') as f:
        json.dump(historial, f, indent=2)

def cargar_historial():
    """Carga el historial de operaciones desde el archivo"""
    if not os.path.exists(HISTORIAL_FILE):
        return []
    
    try:
        with open(HISTORIAL_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def limpiar_historial():
    """Elimina todo el historial de operaciones"""
    if os.path.exists(HISTORIAL_FILE):
        os.remove(HISTORIAL_FILE)
        return True
    return False

def exportar_pdf(ruta):
    """Exporta el historial a un archivo PDF en la ruta especificada"""
    historial = cargar_historial()
    if not historial:
        return False
    
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        # Título
        pdf.cell(200, 10, txt="Historial de Operaciones - PyCalc", ln=1, align='C')
        
        # Contenido
        for operacion in historial:
            expresion = operacion["expresion"]
            resultado = operacion["resultado"]
            fecha = operacion["fecha"]
            
            texto = f"{fecha}: {expresion} = {resultado}"
            pdf.multi_cell(0, 10, txt=texto)
            pdf.ln(2)
        
        pdf.output(ruta)
        return True
    except Exception as e:
        print(f"Error al exportar PDF: {str(e)}")
        return False