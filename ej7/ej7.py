from PIL import Image
import os

def Blanco_y_negro():
    #Creo la nueva carpeta
    ruta_carpeta = "ImagenesFiltradas"
    if not os.path.exists(ruta_carpeta):
        os.mkdir(ruta_carpeta)
    
    ruta_imagen = input("Ingrese ruta de la imagen: ")
    img = Image.open(ruta_imagen)

    #Aplicamos el filtro ByN
    width, height = img.size
    
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            gris = int((r + g + b) / 3) 
            img.putpixel((x, y), (gris, gris, gris))

    img.show()
    
    #Guardo la nueva imagen
    nombre_imagen = os.path.basename(os.path.basename(ruta_imagen))
    nombre_imagen_sin_extension = os.path.splitext(nombre_imagen)[0]
    ruta_imagen_guardada = os.path.join(ruta_carpeta, nombre_imagen_sin_extension + "_blancoynegro_.jpg")
    img.save(ruta_imagen_guardada)
    print(f"Imagen Blanco Y Negro guardada en: {ruta_imagen_guardada}")
   
Blanco_y_negro()


