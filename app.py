# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 18:50:35 2022

@author: DCT
"""

from flask import Flask

# 生成Flask的物件(主程式)
app = Flask(__name__)



@app.route("/")
def lcc():
    return "Hello LCC"

