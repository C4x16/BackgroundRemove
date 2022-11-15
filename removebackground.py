from rembg import remove
from PIL import Image
#imagein = '/home/olivier/Documents/Git/BackgroundRemove/darkvador.jpg'
#imageout= '/home/olivier/Documents/Git/BackgroundRemove/darvador_out.png')
imagein = '/home/olivier/Documents/Git/BackgroundRemove/toutou.jpeg'
imageout= '/home/olivier/Documents/Git/BackgroundRemove/toutou.png'
without_bg = remove(Image.open(imagein))
without_bg.save(imageout)
