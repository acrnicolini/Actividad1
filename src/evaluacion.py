# Función para calcular el puntaje de un solo equipo
def calcular_puntaje(evaluacion):
    """
    Calcula el puntaje de un equipo en una ronda.
    """
    puntos_innovacion = evaluacion['innovacion'] * 3
    puntos_presentacion = evaluacion['presentacion'] * 1
    puntos_errores = -1 if evaluacion['errores'] else 0 # Resta si errores es true
    return puntos_innovacion + puntos_presentacion + puntos_errores

# Procesa una ronda y calcula  MER
def procesar_ronda(ronda, acumulados):
    """_summary_procesa una ronda de evaluacion, actualiza acumulados e infroma
    el mejor equipo de la ronda y el equipo con mas errores graves

    Args:
        ronda (_type_diccionario): diccionario anidado, es un diccionario cuya 
        key es el equipo y value un diccionario con los items a evaluar
        acumulados (_type_diccionario): acumula los valores de cada ronda

    Returns:
        tupla: con el nombre del mejor equipo y su puntaje
    """
   
    puntajes_ronda = dict(zip(ronda.keys(), map(calcular_puntaje, ronda.values())))
    """Itera sobre los equipos de cada ronda para aplicar calcular_puntaje
        ronda.values: accede a los valores del diccionario ronda
        maps: aplica a todos los valores del diccionario  la formula
        calcular_puntaje.
        ronda.keys:accede a las claves de ronda.
        zip: combina el nombre del equipo con su puntaje
        puntajes_ronda: devuelve un diccionario de equipos y sus puntajes
    
    """
    # Actualiza acumulados
   
    for equipo, evaluacion in ronda.items():
        acumulados[equipo]['innovacion'] += evaluacion['innovacion']*3
        acumulados[equipo]['presentacion'] += evaluacion['presentacion']*1
        acumulados[equipo]['errores'] += 1 if evaluacion['errores'] else 0
        acumulados[equipo]['puntos_total'] += puntajes_ronda[equipo]
        
    # Maximo con puntaje alto
    mejor_equipo_ronda = max(puntajes_ronda, key=puntajes_ronda.get)
    mejor_puntaje_ronda = puntajes_ronda[mejor_equipo_ronda]
    acumulados[mejor_equipo_ronda]['mejores_equipos'] += 1
    
    # 
    equipos_con_errores = list(filter(lambda e: ronda[e]['errores'], ronda.keys()))
    print(f"Equipos con errores graves en esta ronda: {equipos_con_errores}")

    return (mejor_equipo_ronda, mejor_puntaje_ronda)

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
        key=lambda item: item[1]['puntos_total'],
        reverse=True
    )
    print("--- Ranking Actualizado ---")
    print(f"{'Equipo':<10}{'Innovación':<15}{'Presentación':<15}{'Errores':<10}
          {'Mejores Equipos':<20}{'Puntos Total':<15}")
    for equipo, datos in equipos_ordenados:
        print(f"{equipo:<10}{datos['innovacion']:<15}{datos['presentacion']:<15}
              {datos['errores']:<10}{datos['mejores_equipos']:<20}{datos['puntos_total']:<15}")
    print("\n" + "="*80 + "\n")
    
    
