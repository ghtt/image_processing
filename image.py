from PIL import Image, ImageFilter

img = Image.open('./images/astro.jpg')

img.thumbnail((400, 200))
img.save('./thumbnail.jpg')
