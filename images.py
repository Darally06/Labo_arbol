from typing import Any, List, Optional, Tuple
import os


def proces_images(carpeta):
    images = []
    archivos = os.listdir(carpeta)

    for archivo in archivos:
        ruta_archivo = os.path.join(carpeta, archivo)
        if os.path.isfile(ruta_archivo):
            name = os.path.basename(ruta_archivo)
            categoria_archivo = obtener_categoria(name)
            peso_archivo = os.path.getsize(ruta_archivo) / (1024 * 1024)
            registro = {"Nombre": name, "Categoria": categoria_archivo, "Peso": peso_archivo}
            images.append(registro)
        elif os.path.isdir(ruta_archivo):
            images.extend(proces_images(ruta_archivo))

    return images

def obtener_categoria(nombre_archivo):
    if "dog" in nombre_archivo.lower():
        return "dogs"
    elif "rider" in nombre_archivo.lower():
        return "humans"
    elif "horse" in nombre_archivo.lower():
        return "horses"
    elif "cat" in nombre_archivo.lower():
        return "cats"
    elif "bike" in nombre_archivo.lower():
        return "bikes"
    elif "car" in nombre_archivo.lower():
        return "cars"
    else:
        return "flowers"



