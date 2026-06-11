# EL proceso que yo hice fue el siguiente:

#Paso 1: La matriz de botones

button_values = [
    ["ON/OFF", "AC", "⌫", "÷"], 
    ["7", "8", "9", "×"], 
]
# esto sirve para tener una forma sencilla de modificar la disposicion sin tocar el otras partes del codigo

# Paso 2: Clasificación de botones

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["ON/OFF", "AC", "HIST","⌫"]

#Esto funciona para que tengan colores diferentes dependidendo la funcion

#Paso 3: Variables de estado

numero_1 = "0"
operador = None
numero_2 = None
calculadora_encendida = True
historial = []

# esta parde sirve para recordar el primer numero, la operacion que se aplica y el historial mientras el usuario interactua


#Paso 4: La lógica principal button_clicked()

#ON/OFF: Apagar/encender la calculadora

#HIST: Mostrar ventana de historial

#AC: Limpiar todo

#⌫: Borrar el último carácter

#Operadores (+,-,×,÷,=) - La lógica matemática

#Números y punto decimal - Construir el número actual


#Paso 5: La interfaz gráfica
#Crea: la ventana con tkinter.Tk()

#Añadi el Label: para la pantalla

#Genere los botones con un doble for loop

#Aplicar colores según la clasificación

