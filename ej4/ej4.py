from PIL import Image
import os

def Imagenes_recortadas():
    #Creo la nueva carpeta
    ruta_carpeta = "Recortes"
    if not os.path.exists(ruta_carpeta):
        os.mkdir(ruta_carpeta)
        
    ruta_imagen = input("Ingrese la ruta de la imagen: ")
    while not os.path.isfile(ruta_imagen):
        ruta_imagen = input("La ruta ingresada no es válida. Ingrese nuevamente la ruta de la imagen: ")

    img = Image.open(ruta_imagen)
    width, height = img.size

    print(f"Dimensiones de la imagen: {width}x{height}")

    X1 = int(input('Ingrese la posición X donde iniciará el recorte: '))
    while X1 >= width:
        X1 = int(input('La posición X ingresada es mayor o igual al ancho de la imagen. Ingrese nuevamente: '))

    Y1 = int(input('Ingrese la posición Y donde iniciará el recorte: '))
    while Y1 >= height:
        Y1 = int(input('La posición Y ingresada es mayor o igual a la altura de la imagen. Ingrese nuevamente: '))

    widthImg = int(input('Ingrese el ancho del recorte: '))
    while widthImg <= 0 or X1 + widthImg > width:
        widthImg = int(input('El ancho del recorte no puede ser negativo ni exceder el ancho de la imagen desde la posición X. Ingrese nuevamente: '))

    heightImg = int(input('Ingrese la altura del recorte: '))
    while heightImg <= 0 or Y1 + heightImg > height:
        heightImg = int(input('La altura del recorte no puede ser negativa ni exceder la altura de la imagen desde la posición Y. Ingrese nuevamente: '))

    marcosCortado = img.crop((X1, Y1, X1 + widthImg, Y1 + heightImg))
    marcosCortado.show()

    #Guardo la nueva imagen
    nombre_imagen = os.path.basename(ruta_imagen)
    nombre_imagen_sin_extension = os.path.splitext(nombre_imagen)[0]
    ruta_imagen_guardada = os.path.join(ruta_carpeta, nombre_imagen_sin_extension + "_recortado.jpg")
    marcosCortado.save(ruta_imagen_guardada)

Imagenes_recortadas()
