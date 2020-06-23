#! /usr/bin/python3
# coding=utf-8

__author__ = "lvpengze"

import os
import re


def file_analysis(path, ext):
    file_list = os.listdir(path)

    directories = []
    for file in file_list:
        filepath = os.path.join(path, file)
        if os.path.isdir(filepath):
            directories.append(filepath)
        else:
            _, fileext = os.path.splitext(filepath)
            if fileext == ext:
                statistic_code(filepath)

    for dir in directories:
        file_analysis(dir, ext)


def statistic_code(filepath):
    print(filepath)

    #总行数，代码行数，单行注释数，空行数
    num = [0, 0, 0, 0]

    lines = open(filepath, "r").readlines()
    num[0] = len(lines)
    for l in lines:
        if re.match("^[\s]*#", l) == None:
            pass
        else:
            num[2] += 1

    num[3] = lines.count("\n")
    num[1] = num[0] - num[2] - num[3]

    print("总行数: %d 代码行数: %d 单行注释数: %d 空行数: %d" %
          (num[0], num[1], num[2], num[3]))


if __name__ == "__main__":
    path = "/root/Code/show-me-the-code/0000"
    ext = ".py"
    file_analysis(path, ext)
