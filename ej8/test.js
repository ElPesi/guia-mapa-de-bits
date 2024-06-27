let img;

function preload() {
    img = loadImage("Sin título.png");
}

function setup() {
    createCanvas(500, 500);
    image(img, 0, 0); // Dibujar la imagen en el lienzo
    noLoop();
    gaussiano(); // Aplicar el filtro gaussiano
}

function gaussiano() {
    img.loadPixels(); // Cargar los píxeles de la imagen

    for (let y = 1; y < img.height - 1; y++) {
        for (let x = 1; x < img.width - 1; x++) {
            let c = promedioVecino(x, y);
            img.set(x, y, c);
        }
    }

    img.updatePixels(); // Actualizar los píxeles modificados en la imagen
}

function promedioVecino(x, y) {
    let totalPixels = 0;
    let totalR = 0;
    let totalG = 0;
    let totalB = 0;

    for (let j = -1; j <= 1; j++) {
        for (let i = -1; i <= 1; i++) {
            let auxX = x + i;
            let auxY = y + j;

            let c = img.get(auxX, auxY);
            totalR += c[0];
            totalG += c[1];
            totalB += c[2];
            totalPixels++;
        }
    }

    totalR /= totalPixels;
    totalG /= totalPixels;
    totalB /= totalPixels;

    return color(totalR, totalG, totalB);
}
