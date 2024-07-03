from PIL import Image
import os

def pixelator():
    # Crear la carpeta para las imágenes filtradas si no existe
    ruta_carpeta = "ImagenesFiltradas"
    if not os.path.exists(ruta_carpeta):
        os.mkdir(ruta_carpeta)
         
    ruta_imagen = input("Ingrese la ruta de la imagen: ")
    
    # Cargar la imagen
    img = Image.open(ruta_imagen)
  
    width, height = img.size
    
    # Tamaño del píxel (resolución) para el efecto pixelado
    resolution = 10  
    
    # Iterar sobre los píxeles y aplicar el efecto pixelado
    for x in range(0, width, resolution):
        for y in range(0, height, resolution):
            # Obtener el color del píxel original en la esquina superior izquierda del bloque
            c = img.getpixel((x, y))
            
            # Pintar todo el bloque con ese color
            for i in range(resolution):
                for j in range(resolution):
                    px = x + j
                    py = y + i
                    if px < width and py < height:
                        img.putpixel((px, py), c)
    
    img.show()
    
    # Guardar la imagen filtrada con un nombre apropiado
    nombre_imagen = os.path.basename(ruta_imagen)
    nombre_sin_extension, extension = os.path.splitext(nombre_imagen)
    nombre_guardado = f"{nombre_sin_extension}Pixelated{extension}"
    ruta_imagen_guardada = os.path.join(ruta_carpeta, nombre_guardado)
    img.save(ruta_imagen_guardada)
    print(f"Imagen pixelada guardada en: {ruta_imagen_guardada}")
    

# Llamar a la función para ejecutar el script
pixelator()


    
    
