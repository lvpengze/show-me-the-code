#! /usr/bin/python3
# coding=utf-8

__author__ = "lvpengze"


import re


def statistic_words(filename):
    file = open(filename, "r")
    text = file.read()

    words = re.findall(r"[\w\-\_\']+", text)

    print(len(words))
    print(words)

    return


if __name__ == "__main__":
    filename = "words"
    statistic_words(filename)
