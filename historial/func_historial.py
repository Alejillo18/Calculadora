import json
import os
from datetime import datetime

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