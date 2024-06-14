from PIL import Image

def mostrar_datos():
    ruta_imagen = input("Por favor, ingresa la ruta de la imagen: ")
    ejImg = Image.open(ruta_imagen)
    width, height = ejImg.size
    
    print(f'nombre      |   {ejImg.filename.split("/")[-1]}')
    print(f'extension   |   {ejImg.format}')
    print(f'resolucion  |   {ejImg.size}')
    print(f'pixeles     |   {width * height}')
    print(f'ruta        |   {ejImg.filename}')

    ejImg.show()

mostrar_datos()
