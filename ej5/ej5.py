from PIL import Image

def agregar_marca_de_agua(ruta_imagen_base, ruta_imagen_marca, posicion):
    
    imagen_base = Image.open(ruta_imagen_base).convert("RGBA")
    marca_de_agua = Image.open(ruta_imagen_marca).convert("RGBA")

    ancho_base, alto_base = imagen_base.size
    ancho_marca, alto_marca = marca_de_agua.size

    if posicion == 'Superior izquierda':
        posicion = (50, 50)
    elif posicion == 'Superior derecha':
        posicion = (ancho_base - ancho_marca - 50, 50)
    elif posicion == 'Inferior izquierda':
        posicion = (50, alto_base - alto_marca - 50)
    elif posicion == 'Inferior derecha':
        posicion = (ancho_base - ancho_marca - 50, alto_base - alto_marca - 50)
    else:
        raise ValueError("Posición no válida. Intenta usar: Superior izquierda, Superior derecha, Inferior izquierda, Inferior derecha")

    imagen_base.paste(marca_de_agua, posicion, marca_de_agua)
    
    ruta_salida = "imagen_marcada.png"
    imagen_base.save(ruta_salida, "PNG")

    print(f"Imagen guardada en: {ruta_salida}")

ruta_imagen_base = input("Introduce la ruta de la imagen base: ")
ruta_imagen_marca = input("Introduce la ruta de la marca de agua: ")
print("Opciones de posición: Superior izquierda, Superior derecha, Inferior izquierda, Inferior derecha")
posicion = input("Introduce la posición de la marca de agua: ")

agregar_marca_de_agua(ruta_imagen_base, ruta_imagen_marca, posicion)

