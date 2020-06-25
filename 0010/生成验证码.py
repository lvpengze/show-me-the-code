#! /usr/bin/python3
# coding=utf-8

__author__ = "lvpengze"


import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def random_color_bk():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def random_color_text():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def random_char():
    return chr(random.randint(65, 90))


def generate_captcha(n):
    height = 60
    width = 60*n

    image = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype("font.otf", 36)
    draw = ImageDraw.Draw(image)

    #填充每个像素
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=random_color_bk())

    for i in range(n):
        char = random_char()
        draw.text((60 * i + 10, 10), char, font=font, fill=random_color_text())

    image = image.filter(ImageFilter.EDGE_ENHANCE)

    return image


if __name__ == "__main__":
    image = generate_captcha(4)
    image.save("captcha.jpg", "jpeg")
