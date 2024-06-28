from PIL import Image
import os

def pixelator():
    # Creo la nueva carpeta
    ruta_carpeta = "ImagenesFiltradas"
    if not os.path.exists(ruta_carpeta):
        os.mkdir(ruta_carpeta)
    
    ruta_imagen = input("Ingrese ruta de la imagen: ")
    img = Image.open(ruta_imagen)
    
    width, height = img.size
    resolution = 8
    
    for x in range(0, width, resolution):
        for y in range(0, height, resolution):
            c = img.getpixel((x, y))
            for i in range(resolution):
                for j in range(resolution):
                    auxX = x + j
                    auxY = y + i
                    img.putpixel((auxX, auxY), c)
    
    img.show()

    #Guardo la nueva imagen
    #nombre_imagen = os.path.basename(os.path.basename(ruta_imagen))
    #nombre_imagen_sin_extension = os.path.splitext(nombre_imagen)[0]
    #ruta_imagen_guardada = os.path.join(ruta_carpeta, nombre_imagen_sin_extension + "_blancoynegro_.jpg")
    #img.save(ruta_imagen_guardada)
    
pixelator()

    
    