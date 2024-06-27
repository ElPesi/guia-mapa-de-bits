
from PIL import Image

def gaussiano(img):
    img = img.copy()  
    pixels = img.load()  

    width, height = img.size

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            totalPixels = 0
            totalR = 0
            totalG = 0
            totalB = 0

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

            pixels[x, y] = (totalR, totalG, totalB)

    return img

def main():
    # Cargar la imagen
    img = Image.open("marcos.jg")

    # Aplicar el filtro gaussiano
    img_gaussiano = gaussiano(img)

    # Mostrar la imagen original y la imagen filtrada
    img.show()
    img_gaussiano.show()

    # Guardar la imagen filtrada
    img_gaussiano.save("marcos_gaussiano.jpg")

main()
