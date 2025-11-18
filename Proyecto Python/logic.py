import csv
import os

def new_logic():
    """
    Crea y retorna un nuevo catálogo vacío.

    Retorna:
        list: Lista vacía que servirá como estructura base del catálogo.
    """
    catalog = []
    return catalog


def carga_datos(catalog, filename):
    """
    Carga los datos desde un archivo CSV al catálogo.

    Parámetros:
        catalog (list): Lista donde se almacenarán los registros del archivo.
        filename (str): Nombre del archivo CSV dentro de la carpeta 'Data'.

    Retorna:
        list: Catálogo actualizado con los datos cargados.
    """
    # Construimos la ruta completa al archivo dentro de la carpeta 'Data'
    archivo = os.path.join("Data", filename)
    
    # Abrimos el archivo CSV y leemos su contenido
    with open(archivo, encoding="utf-8") as ruta:
        leer_archivo = csv.DictReader(ruta)  # Cada fila se lee como un diccionario
        for fila in leer_archivo:
            catalog.append(fila)  # Añadimos cada fila al catálogo
    
    return catalog


def best_shooters(catalog):
    """
    Determina el jugador con mayor cantidad de tiros acertados.

    Parámetros:
        catalog (list): Lista de diccionarios con los datos de tiros.

    Retorna:
        tuple: (nombre del mejor tirador, número de tiros acertados)
    """
    tirador = {}

    # Contamos los tiros acertados por jugador
    for jugador in catalog:
        if jugador["SHOT_RESULT"] != "missed":  # Solo consideramos los aciertos
            nombre = jugador["player_name"]
            tirador[nombre] = tirador.get(nombre, 0) + 1

    # Encontramos el jugador con más tiros acertados
    mejor_tirador = None
    mejor_contador = -1
    for nombre, cantidad in tirador.items():
        if cantidad > mejor_contador:
            mejor_tirador = nombre
            mejor_contador = cantidad
            
    return mejor_tirador, mejor_contador


def best_defender(catalog):
    """
    Determina el jugador defensor que ha provocado más tiros fallados.

    Parámetros:
        catalog (list): Lista de diccionarios con datos de tiros.

    Retorna:
        tuple: (nombre del mejor defensor, número de tiros defendidos)
    """
    defensor = {}

    # Contamos los tiros fallados (defendidos) por cada defensor
    for jugador in catalog:
        if jugador["SHOT_RESULT"] == "missed":
            nombre_defensor = jugador["CLOSEST_DEFENDER"]
            defensor[nombre_defensor] = defensor.get(nombre_defensor, 0) + 1

    # Encontramos el defensor con más tiros defendidos
    mejor_defensor = None
    mejor_contador = -1
    for nombre, cantidad in defensor.items():
        if cantidad > mejor_contador:
            mejor_defensor = nombre
            mejor_contador = cantidad
            
    return mejor_defensor, mejor_contador


def best_shoot_range(catalog):
    """
    Determina la distancia desde la cual se acertaron más tiros (independientemente del jugador).

    Parámetros:
        catalog (list): Lista de diccionarios con datos de tiros.

    Retorna:
        tuple: (distancia con más aciertos, número de aciertos)
    """
    tiro = {}

    # Contamos los tiros acertados agrupados por distancia
    for registro in catalog:
        if registro["SHOT_RESULT"] == "made":
            dist = registro["SHOT_DIST"]
            tiro[dist] = tiro.get(dist, 0) + 1

    # Encontramos la distancia con mayor cantidad de aciertos
    mejor_distancia = None
    mejor_contador = -1
    for dist, cantidad in tiro.items():
        if cantidad > mejor_contador:
            mejor_distancia = dist
            mejor_contador = cantidad

    return mejor_distancia, mejor_contador


def best_shoot_range_player(catalog):
    """
    Determina la mejor distancia de tiro para cada jugador
    (donde tuvo más aciertos) y cuántos aciertos logró desde allí.

    Parámetros:
        catalog (list): Lista de diccionarios con datos de tiros.

    Retorna:
        dict: Diccionario con estructura:
              {nombre_jugador: (mejor_distancia, aciertos_desde_esa_distancia)}
    """
    tirador = {}

    # Recorremos cada tiro en el catálogo
    for jugador in catalog:
        if jugador["SHOT_RESULT"] == "made":  # Solo consideramos los tiros acertados
            nombre = jugador["player_name"]
            dist = jugador["SHOT_DIST"]

            # Inicializamos el jugador en el diccionario si no existe
            if nombre not in tirador:
                tirador[nombre] = {}

            # Contamos cuántos aciertos tuvo desde cada distancia
            tirador[nombre][dist] = tirador[nombre].get(dist, 0) + 1

    # Determinamos la mejor distancia y el número de aciertos por jugador
    resultado = {}
    for nombre, distancias in tirador.items():
        mejor_dist = max(distancias, key=distancias.get)  # distancia con más aciertos
        mejor_contador = distancias[mejor_dist]
        resultado[nombre] = (mejor_dist, mejor_contador)

    return resultado

def validar_jugador(catalog,nombre_judador):
    """
    Busca el nombre del jugador digitado y analiza los datos
    Parámetros:
        catalog (list): Lista de diccionarios con datos de tiros.

    Retorna:
        dict: Diccionario con estructura:
              {nombre_jugador: (mejor_distancia, aciertos_desde_esa_distancia)}
    """
    jugador = {}
    #Recorre la lista buscando al jugador escrito
    for jugador in catalog:        
        if nombre_judador == jugador["player_name"]:
            return True
    return False

def cantidad_tiros(catalog, nombre_jugador, resultado_tiro):
    """
    Recorre el catalogo y va a contar solamenten los aciertos del jugador
    
    """
    aciertos = 0
    jugador = {}
    for jugador in catalog:        
        if nombre_jugador == jugador["player_name"]:            
            if jugador["SHOT_RESULT"]== resultado_tiro:
                aciertos += 1
    return aciertos
            
def mejor_distancia_jugador(catalog, nombre_jugador):
    """
    
    """
    aciertos = {}
    jugador = {}
    for jugador in catalog:        
        if nombre_jugador == jugador["player_name"]:
            if jugador["SHOT_RESULT"]== "made":
                nombre=jugador["player_name"]
                dist = jugador["SHOT_DIST"]
                aciertos[nombre] = {}
                aciertos[nombre][dist] = (dist)
                
    mejor_dist=0
    
    for nombre, distancias in aciertos.items():
        mejor_dist = max(distancias, key=distancias.get) 
    return mejor_dist
                
    