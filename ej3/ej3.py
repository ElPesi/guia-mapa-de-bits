from PIL import Image
import os

def rotar_img():
    
    marcos = input("Ingrese ruta de la imagen: ")
    angulo = int(input("Ingrese rotacion del angulo: "))

    img = Image.open('marcos.jpg')
    rotated_img = img.rotate(angulo)
    filename, file_extension = os.path.splitext(marcos)
    rotated_img.save(f"{filename}_Rot{file_extension}")
    rotated_img.show()

rotar_img()