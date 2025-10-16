import logic
import sys

def new_logic():
    return logic.new_logic()

def print_menu():
    print("Bienvenido")
    print("0- Cargar información")
    print("1- Ejecutar Top5 Mejores Tiradores")
    print("2- Ejecutar Top5 Mejores Defensores")
    print("3- Ejecutar Mejor Rango de Tiro por Jugador")
    print("4- Salir")

def best_shooters ():
    pass
def best_defender ():
    pass
def best_shoot_range ():
    pass

control = new_logic()

def main():

    working = True
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 0:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 1:
            print_best_shooters(control)

        elif int(inputs) == 2:
            print_best_defender(control)

        elif int(inputs) == 3:
            print_best_shoot_range(control)
        elif int(inputs) == 4:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
    
def load_data(control):
    
    logic.load_data(control, "shot_logs.csv")
    print("Datos cargados exitosamente")
    print("Total de taxis cargados:", len(control))