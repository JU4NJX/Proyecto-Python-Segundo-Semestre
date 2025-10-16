import csv
import os

def new_logic ():
    catalog = [ ]
    
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

def best_shoot_range (catalog):
    pass