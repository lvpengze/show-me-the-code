#! /usr/bin/python3
# coding=utf-8

__author__ = "lvpengze"

import pymysql


def write_to_mysql(filename):
    db = pymysql.connect(
        host="localhost",
        port=3306,
        user="lvpengze",
        password="654353",
        database="test")
    cursor = db.cursor()

    # create table
    try:
        sql = "create table if not exists active_code(code char(8), primary key(code));"
        cursor.execute(sql)
    except:
        print("table create error")

    # insert data
    file = open(filename, "r")

    line_list = []
    while True:
        line = file.readline()
        if line == "":
            break
        line_list.append(line)
    try:
        cursor.executemany("insert into active_code values(%s)", line_list)
        db.commit()
    except:
        print("insert error")
    
    cursor.close()
    db.close()


if __name__ == '__main__':
    filename = "/root/Code/show-me-the-code/0002/active_code"
    write_to_mysql(filename)
