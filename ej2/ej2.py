from PIL import Image
import os

def guardar_img():
    ejImg2 = Image.open("ejImg2.jpg")
    ejImg2.show()   

    nuevo_nombre = "copia.jpg"
    nueva_ruta = os.path.join(nuevo_nombre)

    ejImg2.save(nueva_ruta)
    print("Imagen guardada con éxito en:", nueva_ruta)

guardar_img()