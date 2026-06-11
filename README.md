# proyecto final

¿ Qué hace el programa?

1.Operaciones básicas: Permite realizar sumas (+), restas (-), multiplicaciones (×) y divisiones (÷) con números enteros y decimales.

2. Interfaz adaptable: Tiene un diseño ordenado en una cuadrícula de botones con diferentes colores según su función para que sea intuitiva. Además, la ventana se centra automáticamente en la pantalla al abrirse.

3.Control de encendido/apagado: Cuenta con un botón ON/OFF que simula apagar la pantalla y bloquea las funciones si está apagada.

4. Historial de operaciones: Incluye un botón HIST que abre una ventana secundaria flotante donde se van guardando y mostrando todas las operaciones que se han hecho en la sesión.

   
¿ Qué partes del código implementaste tú?

1. Diseño de la interfaz y matriz de botones: Creé la estructura de la cuadrícula usando una lista de listas (button_values) para organizar las filas y columnas, y asigné colores personalizados a cada tipo de botón (operadores, números y funciones especiales).

2.Lógica de los estados (Variables globales): Configuré variables para controlar la lógica del programa, como guardar el primer número, el operador seleccionado, el estado de encendido (calculadora_encendida) y la lista para almacenar el historial.

3.La función principal de los clics (button_clicked): Programé el comportamiento de cada botón. Por ejemplo, la lógica de las condiciones (if/elif) para decidir qué pasa si se presiona un número, un operador, el borrador (⌫), o el botón de limpiar (AC).

4.Validaciones especiales: Implementé las condiciones para que no se divida entre cero y la lógica de texto con recortes (texto[:-1]) para que el botón de borrar elimine solo el último carácter de la pantalla.

5.Ventana de historial: Programé la función mostrar_el_historial para que cree una ventana nueva (Toplevel) y use un ciclo para mostrar la lista de operaciones guardadas o un aviso si aún está vacía.


¿ Qué aprendiste durante el desarrollo?

Uso de interfaces gráficas con Tkinter: Aprendí a crear ventanas, usar contenedores (Frame), etiquetas de texto (Label) y botones, además de cómo acomodarlos de forma ordenada usando el sistema de cuadrícula (grid).

Manejo de eventos y funciones Lambda: Entendí cómo pasarle datos dinámicos a una función cuando se presiona un botón específico en un ciclo, usando command=lambda v=value: button_clicked(v).

Conversión y manipulación de tipos de datos: Reforcé cómo cambian los tipos de datos al capturar texto de la pantalla, convertirlo a número (float) para hacer la operación matemática, y luego regresarlo a texto (str) para mostrar el resultado.

Manejo de ventanas secundarias y listas: Aprendí a usar la función Toplevel para abrir más de una ventana en una misma aplicación y a usar listas dinámicas (.append()) para almacenar datos en un historial.




