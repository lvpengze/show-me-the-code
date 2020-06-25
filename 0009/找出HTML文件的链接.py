#! /usr/bin/python3
# coding=utf-8

__author__ = "lvpengze"

from bs4 import BeautifulSoup


def get_text(html):
    soup = BeautifulSoup(html, "html.parser")

    for item in soup.find_all("a"):
        print(item.get("href"))


if __name__ == "__main__":
    html = open("index.html", "r").read()

    get_text(html)
