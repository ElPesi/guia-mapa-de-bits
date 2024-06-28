let img;

function preload(){
  img = loadImage('sample_bfe761110a7cb4d3c7d45a353f9fc0a4.jpg');
  
}
function setup(){
  createCanvas(1920,1080);
  let r = 8
  for(let x = 0; x < img.width; x += r){
    for(let y = 0; y < img.height; y += r){
      c = img.get(x,y);
      for(let i = 0; i < r; i++){
        for(let j = 0; j < r; j++){
          let auxX = x + j;
          let auxY = y + i;
          img.set(auxX,auxY,c);    

        }
      }
    }
  }
  img.updatePixels()
  image(img,0,0);
}