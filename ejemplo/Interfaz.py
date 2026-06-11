#Estas fueron algunas cosas que utilize para el diseño de la interfaz

window = tkinter.Tk()
window.title("Calculadora")

label = tkinter.Label(frame, text="0", font=("Arial",45), ...)

for row in range(row_count):
    for column in range(column_count):
        button = tkinter.Button(frame, text=value, ...)
        button.grid(row=row+1, column=column, padx=3, pady=3)

#Características:

#ventana:  no es redimensonable 

#pantalla: Utilize label de 45px, con fondo azul oscuro, texto alineado a la derecha

#Botones:  en total son 20 botones (5filas x 4 columnas),y de fuente es:Segoe UI

#Colores de pendiendo del boton:  Botones superiores(morado), operadores(naranja/verde), numeros(gris)

#Venta del historila: Toplevel flotante con caja de texto para las operaciones 

