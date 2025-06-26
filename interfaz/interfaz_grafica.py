import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog, Menu
import numpy as np
from operaciones.operacionesBasicas import calcular_expresion
from operaciones.funciones_avanzadas import resolver_sistema_ecuaciones, operaciones_matriciales, calculos_estadisticos, calculos_base
from historial.func_historial import guardar_operacion, cargar_historial, limpiar_historial, exportar_pdf

def mostrar_resultado_cli(expresion, resultado):
    """Muestra el resultado en la consola"""
    print(f"Expresión: {expresion}")
    print(f"Resultado: {resultado}")

def limpiar_entrada(expresion_var):
    """Borra completamente el contenido del campo de entrada"""
    expresion_var.set("")

def agregar_a_entrada(texto, expresion_var):
    """Agrega texto al campo de entrada o ejecuta acción especial"""
    if texto == '=':
        return
    elif texto == 'C':
        # Borra el último carácter (Backspace)
        current = expresion_var.get()
        expresion_var.set(current[:-1])
    else:
        expresion_var.set(expresion_var.get() + texto)

def calcular(expresion_var, resultado_var, modo_angulo, historial_text):
    """Realiza el cálculo y muestra el resultado"""
    expresion = expresion_var.get()
    if not expresion:
        return
    
    try:
        # Agregar prefijo para modo grados si es necesario
        if modo_angulo.get() == "grados":
            expresion = expresion.replace("sin(", "sind(")
            expresion = expresion.replace("cos(", "cosd(")
            expresion = expresion.replace("tan(", "tand(")
        
        resultado = calcular_expresion(expresion)
        resultado_var.set(str(resultado))
        guardar_operacion(expresion, resultado)
        actualizar_historial(historial_text)
    except Exception as e:
        messagebox.showerror("Error", f"Error en el cálculo: {str(e)}")

def actualizar_historial(historial_text):
    """Actualiza el widget de historial con las operaciones recientes"""
    historial = cargar_historial()
    historial_text.delete(1.0, tk.END)
    
    for op in historial:
        texto = f"{op['fecha']}: {op['expresion']} = {op['resultado']}\n"
        historial_text.insert(tk.END, texto)

def limpiar_historial_gui(historial_text):
    """Limpia el historial desde la GUI"""
    if limpiar_historial():
        actualizar_historial(historial_text)
        messagebox.showinfo("Historial", "Historial borrado correctamente")
    else:
        messagebox.showinfo("Historial", "El historial ya estaba vacío")

def exportar_pdf_gui():
    """Exporta el historial a PDF a través de diálogo de archivos"""
    ruta_archivo = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
    )
    if ruta_archivo:
        if exportar_pdf(ruta_archivo):
            messagebox.showinfo("Éxito", "Historial exportado correctamente a PDF.")
        else:
            messagebox.showerror("Error", "No se pudo exportar el historial")

