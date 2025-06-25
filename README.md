CALCULADORA CIENTIFICA

INTEGRANTES:
 Vicente Ybalo
 Alejo Oviedo
 Cristian Sasinka
 Facundo Castillo
 Lautaro Gutierrez Lardit










🧩 Épica General: Módulo de Calculadora Científica
Como usuario técnico o estudiante, quiero realizar cálculos matemáticos avanzados, para resolver problemas científicos, académicos o de ingeniería de manera precisa.

📝 Historias de Usuario (User Stories)
1. Realizar operaciones aritméticas básicas
Historia de Usuario
Como usuario, quiero realizar operaciones básicas como suma, resta, multiplicación y división para efectuar cálculos simples.

Criterios de Aceptación

 Se pueden introducir números positivos y negativos.

 Soporta decimales (coma o punto según localización).

 El resultado se actualiza tras presionar el botón "=".

 Se maneja la división por cero con un mensaje de error claro.

Notas Técnicas

Utilizar librerías de precisión decimal.

Localización del formato numérico (Ej: 3,14 vs 3.14).

2. Realizar operaciones científicas avanzadas
Historia de Usuario
Como usuario avanzado, quiero usar funciones científicas como seno, coseno, tangente, logaritmo, exponencial, raíces para resolver ecuaciones complejas.

Criterios de Aceptación

 Disponibilidad de funciones trigonométricas en radianes y grados.

 Logaritmo natural (ln) y logaritmo base 10 (log).

 Exponenciales (e^x) y potencia (x^y).

 Raíz cuadrada y enésima raíz.

 Se puede cambiar entre grados/radianes.

 Se muestra el resultado con precisión configurable.

Notas Técnicas

Validar entradas para evitar raíces de negativos si no hay soporte para números complejos.

3. Soporte para paréntesis y jerarquía de operaciones
Historia de Usuario
Como usuario, quiero usar paréntesis en mis expresiones para controlar la prioridad de las operaciones.

Criterios de Aceptación

 Se pueden anidar múltiples niveles de paréntesis.

 La jerarquía respeta PEMDAS/BODMAS.

 El sistema muestra errores si los paréntesis están mal balanceados.

Notas Técnicas

Se sugiere usar un parser de expresiones matemáticas (Ej: Shunting Yard Algorithm).

4. Historial de operaciones
Historia de Usuario
Como usuario frecuente, quiero ver el historial de operaciones realizadas para revisar o reutilizar cálculos anteriores.

Criterios de Aceptación

 Se listan las operaciones y resultados anteriores.

 Se puede seleccionar una operación pasada y reutilizarla.

 Se puede borrar el historial completo o por ítem.

Notas Técnicas

Almacenamiento en memoria local o persistente (por sesión o usuario).

Posibilidad de exportar historial en formato texto o CSV (opcional).

5. Manejo de constantes científicas
Historia de Usuario
Como usuario científico, quiero acceder rápidamente a constantes como π, e, g para realizar cálculos con valores estandarizados.

Criterios de Aceptación

 π (pi), e (número de Euler), g (gravedad), c (velocidad de la luz) disponibles.

 Se pueden insertar con un botón o mediante teclado.

Notas Técnicas

Configurar la precisión de cada constante.

Agrupar constantes por categoría (matemáticas, física, etc.).

6. Modo de notación científica
Historia de Usuario
Como usuario académico, quiero ver y usar notación científica para trabajar con números muy grandes o pequeños.

Criterios de Aceptación

 El usuario puede elegir mostrar resultados en notación científica.

 Se pueden ingresar números usando E o e (Ej: 1.23e-5).

 Botón para alternar entre notación normal y científica.

Notas Técnicas

Utilizar formatos estándar IEEE o similares.

Opciones de configuración de precisión de dígitos.

7. Conversión entre grados y radianes
Historia de Usuario
Como usuario que trabaja con ángulos, quiero cambiar entre grados y radianes para obtener resultados correctos en funciones trigonométricas.

Criterios de Aceptación

 Botón claro para alternar entre grados y radianes.

 Estado visible del modo actual.

 Las funciones trigonométricas se comportan según el modo activo.

Notas Técnicas

Estado debe mantenerse incluso si se reinicia la calculadora (opcional).

8. Validación de entradas y manejo de errores
Historia de Usuario
Como usuario, quiero recibir mensajes claros si hay un error en la expresión para entender qué corregir.

Criterios de Aceptación

 Error de sintaxis (Ej: “2+*5”) produce un mensaje claro.

 División por cero no causa crash.

 Paréntesis mal cerrados se indican visualmente.

Notas Técnicas

Se recomienda validación incremental conforme se ingresa la expresión.

9. Interfaz adaptable y accesible
Historia de Usuario
Como usuario con diferentes dispositivos, quiero una interfaz responsiva y accesible para usar la calculadora en móviles, tablets y PCs.

Criterios de Aceptación

 Botones accesibles en pantalla táctil.

 Contraste adecuado para visibilidad.

 Navegación por teclado y compatibilidad con lectores de pantalla.

Notas Técnicas

Aplicar estándares de accesibilidad (WCAG 2.1).

Framework sugerido: React con Tailwind para adaptabilidad.

🧠 Consideraciones del Análisis Sistémico
Subsistemas involucrados:

Subsistema	Descripción
Parser matemático	Interpretación de expresiones complejas
Motor de cálculo	Operaciones básicas, científicas, manejo de errores
UI/UX responsiva	Interfaz accesible en cualquier dispositivo
Persistencia local	Historial, configuración del modo (grados/radianes, notación científica)
Internacionalización (opcional)	Soporte multilenguaje, símbolos decimales y separadores

CHAT DE LAS HISTORIAS DE USUARIO CON CHATGPT= https://chatgpt.com/share/685c736d-5e4c-8003-98ea-fa6338a50087

CHAT DE LA ISSUE DE VICENTE YBALO= https://chatgpt.com/share/684a1780-0a98-8003-a813-3a867b5e661e
CHAT DE LA ISSUE DE FACUNDO CASTILLO= https://chatgpt.com/share/684a16c9-39b4-8009-b1eb-8849fb5a2996
CHAT DE LA ISSUE DE LAUTARO GUTIERREZ LARDIT: https://chatgpt.com/c/6852c92b-1320-800c-8b52-3462e6896670
CHAT DE LA ISSUE DE OVIEDO ALEJO : https://chatgpt.com/share/685c7b8f-7db8-8012-a66f-a03098d14854
