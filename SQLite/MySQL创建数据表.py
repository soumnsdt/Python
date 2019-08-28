# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:DT

import pymysql

db = pymysql.connect("localhost", "root", "19950716dt", "mrsoft")
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS books")
sql = """
CREATE TABLE books(
    id int(8) NOT NULL AUTO_INCREMENT,
    name varchar(50) NOT NULL,
    category varchar(50) NOT NULL,
    price decimal(10,2) DEFAULT NULL,
    publish_time date DEFAULT NULL,
    PRIMARY KEY (id)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
"""
cursor.execute(sql)

db.close()


