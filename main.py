# Asignacion de Programacion 1 (PA1) - Alcibiades Bustillo - COMP6785
# Creado por: Christian Robles

from Graph import Graph
from DFS import *
from ConnectedComponent import *


def main():
    # Breve intoduccion a lo que hace el programa
    print(
        "\n=========================================================================\n"
        "                            PA1 - COMP6785                               \n"
        "=========================================================================\n"
        "Este programa permite obtener el orden topologico, determinar si hay\n"
        "ciclos, o contar los componentes conexos para un Grafo dado."
    )

    # Instrucciones de como proveerle el grafo al programa
    print(
        "\nComo pasar el Grafo al programa: \n"
        "El grafo se pasa al programa mediante un archivo .txt ubicado dentro\n"
        "de la carpeta nombrada como data/. El nombre debe seguir el siguiente\n"
        "formato: <nombre>DG.txt si es un Grafo dirigido o <nombre>G.txt si es\n"
        "un Grafo no dirigido, donde <nombre> puede ser cualquier concatenacion\n"
        "de caracteres."
    )

    # Aviso sobre como el programa determina si un grafo es o no es dirigido
    print(
        "\nNota: una D (mayuscula) en la penultima posicion del nombre indica que\n"
        "el grafo es dirigido."
    )

    # Instrucciones sobre el formato que se espera en el archivo
    print(
        "\nEstructura del archivo: \n"
        "Primera linea contiene un entero unico n que indica la cantidad de\n"
        "vertices. Segunda linea contiene un entero unico e que indica cuantas\n"
        "aristas hay en el Grafo. Las lineas restantes contienen dos enteros\n"
        "separados por espacios en blanco, digamos u y v, los cuales representan\n"
        "la arista que los conecta (u, v).\n"
    )

    name = ""  # Se inicializa la variable del nombre del archivo
    while (
        True
    ):  # Se itera infinitamente hasta que se provea un nombre correspodiente a un archivo en la carpeta de data
        try:  # Trate de abrir un archivo basado en el nombre provisto por el usuario
            print(
                "Escriba 'salir' para terminar ejecucion..."
            )  # Mensaje para indicarle al usario como terminar el programa
            name = input(
                "Nombre del archivo (sin .txt): "
            )  # El usuario entra el nombre del archivo
            file = open(
                "data/" + name + ".txt", "r"
            )  # Se busca y se abre el archivo con formato .txt en la carpeta data
            break  # Se rompe el ciclo infinito
        except:  # Captura si ocurre un error al intentar abrir el archivo
            if name == "salir":  # Verifica si el usuario ingraso 'salir'
                return  # Termina inmediantamente ejecucion del programa
            print(
                "\nNo se encontro ningun archivo con el nombre {}.txt, intentelo de nuevo...\n".format(
                    name
                )
            )

    n = int(next(file))  # Se extrae la primera linea del archivo
    e = int(next(file))  # Se extrae la segunda linea del acrhivo

    directed = (
        name[-2] == "D"
    )  # Busca el penultimo caracter de nombre ingresado y lo compara con 'D'
    # Asi se determina si el grafo es o no es dirigido

    G = Graph(
        directed
    )  # Se crea un grafo G al cual se le indica si es o no es dirigido

    print("\nLeyendo el Grafo...\n")
    for (
        line
    ) in (
        file.readlines()
    ):  # Se itera por las lineas restantes del archivo (contienen las aristas)
        (
            u,
            v,
        ) = (
            line.split()
        )  # Se divide la linea en dos enteros asignados a u y v respectivamente
        G.add_vertex(u)  # Se añade el valor de u al grafo G
        G.add_vertex(v)  # Se añade el valor de v al grafo G
        G.add_edge(u, v)  # Se crea y se añade la arista (u,v) al grafo G

    file.close()  # Se cierra el archivo

    # Se imprimen las opciones en la consola
    print("Seleccione una de las siguientes opciones:")
    print("1. Conseguir el orden topologico del Grafo.")
    print("2. Determinar si el Grafo tiene al menos un ciclo.")
    print("3. Contar los componentes conexos del Grafo.\n")

    opt = ""  # Se inicializa la varible que va a guardar la opcion seleccionada
    while (
        True
    ):  # Se itera infinitamente hasta que se provea una de las opciones correctas
        print(
            "Escriba 'salir' para terminar ejecucion..."
        )  # Mensaje para indicarle al usario como terminar el programa
        opt = input(
            "Indique el numero de la opcion pertinente: "
        )  # Usuario entra opcion deaseada
        if opt == "salir":  # Verifica si el usuario ingraso 'salir'
            return  # Termina inmediantamente ejecucion del programa
        if opt in ["1", "2", "3"]:  # Verifica si la opcion entrada es 1, 2, o 3
            break  # Rompe el ciclo infinito ya que una de las opciones disponibles fue provista
        print(
            "\nPor favor provea un valor que sea 1, 2, o 3.\n"
        )  # Mensaje indicando las opciones disponibles

    print(
        "\nOpcion {} seleccionada...".format(opt)
    )  # Se imprime un mensaje indicando la opcion selccionada

    if opt == "1":  # Verifica si la opcion seleccionada fue la 1
        if not directed:  # Verifica si el grafo no es dirigido
            # Imprime mensaje para orden topologico de un grafo no dirigido
            print(
                ">> El Grafo debe ser dirigido para poder conseguir su orden topologico."
            )
        else:  # Grafo es dirigido
            cycles, order = DFS(G)  # Se la aplica DFS (Depth First Search) al grafo G
            if cycles:  # Verifica si el grafo tiene ciclos
                # Imprime mensaje para orden topologico de un grafo ciclico
                print(
                    ">> El Grafo no puede contener ciclos para poder obtener un orden topologico adecuado."
                )
            else:  # No tiene ciclos
                arr = order.to_array()  # Se obtiene un arreglo con el orden topologico
                print(">> Orden Topologico: ")
                print(
                    ">>", " -> ".join(arr)
                )  # Se imprime el orden topologico obtenido con -> indicando la direccion
    elif opt == "2":  # Verifica si la opcion seleccionada fue la 2
        cycles, _ = DFS(G)  # Se la aplica DFS (Depth First Search) al grafo G
        if cycles:  # Verifica si el grafo tiene ciclos
            # Imprime mensaje para un grafo ciclico
            print(">> El Grafo contiene al menos un ciclo.")
        else:  # No tiene ciclos
            # Imprime mensaje para un grafo aciclico
            print(">> No se encontro ningun ciclo en el Grafo.")
    else:  # Si no es opcion 1 o 2, pues debe ser opcion 3
        count = ConnectedComponent(G)  # Se le aplica la funcion ConnectedComponents
        # Imprime un mensaje para indicar la cantidad de componentes conexos encontrados
        print(">> Se encontraron {} componentes conexos en el Grafo.".format(count))

    print(
        "\nLa ejecucion del programa ha culminado.\n"
    )  # Le indica al usuario que el programa termino su ejecucion


main()
