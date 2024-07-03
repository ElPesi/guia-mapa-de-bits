from PIL import Image
import os

def gaussiano():
    #Creo la nueva carpeta
    ruta_carpeta = "ImagenesFiltradas"
    if not os.path.exists(ruta_carpeta):
        os.mkdir(ruta_carpeta)

    ruta_imagen = input("Ingrese la ruta de la imagen: ")
    img = Image.open(ruta_imagen)
    
    width, height = img.size
    
    pixels = img.load()

    # Aplicamos el filtro gaussiano
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            totalPixels = 0
            totalR = 0
            totalG = 0
            totalB = 0

            # Sumamos los valores de los píxeles vecinos
            for j in range(-1, 2):
                for i in range(-1, 2):
                    auxX = x + i
                    auxY = y + j

                    r, g, b = pixels[auxX, auxY]
                    totalR += r
                    totalG += g
                    totalB += b
                    totalPixels += 1

            totalR //= totalPixels
            totalG //= totalPixels
            totalB //= totalPixels

            img.putpixel((x, y), (totalR, totalG, totalB))

    
    img.show()

    # Guardar la imagen
    nombre_imagen = os.path.basename(os.path.basename(ruta_imagen))
    nombre_imagen_sin_extension = os.path.splitext(nombre_imagen)[0]
    ruta_imagen_guardada = os.path.join(ruta_carpeta, nombre_imagen_sin_extension + "_gaussiano_.jpg")
    img.save(ruta_imagen_guardada)
    print(f"Imagen filtrada gaussiano guardada en: {ruta_imagen_guardada}")
    
gaussiano()
