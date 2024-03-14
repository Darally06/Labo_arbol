from typing import Any, List, Optional, Tuple
import os
from arbol import *

# Cargar los datos. 

carpeta = "C:\\Users\\danie\\OneDrive\\Escritorio\\data"
images = proces_images(carpeta)

#for registro in images:
#    print(registro)

avl = AVL()
raiz = None

# MAIN

def separador():
    print("______________________")

print("Bienvenido al algoritmo del Arbol Binario Balanceado.")
separador()
print("Creadores: Juan Aguirre, Daniella Guerra, Maria Gabriela Reyes.")
separador()

user = str(input("Por favor, ingrese su nombre:\n"))

option = 0

while option != 6:
    separador()
    print("Hola", user, ", ¿Que opcion te gustaria utilizar hoy?")
    separador()
    print("#1. Añadir Nodo. ")
    print("#2. Eliminar Nodo. ")
    print("#3. Buscar Nodo.")
    print("#4. Buscar Nodo (con parametros especificos).")
    print("#5. Mostrar el recorrido por niveles del arbol.")
    print("#6. Salir del programa.")
    separador()

    option = int(input("Seleccione una opción: "))
    separador()

    if option == 1:
        print("Eleccion escogida: [#1. Insertar Nodo.]")
        nombre_archivo = input("Ingrese el nombre de la foto a insertar: ")

        if os.path.exists(f"C:\\Users\\danie\\OneDrive\\Escritorio\\data\\{nombre_archivo}"):
            avl.raiz = avl.insertar(avl.raiz, nombre_archivo)
            print("El nodo ha sido insertado exitosamente.")
            separador()
            #dot = Digraph(comment="Árbol AVL de nombres de archivos")
            #avl.graficar_arbol(avl.raiz, dot)
            #dot.render("arbol_avl_nombres", format="png", cleanup=True)
            #dot.view()
        else:
            print(f"El archivo '{nombre_archivo}' no existe en el directorio.")


    elif option == 2:
      print("Eleccion escogida: [#2. Eliminar Nodo.]")

    elif option == 3:
      print("Eleccion escogida: [#3. Salir del programa.]")

    elif option == 4:
      print("Eleccion escogida: [#4. Buscar Nodo (con parametros especificos).]")

    elif option == 5:
        print("Eleccion escogida: [#5. Mostrar el recorrido por niveles del arbol.]")

    elif option == 6:
        print("Eleccion escogida: [#6. Salir del programa.]")
        Node.vaciar_arbol()

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")