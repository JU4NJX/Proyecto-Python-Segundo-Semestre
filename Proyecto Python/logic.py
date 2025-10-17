import csv
import os

def new_logic ():
    catalog = [ ]
    return catalog
    
def carga_datos (catalog, filename):
    archivo = os.path.join("Data", filename)
    
    with open(archivo, encoding="utf-8") as ruta:
        leer_archivo = csv.DictReader(ruta)
        for fila in leer_archivo:
            catalog.append(fila)
            
    return catalog

def best_shooters (catalog):
    tirador = {}
    for jugador in catalog:
        if jugador["SHOT_RESULT"] !=  "missed":
            if jugador["player_name"] in tirador.keys():
                tirador[jugador["player_name"]] += 1
            else:
                tirador [jugador["player_name"]] = 1
    mejor_tirador = None
    mejor_contador = -1
    for i in tirador.keys():
        if tirador[i] > mejor_contador:
            mejor_tirador = i
            mejor_contador = tirador[i]
            
    return mejor_tirador, mejor_contador
        
def best_defender (catalog):
    defensor = {}
    for jugador in catalog:
        if jugador["SHOT_RESULT"] ==  "missed":
            if jugador["CLOSEST_DEFENDER"] in defensor.keys():
                defensor[jugador["CLOSEST_DEFENDER"]] += 1
            else:
                defensor [jugador["CLOSEST_DEFENDER"]] = 1
    mejor_defensor = None
    mejor_contador = -1
    for i in defensor.keys():
        if defensor [i] > mejor_contador:
            mejor_defensor = i
            mejor_contador = defensor [i]
            
    return mejor_defensor, mejor_contador

def best_shoot_range(catalog): 
    tiro = {}
    for distancia in catalog:
        if distancia["SHOT_RESULT"] == "made":
            dist = distancia["SHOT_DIST"]
            if dist in tiro:       # primero comprobamos si la clave existe
                tiro[dist] += 1
            else:
                tiro[dist] = 1

    mejor_distancia = None
    mejor_contador = -1
    for dist in tiro:
        if tiro[dist] > mejor_contador:
            mejor_distancia = dist
            mejor_contador = tiro[dist]

    return mejor_distancia, mejor_contador

def best_shoot_range_player (catalog):

    tirador = {}

    # Recorremos cada tiro
    for jugador in catalog:
        if jugador["SHOT_RESULT"] == "made":
            nombre = jugador["player_name"]
            dist = jugador["SHOT_DIST"]

            # Si el jugador no está en el diccionario, lo agregamos
            if nombre not in tirador:
                tirador[nombre] = {}

            # Contamos los tiros exitosos por distancia
            tirador[nombre][dist] = tirador[nombre].get(dist, 0) + 1

    # Ahora encontramos la mejor distancia por jugador
    resultado = {}
    for nombre, distancias in tirador.items():
        mejor_dist = max(distancias, key=distancias.get)
        mejor_contador = distancias[mejor_dist]
        resultado[nombre] = (mejor_dist, mejor_contador)

    return resultado