def iniciar_interfaz_grafica():
    """Inicia la interfaz gráfica de la calculadora"""
    root = tk.Tk()
    root.title("PyCalc - Calculadora Científica")
    root.state('zoomed')  # Abrir en pantalla completa
    
    # Variables
    expresion_var = tk.StringVar()
    resultado_var = tk.StringVar()
    modo_angulo = tk.StringVar(value="radianes")
    
    # Menú superior
    menu_bar = Menu(root)
    root.config(menu=menu_bar)
    
    # Menú Operaciones
    operaciones_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Operaciones", menu=operaciones_menu)
    operaciones_menu.add_command(label="Sistema de ecuaciones", command=lambda: mostrar_dialogo_avanzado(root, 0))
    operaciones_menu.add_command(label="Matrices", command=lambda: mostrar_dialogo_avanzado(root, 2))
    operaciones_menu.add_command(label="Estadística", command=lambda: mostrar_dialogo_avanzado(root, 3))
    operaciones_menu.add_command(label="Bases numéricas", command=lambda: mostrar_dialogo_avanzado(root, 4))
    operaciones_menu.add_separator()
    operaciones_menu.add_command(label="Fracciones", command=lambda: agregar_a_entrada('frac()', expresion_var))
    
    # Menú Funciones
    funciones_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Funciones", menu=funciones_menu)
    funciones_menu.add_command(label="Hiperbólicas", command=lambda: mostrar_dialogo_hiperbolicas(root, expresion_var))
    funciones_menu.add_command(label="Probabilidad", command=lambda: mostrar_dialogo_probabilidad(root, expresion_var))
    funciones_menu.add_command(label="Constantes", command=lambda: mostrar_dialogo_constantes(root, expresion_var))
    
    # Frame principal
    main_frame = ttk.Frame(root, padding="20")
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Pantalla de entrada y resultado
    entrada_frame = ttk.Frame(main_frame)
    entrada_frame.pack(fill=tk.X, pady=10)
    
    ttk.Label(entrada_frame, text="Expresión:", font=('Arial', 12)).pack(anchor=tk.W)
    entrada = ttk.Entry(entrada_frame, textvariable=expresion_var, font=('Arial', 16))
    entrada.pack(fill=tk.X, pady=5)
    entrada.focus()
    
    ttk.Label(entrada_frame, text="Resultado:", font=('Arial', 12)).pack(anchor=tk.W)
    resultado_label = ttk.Label(entrada_frame, textvariable=resultado_var, font=('Arial', 16), 
                              background="#f0f0f0", anchor=tk.E, relief="sunken", padding=10)
    resultado_label.pack(fill=tk.X, pady=5)
    
    # Botones básicos
    botones_frame = ttk.Frame(main_frame)
    botones_frame.pack(fill=tk.BOTH, expand=True, pady=10)
    
    # Configurar grid
    botones_frame.columnconfigure(0, weight=1)
    botones_frame.columnconfigure(1, weight=1)
    botones_frame.columnconfigure(2, weight=1)
    botones_frame.columnconfigure(3, weight=1)
    botones_frame.columnconfigure(4, weight=1)
    botones_frame.rowconfigure(0, weight=1)
    botones_frame.rowconfigure(1, weight=1)
    botones_frame.rowconfigure(2, weight=1)
    botones_frame.rowconfigure(3, weight=1)
    
    botones_basicos = [
        '7', '8', '9', '/', 'sin(',
        '4', '5', '6', '*', 'cos(',
        '1', '2', '3', '-', 'tan(',
        '0', '.', '(', ')', 'log('
    ]
    
    for i, texto in enumerate(botones_basicos):
        row = i // 5
        col = i % 5
        btn = ttk.Button(botones_frame, text=texto, 
                        command=lambda t=texto: agregar_a_entrada(t, expresion_var))
        btn.grid(row=row, column=col, sticky=tk.NSEW, padx=5, pady=5)
    
    # Botones operadores
    operadores_frame = ttk.Frame(main_frame)
    operadores_frame.pack(fill=tk.X, pady=10)
    
    operadores = ['+', '-', '*', '/', '=']
    for i, op in enumerate(operadores):
        if op == '=':
            btn = ttk.Button(operadores_frame, text=op, width=5,
                           command=lambda: calcular(expresion_var, resultado_var, modo_angulo, historial_text),
                           style='Accent.TButton')
        else:
            btn = ttk.Button(operadores_frame, text=op, width=5,
                           command=lambda t=op: agregar_a_entrada(t, expresion_var))
        btn.pack(side=tk.LEFT, padx=5)
    
    # Botones especiales
    botones_especiales_frame = ttk.Frame(main_frame)
    botones_especiales_frame.pack(fill=tk.X, pady=10)
    
    especiales = ['CE', 'C', '^', 'π', 'e', 'ln(', '∫', 'd/dx', 'simplify', 'solve(', 'frac(']
    
    for i, texto in enumerate(especiales):
        if texto == 'CE':
            btn = ttk.Button(botones_especiales_frame, text=texto, 
                           command=lambda: limpiar_entrada(expresion_var))
        elif texto == '∫':
            btn = ttk.Button(botones_especiales_frame, text=texto,
                           command=lambda: mostrar_dialogo_integral(root, expresion_var))
        else:
            btn = ttk.Button(botones_especiales_frame, text=texto, 
                           command=lambda t=texto: agregar_a_entrada(t, expresion_var))
        btn.pack(side=tk.LEFT, padx=5, expand=True)
    
    # Configuración
    config_frame = ttk.Frame(main_frame)
    config_frame.pack(fill=tk.X, pady=10)
    
    ttk.Radiobutton(config_frame, text="Radianes", variable=modo_angulo, 
                   value="radianes").pack(side=tk.LEFT, padx=10)
    ttk.Radiobutton(config_frame, text="Grados", variable=modo_angulo, 
                   value="grados").pack(side=tk.LEFT, padx=10)
    
    # Historial
    historial_frame = ttk.LabelFrame(main_frame, text="Historial", padding=10)
    historial_frame.pack(fill=tk.BOTH, expand=True)
    
    # Botones de gestión de historial
    historial_btns_frame = ttk.Frame(historial_frame)
    historial_btns_frame.pack(fill=tk.X, pady=5)
    
    btn_limpiar = ttk.Button(historial_btns_frame, text="Limpiar Historial",
                            command=lambda: limpiar_historial_gui(historial_text))
    btn_limpiar.pack(side=tk.LEFT, padx=5)
    
    btn_exportar = ttk.Button(historial_btns_frame, text="Exportar a PDF",
                            command=exportar_pdf_gui)
    btn_exportar.pack(side=tk.LEFT, padx=5)
    
    historial_text = scrolledtext.ScrolledText(historial_frame, height=10, state="normal", font=('Arial', 10))
    historial_text.pack(fill=tk.BOTH, expand=True)
    actualizar_historial(historial_text)
    
    # Eventos de teclado
    entrada.bind('<Return>', lambda e: calcular(expresion_var, resultado_var, modo_angulo, historial_text))
    entrada.bind('<KP_Enter>', lambda e: calcular(expresion_var, resultado_var, modo_angulo, historial_text))
    entrada.bind('<Escape>', lambda e: limpiar_entrada(expresion_var))
    
    # Estilo para botón de calcular
    style = ttk.Style()
    style.configure('Accent.TButton', font=('Arial', 12, 'bold'), foreground='blue')
    
    # ===== DIÁLOGOS =====
    
    def mostrar_dialogo_integral(parent, exp_var):
        dialog = tk.Toplevel(parent)
        dialog.title("Integral")
        dialog.geometry("400x300")
        dialog.transient(parent)
        dialog.grab_set()
        
        ttk.Label(dialog, text="Expresión:", font=('Arial', 10)).pack(padx=10, pady=5, anchor=tk.W)
        expr_entry = ttk.Entry(dialog, font=('Arial', 12))
        expr_entry.pack(fill=tk.X, padx=10, pady=5)
        expr_entry.insert(0, exp_var.get())
        expr_entry.focus()
        
        ttk.Label(dialog, text="Variable:", font=('Arial', 10)).pack(padx=10, pady=5, anchor=tk.W)
        var_entry = ttk.Entry(dialog, font=('Arial', 12), width=10)
        var_entry.pack(padx=10, pady=5, anchor=tk.W)
        var_entry.insert(0, "x")
        
        # Checkbox para tipo de integral
        integral_type = tk.StringVar(value="definida")
        ttk.Checkbutton(dialog, text="Integral Definida", 
                       variable=integral_type, onvalue="definida", offvalue="indefinida").pack(anchor=tk.W, padx=10, pady=5)
        
        limits_frame = ttk.Frame(dialog)
        limits_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(limits_frame, text="Límite inferior:", font=('Arial', 10)).pack(side=tk.LEFT, padx=(0, 5))
        lower_entry = ttk.Entry(limits_frame, font=('Arial', 12), width=10)
        lower_entry.pack(side=tk.LEFT)
        lower_entry.insert(0, "0")
        
        ttk.Label(limits_frame, text="Límite superior:", font=('Arial', 10)).pack(side=tk.LEFT, padx=(10, 5))
        upper_entry = ttk.Entry(limits_frame, font=('Arial', 12), width=10)
        upper_entry.pack(side=tk.LEFT)
        upper_entry.insert(0, "1")
        
        def aplicar_integral():
            expr = expr_entry.get()
            var = var_entry.get()
            tipo = integral_type.get()
            
            if tipo == "definida":
                lower = lower_entry.get()
                upper = upper_entry.get()
                
                if not expr or not var or not lower or not upper:
                    messagebox.showerror("Error", "Todos los campos son obligatorios")
                    return
                    
                try:
                    float(lower)
                    float(upper)
                except ValueError:
                    messagebox.showerror("Error", "Los límites deben ser números válidos")
                    return
                    
                exp_var.set(f"∫({expr},{var},{lower},{upper})")
            else:
                if not expr or not var:
                    messagebox.showerror("Error", "Expresión y variable son obligatorias")
                    return
                    
                exp_var.set(f"∫({expr},{var})")
            
            dialog.destroy()
        
        btn_frame = ttk.Frame(dialog)
        btn_frame.pack(pady=10)
        
        ttk.Button(btn_frame, text="Cancelar", command=dialog.destroy).pack(side=tk.LEFT, padx=10)
        ttk.Button(btn_frame, text="Aplicar", command=aplicar_integral, style='Accent.TButton').pack(side=tk.LEFT, padx=10)
    
    def mostrar_dialogo_avanzado(parent, tab_index=0):
        dialog = tk.Toplevel(parent)
        dialog.title("Operaciones Avanzadas")
        dialog.geometry("600x500")
        dialog.transient(parent)
        dialog.grab_set()
        
        notebook = ttk.Notebook(dialog)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Pestaña para 2 ecuaciones
        frame2 = ttk.Frame(notebook)
        notebook.add(frame2, text="2 Ecuaciones")
        
        ttk.Label(frame2, text="Ecuación 1:").grid(row=0, column=0, padx=5, pady=5)
        eq1_var = tk.StringVar()
        ttk.Entry(frame2, textvariable=eq1_var, width=25).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame2, text="Ecuación 2:").grid(row=1, column=0, padx=5, pady=5)
        eq2_var = tk.StringVar()
        ttk.Entry(frame2, textvariable=eq2_var, width=25).grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(frame2, text="Variables (ej: x,y):").grid(row=2, column=0, padx=5, pady=5)
        vars_var = tk.StringVar(value="x,y")
        ttk.Entry(frame2, textvariable=vars_var, width=10).grid(row=2, column=1, padx=5, pady=5)
        
        resultado_var = tk.StringVar()
        ttk.Label(frame2, textvariable=resultado_var, wraplength=400).grid(row=3, column=0, columnspan=2, pady=10)
        
        def resolver():
            try:
                ecuaciones = [eq1_var.get(), eq2_var.get()]
                variables = vars_var.get().split(',')
                solucion = resolver_sistema_ecuaciones(ecuaciones, variables)
                resultado_text = "\n".join([f"{var} = {val}" for var, val in solucion.items()])
                resultado_var.set(resultado_text)
                # Guardar en historial
                guardar_operacion(f"Sistema: {ecuaciones}", resultado_text)
                actualizar_historial(historial_text)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        ttk.Button(frame2, text="Resolver", command=resolver).grid(row=4, column=0, columnspan=2, pady=10)
        
        # Pestaña para 3 ecuaciones
        frame3 = ttk.Frame(notebook)
        notebook.add(frame3, text="3 Ecuaciones")
        
        ttk.Label(frame3, text="Ecuación 1:").grid(row=0, column=0, padx=5, pady=5)
        eq1_3_var = tk.StringVar()
        ttk.Entry(frame3, textvariable=eq1_3_var, width=25).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame3, text="Ecuación 2:").grid(row=1, column=0, padx=5, pady=5)
        eq2_3_var = tk.StringVar()
        ttk.Entry(frame3, textvariable=eq2_3_var, width=25).grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(frame3, text="Ecuación 3:").grid(row=2, column=0, padx=5, pady=5)
        eq3_3_var = tk.StringVar()
        ttk.Entry(frame3, textvariable=eq3_3_var, width=25).grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(frame3, text="Variables (ej: x,y,z):").grid(row=3, column=0, padx=5, pady=5)
        vars_3_var = tk.StringVar(value="x,y,z")
        ttk.Entry(frame3, textvariable=vars_3_var, width=10).grid(row=3, column=1, padx=5, pady=5)
        
        resultado_3_var = tk.StringVar()
        ttk.Label(frame3, textvariable=resultado_3_var, wraplength=400).grid(row=4, column=0, columnspan=2, pady=10)
        
        def resolver_3():
            try:
                ecuaciones = [eq1_3_var.get(), eq2_3_var.get(), eq3_3_var.get()]
                variables = vars_3_var.get().split(',')
                solucion = resolver_sistema_ecuaciones(ecuaciones, variables)
                resultado_text = "\n".join([f"{var} = {val}" for var, val in solucion.items()])
                resultado_3_var.set(resultado_text)
                # Guardar en historial
                guardar_operacion(f"Sistema: {ecuaciones}", resultado_text)
                actualizar_historial(historial_text)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        ttk.Button(frame3, text="Resolver", command=resolver_3).grid(row=5, column=0, columnspan=2, pady=10)
        
        # Pestaña para matrices
        frame_mat = ttk.Frame(notebook)
        notebook.add(frame_mat, text="Matrices")
        
        ttk.Label(frame_mat, text="Operación:").grid(row=0, column=0, padx=5, pady=5)
        op_mat_var = tk.StringVar()
        ttk.Combobox(frame_mat, textvariable=op_mat_var, values=['Determinante', 'Inversa', 'Suma', 'Multiplicación'], width=15).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame_mat, text="Matriz 1 (filas separadas por ;):").grid(row=1, column=0, padx=5, pady=5)
        mat1_text = scrolledtext.ScrolledText(frame_mat, height=5, width=30)
        mat1_text.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(frame_mat, text="Matriz 2 (solo para suma/multiplicación):").grid(row=2, column=0, padx=5, pady=5)
        mat2_text = scrolledtext.ScrolledText(frame_mat, height=5, width=30)
        mat2_text.grid(row=2, column=1, padx=5, pady=5)
        
        resultado_mat_var = tk.StringVar()
        ttk.Label(frame_mat, textvariable=resultado_mat_var, wraplength=400).grid(row=3, column=0, columnspan=2, pady=10)
        
        def resolver_mat():
            try:
                operacion = op_mat_var.get().lower()
                if not operacion:
                    messagebox.showerror("Error", "Seleccione una operación")
                    return
                    
                # Parsear matriz 1
                mat1_str = mat1_text.get("1.0", tk.END).strip()
                if not mat1_str:
                    messagebox.showerror("Error", "Matriz 1 es requerida")
                    return
                    
                filas1 = mat1_str.split(';')
                matriz1 = []
                for fila in filas1:
                    elementos = [float(x) for x in fila.split()]
                    matriz1.append(elementos)
                
                matriz1 = np.array(matriz1)
                matrices = [matriz1]
                
                # Parsear matriz 2 si es necesario
                if operacion in ['suma', 'multiplicación']:
                    mat2_str = mat2_text.get("1.0", tk.END).strip()
                    if not mat2_str:
                        messagebox.showerror("Error", "Matriz 2 es requerida para esta operación")
                        return
                        
                    filas2 = mat2_str.split(';')
                    matriz2 = []
                    for fila in filas2:
                        elementos = [float(x) for x in fila.split()]
                        matriz2.append(elementos)
                    
                    matriz2 = np.array(matriz2)
                    matrices.append(matriz2)
                
                # Mapear operaciones
                op_map = {
                    'determinante': 'det',
                    'inversa': 'inv',
                    'suma': 'add',
                    'multiplicación': 'mult'
                }
                
                resultado = operaciones_matriciales(matrices, op_map[operacion])
                resultado_mat_var.set(str(resultado))
                # Guardar en historial
                guardar_operacion(f"Matrices: {operacion}", str(resultado))
                actualizar_historial(historial_text)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        ttk.Button(frame_mat, text="Calcular", command=resolver_mat).grid(row=4, column=0, columnspan=2, pady=10)
        
        # Pestaña para estadística
        frame_est = ttk.Frame(notebook)
        notebook.add(frame_est, text="Estadística")
        
        ttk.Label(frame_est, text="Datos (separados por comas):").grid(row=0, column=0, padx=5, pady=5)
        datos_var = tk.StringVar()
        ttk.Entry(frame_est, textvariable=datos_var, width=30).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame_est, text="Operación:").grid(row=1, column=0, padx=5, pady=5)
        op_est_var = tk.StringVar()
        ttk.Combobox(frame_est, textvariable=op_est_var, values=['Media', 'Mediana', 'Desviación Estándar', 'Varianza', 'Regresión Lineal'], width=20).grid(row=1, column=1, padx=5, pady=5)
        
        resultado_est_var = tk.StringVar()
        ttk.Label(frame_est, textvariable=resultado_est_var, wraplength=400).grid(row=2, column=0, columnspan=2, pady=10)
        
        def calcular_est():
            try:
                datos_str = datos_var.get().strip()
                if not datos_str:
                    messagebox.showerror("Error", "Ingrese datos")
                    return
                    
                datos = [float(x) for x in datos_str.split(',')]
                operacion = op_est_var.get().lower()
                
                op_map = {
                    'media': 'media',
                    'mediana': 'mediana',
                    'desviación estándar': 'desv',
                    'varianza': 'var',
                    'regresión lineal': 'reg_lin'
                }
                
                resultado = calculos_estadisticos(datos, op_map[operacion])
                resultado_est_var.set(str(resultado))
                # Guardar en historial
                guardar_operacion(f"Estadística: {operacion}", str(resultado))
                actualizar_historial(historial_text)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        ttk.Button(frame_est, text="Calcular", command=calcular_est).grid(row=3, column=0, columnspan=2, pady=10)
        
        # Pestaña para bases numéricas
        frame_base = ttk.Frame(notebook)
        notebook.add(frame_base, text="Bases")
        
        ttk.Label(frame_base, text="Número:").grid(row=0, column=0, padx=5, pady=5)
        num_var = tk.StringVar()
        ttk.Entry(frame_base, textvariable=num_var, width=15).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame_base, text="Base entrada:").grid(row=1, column=0, padx=5, pady=5)
        base_in_var = tk.IntVar(value=10)
        ttk.Combobox(frame_base, textvariable=base_in_var, values=[2, 8, 10, 16], width=5).grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(frame_base, text="Base salida:").grid(row=2, column=0, padx=5, pady=5)
        base_out_var = tk.IntVar(value=10)
        ttk.Combobox(frame_base, textvariable=base_out_var, values=[2, 8, 10, 16], width=5).grid(row=2, column=1, padx=5, pady=5)
        
        resultado_base_var = tk.StringVar()
        ttk.Label(frame_base, textvariable=resultado_base_var, font=('Arial', 12)).grid(row=3, column=0, columnspan=2, pady=10)
        
        def convertir_base():
            try:
                numero = num_var.get()
                base_in = base_in_var.get()
                base_out = base_out_var.get()
                resultado = calculos_base(numero, base_in, base_out)
                resultado_base_var.set(f"Resultado: {resultado}")
                # Guardar en historial
                guardar_operacion(f"Bases: {numero} (base {base_in} a {base_out})", resultado)
                actualizar_historial(historial_text)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        
        ttk.Button(frame_base, text="Convertir", command=convertir_base).grid(row=4, column=0, columnspan=2, pady=10)
        
        # Seleccionar pestaña inicial
        notebook.select(tab_index)
    
    def mostrar_dialogo_hiperbolicas(parent, exp_var):
        dialog = tk.Toplevel(parent)
        dialog.title("Funciones Hiperbólicas")
        dialog.geometry("300x200")
        dialog.transient(parent)
        dialog.grab_set()
        
        funciones = [
            ("sinh", "sinh("),
            ("cosh", "cosh("),
            ("tanh", "tanh("),
            ("asinh", "asinh("),
            ("acosh", "acosh("),
            ("atanh", "atanh(")
        ]
        
        for i, (nombre, comando) in enumerate(funciones):
            btn = ttk.Button(dialog, text=nombre, width=10,
                           command=lambda c=comando: agregar_a_entrada(c, exp_var))
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    
    def mostrar_dialogo_probabilidad(parent, exp_var):
        dialog = tk.Toplevel(parent)
        dialog.title("Probabilidad")
        dialog.geometry("300x200")
        dialog.transient(parent)
        dialog.grab_set()
        
        funciones = [
            ("nPr", "nPr("),
            ("nCr", "nCr("),
            ("!", "factorial("),
            ("Rand", "rand("),
            ("Dist Normal", "normal_dist(")
        ]
        
        for i, (nombre, comando) in enumerate(funciones):
            btn = ttk.Button(dialog, text=nombre, width=10,
                           command=lambda c=comando: agregar_a_entrada(c, exp_var))
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    
    def mostrar_dialogo_constantes(parent, exp_var):
        dialog = tk.Toplevel(parent)
        dialog.title("Constantes")
        dialog.geometry("300x200")
        dialog.transient(parent)
        dialog.grab_set()
        
        constantes = [
            ("π", "π"),
            ("e", "e"),
            ("c (vel. luz)", "299792458"),
            ("G (gravitación)", "6.67430e-11"),
            ("h (Planck)", "6.62607015e-34")
        ]
        
        for i, (nombre, valor) in enumerate(constantes):
            btn = ttk.Button(dialog, text=nombre, width=10,
                           command=lambda v=valor: agregar_a_entrada(v, exp_var))
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    
    root.mainloop()