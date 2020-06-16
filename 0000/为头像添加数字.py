from PIL import Image, ImageFont, ImageDraw
import sys

text = 'hello'

imagePath = './pic.jpg'

image = Image.open(imagePath)
width, height = image.size
font = ImageFont.truetype('font.otf', int(width/6))

draw = ImageDraw.Draw(image)
s_width, s_height = draw.textsize(text, font)
draw.text((width - s_width, 0), text, fill=(255,0,5), font = font)
image.save('numPic.jpg')
