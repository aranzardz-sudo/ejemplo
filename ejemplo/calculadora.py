import tkinter 

#Configuracion de los botones que van ir en la cuadricula de la interfaz

button_values = [
    ["ON/OFF", "AC", "⌫", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "HIST", "="]
]

# Estas listas son para identificar que tipo de boton es y poner diseños diferentes

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["ON/OFF", "AC", "HIST","⌫"]

# Esto guarda el tamaño de la matriz

row_count = len(button_values) 
column_count = len(button_values[0]) 

# Estos son los colores, para que se vea mejor la interfaz y no se vea todo parejo

colors = {
    "morado": "#B79DCE",
    "negro": "#455F76",
    "gris": "#B7DBF2",
    "naranja": "#B7E4C7",
    "blanco": "#355070"    
}



#                                                                         VARIABLES
# Aqui guardo los estados y los numeros para las operaciones 

numero_1="0"
operador=None
numero_2=None
calculadora_encendida = True
historial=[]


#                                                                          FUNCIONES

# Esta funcion sirve para reiniciar los valores de la operacion que se hace en ese momento

def limpiar():
    global numero_1, numero_2, operador

    numero_1="0"
    numero_2=None
    operador=None
    
#ESta funcion sirve para quitar el numero decimal de algun resultado con .0 y solo salga un numero entero

def eliminar_cero_con_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)

# Esto crea una ventana secundaria flotante para mostrar todas las operaciones que se han hecho

def mostrar_el_historial():
    ventana_de_historial= tkinter.Toplevel(window)
    ventana_de_historial.title("Historial")

# Caja de texto para meter los datos del historial

    texto = tkinter.Text(ventana_de_historial, width=30, height=10)
    texto.pack()

# Si no han hecho operaciones, muestra un aviso de que NO hay operaciones y si si hay pues la muestra

    if len(historial)==0:
        texto.insert(tkinter.END, "No hay operaciones")
    else:
        for operacion in historial:
            texto.insert(tkinter.END, operacion + "\n")

#ESto es muy importante por que procesa el clic de cualquier boton

def button_clicked(value):

    global numero_1, numero_2, operador
    global calculadora_encendida

    #                                                                        ON/OFF
    if value == "ON/OFF":

        if calculadora_encendida:
            label["text"]=""            # Borra la pantalla simulando que se apaga 
            calculadora_encendida = False
        else:
            label["text"] ="0"         # Muestra el cero al inicio al encender
            calculadora_encendida = True
        
        return

# si la calculadora esta apagada, ignora por completo cualquier otro boton

    if not calculadora_encendida:
        return
    
    #                                                                        HISTORIAL

    if value=="HIST":
        mostrar_el_historial()
        return
    
    #                                                                        BOTON AC
    if value=="AC":
        limpiar()
        label["text"] = "0"
        return
    
    #                                                                  BORRADOR DE NUMEROS
    if value=="⌫":

        if label["text"]=="Error":
            label["text"]= "0"
            return
        texto=label["text"]
# Si hay mas de un numero  borra el ultimo
        if len(texto)>1:
            label["text"] = texto[:-1]
        else:
            label["text"] = "0"
        return
        
        
    #                                                                    OPERADORES

    if value in right_symbols:
#si presionan igual, hace las operaaciones matematicas
        if value == "=":
             if operador is not None:
                 
                 numero_2=label ["text"]
# convierte a float para poder manejar decimales sin problemas
                 primer_numero=float(numero_1)
                 segundo_numero=float(numero_2)

                 if operador == "+":
                     resultado=eliminar_cero_con_decimal(primer_numero + segundo_numero)
                 elif operador== "-":
                     resultado=eliminar_cero_con_decimal(primer_numero - segundo_numero)
                 elif  operador== "×":
                     resultado=eliminar_cero_con_decimal(primer_numero * segundo_numero)
                 elif operador== "÷":
# esto sirve para que si se divide entre cero no falle el programa
                     if segundo_numero== 0:
                         label["text"] = "Error"
                         limpiar()
                         return   
                     resultado=eliminar_cero_con_decimal(primer_numero / segundo_numero)
                 label["text"]=resultado 

                 historial.append(
                     f"{numero_1} {operador} {numero_2} = {resultado}"
                 )

                 limpiar()
        else:       # si presionan +,-,x o / se guarda el primer numero
          if operador is None:
              numero_1= label ["text"]
              label["text"] = "0"
              operador = value
          
           
        
        return
             
    #                                                                      NUMEROS Y DECIMAL 
    
    
    if value == ".":
# Evita que pongan mas de un punto decimal en el mismo numero
        if "." not in label ["text"]:
            label["text"] += "."
    
    elif value in "0123456789":
# si hay un "0", se remplaza por el numero presionado
        if label["text"] == "0":
            label["text"] = value
        
        else:
            label["text"] += value


#                                                                          VENTANA

window = tkinter.Tk() #create the window
window.title("Calculadora")
window.resizable(False, False)

frame= tkinter.Frame(window)
label= tkinter.Label(        # en esta pantalla se muestran los numeros
    frame,
    text="0",
    font=("Arial",45),
    background=colors["negro"],
    foreground=colors["blanco"],
    anchor="e",
    width=column_count
)

label.grid(row=0, column=0, columnspan=column_count, sticky="we")
# se anidan los bucles para la cuadricula de botones 
for row in range(row_count):
    for column in range(column_count):

        value=button_values[row][column]
       
        button=tkinter.Button(
            frame,
            text=value,
            font=("segoe UI",18,"bold"),
            width=6,
            height=2,
            relief="flat",
            borderwidth=0,
            command=lambda v=value: button_clicked(v) # Lambda guarda el valor del boton para enviarlo a la funcion button_clicked 
        )
        
        #                                                                    COLORES
        #se ponen de color los botones dependiendo del tipo de boton para que se vea un poco mejor
        if value in top_symbols:
            button.config(
                foreground=colors["negro"],
                background=colors["morado"]
            )
        elif value in right_symbols:
             button.config(
                  foreground=colors["blanco"],
                  background=colors["naranja"]
             )
           

        else:
            button.config(
                foreground=colors["blanco"],
                background=colors["gris"]
            )
        
        button.grid(
            row=row + 1,
            column=column,
            padx=3,
            pady=3
        )


frame.pack()


#                                          CENTRAR VENTANA EN LA PANTALLA
#centra la pantalla al abrirse 
window.update() 
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

window_x=int((screen_width/2) - (window_width/2))
window_y=int((screen_height/2) - (window_height/2))


window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()
