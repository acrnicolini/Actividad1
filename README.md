# Sistema de Evaluación para la Feria de Ciencias
Este programa permite llevar un registro y calcular los puntajes de los equipos que participan en el evento a lo largo de varias rondas.

## ¿Qué hace este programa?
El programa main.ipynb utiliza las funciones definidas en el módulo evaluacion.py para simular un proceso de evaluación. En este caso son cinco equipos de la A a la E que participan en cindo rondas.Por cada una de ellas, calcula los puntajes de cada equipo basándose en tres criterios:
- Innovación: Cada punto en esta categoría vale 3 puntos en el total.
- Presentación: Cada punto en esta categoría vale 1 punto en el total.
- Errores: Si un equipo comete un error grave (True), se le resta 1 punto del total.
Además, el programa muestra al equipo con el puntaje más alto en cada ronda en "Mejor Equipo de la Ronda". 
Al final, muestra un ranking actualizado después de cada ronda y un ranking final con los resultados acumulados.

## Requisitos y Dependencias
Para poder ejecutar este programa, es necesario tener instalados Python version 3 y Jupyter Noteboks. 
El programa utiliza módulos standard de Python, como os y sys, no se requiere de instalación de librerías adicionales.

## Estructura de los Archivos
Para que el programa funcione correctamente, tus archivos deben estar organizados de la siguiente manera:
""".
├── src/
│   └── evaluacion.py
└── notebooks/
    └── main.ipynb
└── README.md
    """
•	notebooks/main.ipynb: ejecuta la lógica del programa.
•	src/evaluacion.py: contiene todas las funciones que realizan los cálculos y la lógica de evaluación.

## Cómo Usar el Programa
Para ver los resultados de la simulación:
1.	los archivos deben estar en la estructura de carpetas correcta, tal como se muestra arriba.
2.	Abrir el archivo main.ipynb en un entorno que pueda ejecutar Jupyter (como Jupyter Notebook)
3.	Ejecutar cada línea del código.
Una vez ejecutado el programa, se mostrarán los resultados detallados para cada ronda de la competencia, incluyendo:
•	La ronda que se está evauando
•	El "Mejor Equipo de la Ronda" y su puntaje.
•	Un ranking actualizado que muestra los puntajes acumulados de todos los equipos.
Si se desea cambiar los datos de la evaluación, se puede modificar la lista de diccionarios llamada evaluaciones en el archivo main.ipynb para simular nuevos escenarios.
