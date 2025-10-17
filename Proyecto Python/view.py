import logic
import sys
from tabulate import tabulate

def new_logic():
    return logic.new_logic()

def print_menu():
    print("Bienvenido")
    print("0- Cargar información")
    print("1- Ejecutar Top1 Mejores Tiradores")
    print("2- Ejecutar Top1 Mejores Defensores")
    print("3- Ejecutar Mejor Distancia de Tiro (General)")
    print("4- Ejecutar Mejor Distancia de Tiro (Por jugador)")
    print("5- Salir")

def best_shooters(control):
    respuesta = logic.best_shooters(control)
    print(tabulate([respuesta], headers=["Tirador", "Numero Tiros"], tablefmt="grid"))

def best_defender(control):
    respuesta = logic.best_defender(control)
    print(tabulate([respuesta], headers=["Defensa", "Numero Tiros Defendidos"], tablefmt="grid"))

def best_shoot_range(control):
    respuesta = logic.best_shoot_range(control)
    print(tabulate([respuesta], headers=["Distancia (Metros)", "Numero Tiros"], tablefmt="grid"))

def best_shoot_range_player(control):
    respuesta = logic.best_shoot_range_player(control)
    filas = []
    for jugador, (distancia, tiros) in respuesta.items():
        filas.append([jugador, distancia, tiros])
    print(tabulate(filas, headers=["Tirador", "Distancia (Metros)", "Numero Tiros"], tablefmt="grid"))


control = new_logic()

def main():
    print("asdadsa")
    working = True
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 0:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 1:
            best_shooters(control)
            
        elif int(inputs) == 2:
            best_defender(control)

        elif int(inputs) == 3:
            best_shoot_range(control)
            
        elif int(inputs) == 4:
            best_shoot_range_player(control)
            
        elif int(inputs) == 5:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
    
def load_data(control):
    
    logic.carga_datos(control, "shot_logs.csv")
    print("Datos cargados exitosamente")
    print("Total de información cargada:", len(control))
    
