CALCULADORA CIENTIFICA

INTEGRANTES:
 Vicente Ybalo
 Alejo Oviedo
 Cristian Sasinka
 Facundo Castillo
 Lautaro Gutierrez Lardit

📘 Resumen del Proyecto
Nombre del sistema: Calculadora Científica PyCalc
Tecnología principal: Python 3.x
Frameworks/Bibliotecas sugeridas: Tkinter (GUI), NumPy/SymPy (operaciones matemáticas), Pytest (pruebas)
Público objetivo: Usuarios que necesiten realizar cálculos científicos complejos en una aplicación de escritorio o consola.
Modo de ejecución: Interfaz gráfica y línea de comandos (CLI)

🧩 Módulos Funcionales
Operaciones Aritméticas Básicas

Funciones Científicas (Trigonometría, logaritmos, exponenciales)

Funciones Avanzadas (Derivadas, integrales, simplificación simbólica)

Gestión de errores y validaciones

Historial de operaciones

Entrada de expresiones complejas

Interfaz de usuario (CLI y GUI)

🧠 Historias de Usuario y Criterios de Aceptación
🟩 Historia 1: Cálculos Aritméticos Básicos
Como usuario,
quiero poder realizar operaciones básicas como suma, resta, multiplicación y división,
para resolver cálculos cotidianos de manera rápida.

✅ Criterios de Aceptación
GIVEN el usuario ha ingresado una expresión como 3 + 2

WHEN presiona el botón "=" o ejecuta el cálculo

THEN el resultado debe ser 5

AND debe manejar divisiones por cero con un mensaje de error adecuado

🟩 Historia 2: Funciones Trigonométricas
Como usuario,
quiero usar funciones como sin(x), cos(x), tan(x) y sus inversas,
para poder realizar cálculos trigonométricos.

✅ Criterios de Aceptación
GIVEN el usuario ha ingresado sin(π/2)

WHEN ejecuta el cálculo

THEN el resultado debe ser 1

Soporte para ingresar valores en grados y radianes

Mensajes de error si se ingresan valores fuera del dominio (ej. tan(π/2))

🟩 Historia 3: Funciones Logarítmicas y Exponenciales
Como usuario,
quiero calcular logaritmos en base 10, base e y potencias,
para resolver problemas científicos y estadísticos.

✅ Criterios de Aceptación
log(100) devuelve 2

ln(e) devuelve 1

2^3 devuelve 8

Mensajes claros para entradas negativas en logaritmos

🟩 Historia 4: Derivadas e Integrales
Como estudiante de cálculo,
quiero poder obtener derivadas e integrales de funciones simbólicas,
para resolver problemas matemáticos avanzados.

✅ Criterios de Aceptación
d/dx(x^2) devuelve 2x

∫ x dx devuelve x^2/2 + C

Debe soportar funciones como sin(x^2) o e^x

Errores claros si se ingresa una expresión no derivable

🟩 Historia 5: Simplificación y Evaluación de Expresiones
Como usuario,
quiero ingresar expresiones algebraicas simbólicas,
para evaluarlas o simplificarlas.

✅ Criterios de Aceptación
simplify((x^2 - 1)/(x - 1)) debe devolver x + 1

evaluate(x=2) sobre x^2 + 2x devuelve 8

🟩 Historia 6: Manejo de Errores
Como usuario,
quiero recibir mensajes claros cuando algo sale mal,
para entender y corregir mis entradas.

✅ Criterios de Aceptación
Error por división por cero

Error por entrada inválida (ej: 5++2)

Mensajes amigables como "Entrada no válida. Revise su fórmula."

🟩 Historia 7: Historial de Operaciones
Como usuario frecuente,
quiero ver un historial de cálculos anteriores,
para revisar mis operaciones pasadas.

✅ Criterios de Aceptación
Debe guardar las últimas N operaciones

Posibilidad de volver a usar una expresión anterior

🟩 Historia 8: Interfaz Gráfica (GUI)
Como usuario no técnico,
quiero una interfaz amigable con botones y pantalla,
para facilitar el uso sin recordar sintaxis.

✅ Criterios de Aceptación
Botones para funciones y números

Campo de entrada y pantalla de salida

Soporte para teclado numérico

Interfaz responsiva y clara

🟩 Historia 9: Modo Consola (CLI)
Como usuario técnico,
quiero poder usar la calculadora desde la terminal,
para facilitar su integración con scripts y otros programas.

✅ Criterios de Aceptación
Entrada por texto (> calc "sin(pi/4) + log(10)")

Salida clara en consola

Soporte para modo interactivo y modo por línea de comandos

⚙️ Notas Técnicas / Consideraciones de Análisis Sistémico
🔧 Arquitectura Sugerida
Modelo MVC

Modelo: Procesamiento con SymPy / NumPy

Vista: GUI (Tkinter) y CLI

Controlador: Coordinación de entrada/salida y validaciones

📦 Modularidad
core/arithmetic.py: Suma, resta, etc.

core/scientific.py: Trigonometría, log, etc.

core/symbolic.py: Derivadas, integrales

ui/gui.py: Interfaz gráfica

ui/cli.py: Consola

utils/errors.py: Gestión de errores personalizados

🧪 Testing
Usar pytest para pruebas unitarias y de integración

Cobertura mínima del 90%

Tests para:

Casos normales

Casos límite

Manejo de errores

Performance en expresiones largas

🔁 Entradas/Salidas
Entrada: string, botón o teclado

Salida: string con resultado o mensaje de error

Internamente: manipulación simbólica con SymPy, cálculo con NumPy












CHAT DE LAS HISTORIAS DE USUARIO CON CHATGPT= https://chatgpt.com/share/685c74d5-2ee0-8003-a0cf-c86963de2271
| Integrante                | Link IA |
|---------------------------|---------|
| Vicente Ybalo             | https://chatgpt.com/share/684a1780-0a98-8003-a813-3a867b5e661e |
| Alejo Oviedo              | https://chatgpt.com/share/685c7b8f-7db8-8012-a66f-a03098d14854 |
| Cristian Sasinka          | https://chatgpt.com/share/685c74d5-2ee0-8003-a0cf-c86963de2271 |
| Facundo Castillo          | https://chatgpt.com/share/684a16c9-39b4-8009-b1eb-8849fb5a2996 |
| Lautaro Gutierrez Lardit  | https://chatgpt.com/c/685c85a3-1174-800c-b52b-584a6d471925 |
