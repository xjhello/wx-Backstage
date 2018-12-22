# -*- coding: utf-8 -*-
DEBUG = True
SQLALCHEMY_ECHO = True  # 将所有SQL语句打印出来
SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1/food_db?charset=utf8mb4'
# SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1/food_db'
# 'mysql+cymysql://root:123456@localhost:3306/fisher'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENCODING = "utf8mb4"  # 编码
RELEASE_VERSION = 2018813 # 版本号