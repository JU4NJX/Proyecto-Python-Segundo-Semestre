import logic
import sys
from tabulate import tabulate


def new_logic():
    """
    Inicializa y retorna una nueva estructura de datos (catálogo).
    Llama a la función 'new_logic()' del módulo 'logic'.

    Retorna:
        list: Catálogo vacío creado por la función del módulo logic.
    """
    return logic.new_logic()


# Creamos el catálogo global del programa (estructura principal de datos)
control = new_logic()

def print_menu():
    """
    Imprime el menú principal con las opciones disponibles
    para el usuario en la consola.
    """
    print("Bienvenido")
    print("\nAntes de comenzar el analisis de tiros de la NBA ingrese la opcion 0  para cargar la infomacion")
    print("Tambien antes de escoger una opcion de la 6 a la 8  seleccione primero la opcion 5 para saber el nombre del jugador,Gracias!") 
    print("0- Cargar información")
    print("1- Ejecutar Mejores Tiradores")
    print("2- Ejecutar Mejores Defensores")
    print("3- Ejecutar Mejor Distancia de Tiro (General)")    
    print("4- Ejecutar Mejor Distancia de Tiro (Por jugador)")    
    print("5- Ingresar Nombre del jugador")
    print("6- cantidad de aciertos")
    print("7- cantidad de errados")
    print("8- Ejecutar Mejor Distancia de Tiro del jugador")
    print("9- Salir")


def best_shooters(control):
    """
    Muestra en formato de tabla el mejor tirador (jugador con más aciertos).

    Parámetros:
        control (list): Catálogo con los datos cargados.
    """
    respuesta = logic.best_shooters(control)
    # La función devuelve una tupla: (jugador, número de tiros)
    print(tabulate([respuesta], headers=["Tirador", "Número Tiros"], tablefmt="grid"))


def best_defender(control):
    """
    Muestra en formato de tabla el mejor defensor (jugador que provocó más fallos).

    Parámetros:
        control (list): Catálogo con los datos cargados.
    """
    respuesta = logic.best_defender(control)
    # La función devuelve una tupla: (defensor, número de tiros defendidos)
    print(tabulate([respuesta], headers=["Defensa", "Número Tiros Defendidos"], tablefmt="grid"))


def best_shoot_range(control):
    """
    Muestra la distancia con mayor cantidad total de aciertos en formato de tabla.

    Parámetros:
        control (list): Catálogo con los datos cargados.
    """
    respuesta = logic.best_shoot_range(control)
    # La función devuelve una tupla: (distancia, número de aciertos)
    print(tabulate([respuesta], headers=["Distancia (Metros)", "Número Tiros"], tablefmt="grid"))


def best_shoot_range_player(control):
    """
    Muestra, en formato de tabla, la mejor distancia de tiro por cada jugador.

    Parámetros:
        control (list): Catálogo con los datos cargados.
    """
    respuesta = logic.best_shoot_range_player(control)
    filas = []

    # Convertimos el diccionario de resultados en una lista de filas para tabular
    for jugador, (distancia, tiros) in respuesta.items():
        filas.append([jugador, distancia, tiros])

    print(tabulate(filas, headers=["Tirador", "Distancia (Metros)", "Número Tiros"], tablefmt="grid"))




def validar_jugador(control, nombre_jugador):
    """ 
    """
    validar= logic.validar_jugador(control,nombre_jugador)

    return validar

def cantidad_tiros(control, nombre_jugador, resultado_tiro):
    """
    """
    cantidad = logic.cantidad_tiros(control,nombre_jugador, resultado_tiro)
    if resultado_tiro=="made":
        print(f"La cantidad de tiros acertados del jugador, {nombre_jugador} fue de {cantidad}")
    else: 
        print(f"La cantidad de tiros errados del jugador, {nombre_jugador} fue de {cantidad}")
    
def mejor_distancia_jugador(control,nombre_jugador):
    """
    
    """
    respuesta = logic.mejor_distancia_jugador(control,nombre_jugador)
    print(f"La mejor distancia de tiro para el jugador {nombre_jugador} es de {respuesta}mts")    
        
    
    

def main():
    """
    Función principal del programa.
    Muestra el menú y ejecuta las acciones según la opción elegida por el usuario.
    """
    print("Programa de Análisis de Tiros NBA") 
    working = True
    nombre_jugador = ""

    while working:
        print_menu()     
        inputs = input('Seleccione una opción para continuar\n')

        # Opción 0: cargar datos
        if int(inputs) == 0:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)

        # Opción 1: mejores tiradores
        elif int(inputs) == 1:
            best_shooters(control)

        # Opción 2: mejores defensores
        elif int(inputs) == 2:
            best_defender(control)

        # Opción 3: mejor distancia general
        elif int(inputs) == 3:
            best_shoot_range(control)

        # Opción 4: mejor distancia por jugador
        elif int(inputs) == 4:
            best_shoot_range_player(control)
            
        # Opción 5: Nombre Jugador
        elif int(inputs) == 5:
            nombre_jugador = input('Ingrese el Nombre del jugador\n')
            if validar_jugador(control, nombre_jugador):
                print("\nJugador encontrador ", nombre_jugador) 
            else:
                print("Vuelva ha intentarlo") 
                
        # Opción 6: Cantidad Aciertos
        elif int(inputs) == 6:
            cantidad_tiros(control, nombre_jugador, "made")
            
        # Opción 7: Cantidad Aciertos
        elif int(inputs) == 7:
            cantidad_tiros(control, nombre_jugador, "missed")
            
        # Opción 8: Mejor distancia de tiro
        elif int(inputs) == 8:
            mejor_distancia_jugador(control, nombre_jugador)
                
        # Opción 9: salir
        elif int(inputs) == 9:
            working = False
            print("\nGracias por utilizar el programa") 

        # Opción no válida
        else:
            print("Opción errónea, vuelva a elegir.\n")

    # Finaliza el programa limpiamente
    sys.exit(0)


def load_data(control):
    """
    Carga los datos desde el archivo 'shot_logs.csv' a la estructura del catálogo.

    Parámetros:
        control (list): Catálogo donde se almacenará la información cargada.

    Retorna:
        None
    """
    # Llamamos a la función del módulo logic para cargar los datos desde CSV
    logic.carga_datos(control, "shot_logs.csv")

    # Mostramos mensajes de confirmación
    print("Datos cargados exitosamente")
    print("Total de información cargada:", len(control))