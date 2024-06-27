from PIL import Image
import os

def preload():
    ruta_carpeta = "\\institutodc01\d48044935\pesi y julio\Guia mapa de bits\ej7"
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)
        
    ruta_imagen = input("Ingrese ruta de la imagen: ")
    img = Image.open(ruta_imagen).convert("RGB")
    return img, ruta_carpeta

def setup():
    img, ruta_carpeta = preload()
    width, height = img.size
    
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            gris = int((r + g + b) / 3) 
            img.putpixel((x, y), (gris, gris, gris))

    img.show()
    
    nombre_imagen = os.path.basename(img)
    nombre_imagen_sin_extension = os.path.splitext(nombre_imagen)
    ruta_imagen_guardada = os.path.join(ruta_carpeta, nombre_imagen_sin_extension + ".jpg")
    img.save(ruta_imagen_guardada)
        
setup()
