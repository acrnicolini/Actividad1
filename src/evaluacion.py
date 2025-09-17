innovacion = 3
presentacion = 1
errores = -1

# Función para calcular el puntaje de un solo equipo
def calcular_puntaje(evaluacion):
    """
    Calcula el puntaje de un equipo en una ronda, para cada concepto y total.
    
    Returns:
        diccionario con los puntos obtenidos en cada categoria y totales.
    """
    puntos_innovacion = evaluacion['innovacion'] * innovacion
    puntos_presentacion = evaluacion['presentacion'] * presentacion
    puntos_errores = errores if evaluacion['errores'] else 0 # Resta si errores es true
    puntos_totales = puntos_presentacion + puntos_innovacion + puntos_errores
    return {
             'innovacion': puntos_innovacion,
             'presentacion': puntos_presentacion,
             'errores': puntos_errores,
             'puntos_totales': puntos_totales
            }
             

# Procesa una ronda y calcula  MER
def procesar_ronda(ronda, acumulados):
    """Procesa una ronda de evaluacion, actualiza acumulados e infroma
    el mejor equipo de la ronda

    Args:
        ronda (diccionario): diccionario anidado, es un diccionario cuya 
        key es el equipo y value un diccionario con los items a evaluar
        acumulados (diccionario): acumula los valores de cada ronda

    Returns:
        tupla: con el nombre del mejor equipo y su puntaje
    """
    # Aplica calcular_puntaje a todos los equipos de la ronda
    puntos_equipo = list(map(calcular_puntaje, ronda.values()))
    
    #Machtea equipo con datos de puntaje respectivos
    datos_equipos = list(zip(ronda.keys(),puntos_equipo))
    
    #crea diccionario con puntajes por ronda
    puntajes_ronda = {}
   
    for equipo, puntos_desglose in datos_equipos:
        puntajes_ronda[equipo] = puntos_desglose['puntos_totales']
        
        acumulados[equipo]['innovacion'] += puntos_desglose['innovacion']
        acumulados[equipo]['presentacion'] += puntos_desglose['presentacion']
        acumulados[equipo]['errores'] += puntos_desglose['errores']
        acumulados[equipo]['puntos_totales'] += puntos_desglose['puntos_totales']
                
    # Maximo con puntaje alto
    mejor_equipo_ronda = max(puntajes_ronda, key=puntajes_ronda.get)
    mejor_puntaje_ronda = puntajes_ronda[mejor_equipo_ronda]
    acumulados[mejor_equipo_ronda]['mejores_equipos'] += 1
    
    return (mejor_equipo_ronda, mejor_puntaje_ronda)

#Busca los gandores finales
def encontrar_ganadores(acumulados):
    """
    Muestra el o los equipos ganadores una vez finalizadas todas las rondas.
    
    Returns:
        una lista con los nombres de los equipos ganadores.
    """
    puntaje_maximo = max(equipo['puntos_totales'] for equipo in acumulados.values())
    ganadores = [equipo for equipo, datos in acumulados.items() if datos['puntos_totales'] == puntaje_maximo]
    return ganadores

# Muestra el ranking
def mostrar_ranking(acumulados):
    """Muestra el ranking de los equipos.
        Args:
            acumulados (diccionario): es un diccionario con los equipos y el puntaje obtenido
            en las distintas rondas.
        Return:
            imprime una tabla a partir de una lista detuplas con los equipos ordenados de 
            mayor a menor por puntaje total  
    """
     
    equipos_ordenados = sorted(
        acumulados.items(),
        key=lambda item: item[1]['puntos_totales'],
        reverse=True
    )
    
    print("--- Ranking Actualizado ---")
    print(
        f"{'Equipo':<10}{'Innovación':<15}{'Presentación':<15}{'Errores':<10}"
        f"{'Mejores Equipos':<20}{'Puntos Totales':<15}"
    )
    for equipo, datos in equipos_ordenados:
        print(
            f"{equipo:<10}{datos['innovacion']:<15}{datos['presentacion']:<15}"
            f"{datos['errores']:<10}{datos['mejores_equipos']:<20}"
            f"{datos['puntos_totales']:<15}"
        )
    print("\n" + "="*80 + "\n")
    
    
