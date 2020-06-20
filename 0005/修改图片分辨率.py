#! /usr/bin/python3
# coding=utf-8

__author__ = "lvpengze"

import os
import glob
from PIL import Image

iPhone5_width = 1136
iPhone5_height = 640

# PIL 的 thumbnail方法：用来等比例缩小图片
# PIL 的 resize方法：调整图片大小，可放大，可缩小

def thumbnail_pic(path):
    pic_files = glob.glob(path + "*.jpg")
    print(pic_files)
    for file in pic_files:
        image = Image.open(file)
        image.thumbnail((iPhone5_width, iPhone5_height))
        image.save("output/" + os.path.basename(file), "JPEG")

if __name__ == "__main__":
    path = "images/"
    thumbnail_pic(path)
