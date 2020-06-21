#! /usr/bin/python3
# coding=utf-8

__author__ = "lvpengze"

import glob
import re

def statistic_word_frequency(words_list):
    word_frequency = dict()

    for word in words_list:
        if word not in ["a", "an", "the"]:
            if word not in word_frequency:
                word_frequency[word] = 1
            else:
                word_frequency[word] += 1
    
    return word_frequency

def article_analysis(filename):
    file = open(filename,"r")
    words_list = re.findall(r"[\w\-\_\']+", file.read())

    word_frequency = sorted(statistic_word_frequency(words_list).items(), key=lambda t:t[1], reverse=True)

    print(filename)
    print("出现频次最多的单词：", word_frequency[0])
    print("出现频次最少的单词：", word_frequency[-1])


if __name__ == "__main__":
    files = glob.glob(r"*.txt")
    for file in files:
        article_analysis(file)
