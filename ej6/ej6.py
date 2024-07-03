import os
from PIL import Image

def crear_collage():

    print("Creación de Collage de Imágenes")
    print("------------------------------")

    # Solicitar ruta de la carpeta y obtener las imágenes
    while True:
        ruta_carpeta = input("Introduce la ruta de la carpeta que contiene al menos 9 imágenes: ")
        if os.path.isdir(ruta_carpeta):
            # Verificar que la carpeta contenga al menos 9 imágenes válidas
            archivos = os.listdir(ruta_carpeta)
            imagenes = [archivo for archivo in archivos if archivo.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]
            if len(imagenes) >= 9:
                break
            else:
                print("La carpeta no contiene al menos 9 imágenes válidas.")
        else:
            print("Ruta de carpeta inválida. Inténtalo de nuevo.")

    # Solicitar resolución del collage
    ancho = int(input("Ingrese el ancho en píxeles del collage: "))
    alto = int(input("Ingrese el alto en píxeles del collage: "))
    resolucion = (ancho, alto)

    # Función auxiliar para redimensionar una imagen a miniatura
    def resize_imagen(ruta_imagen, size):
        imagen = Image.open(ruta_imagen)
        imagen.thumbnail(size)
        return imagen

    num_imagenes = len(imagenes)
    columnas, filas = 3, 3  # Se especifica que el collage tendrá 3x3 miniaturas

    ancho_celda = resolucion[0] // columnas
    alto_celda = resolucion[1] // filas

    collage = Image.new('RGB', resolucion)
    index = 0

    # Construir el collage
    for y in range(filas):
        for x in range(columnas):
            if index < num_imagenes:
                ruta_imagen = os.path.join(ruta_carpeta, imagenes[index])
                miniatura = resize_imagen(ruta_imagen, (ancho_celda, alto_celda))
                collage.paste(miniatura, (x * ancho_celda, y * alto_celda))
                index += 1

    # Guardar el collage
    ruta_salida = "collage_resultado.png"
    collage.save(ruta_salida)
    print(f"Collage guardado en: {ruta_salida}")

# Llamada a la función principal para crear el collage
crear_collage()
