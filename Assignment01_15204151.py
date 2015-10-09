# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 22:22:12 2015

@author: adedayoadelowokan
"""

import sqlite3 as lite
import math
import numpy as np

con = lite.connect('renewable.db')

#cur = con.cursor()
#cur.execute("SELECT * FROM ports;")
#cur.execute("SELECT * FROM location;")
#    
#for item in cur:
#    print item

def distance(x1, y1, x2, y2):
    x = (x2 - x1)**2
    y = (y2 - y1)**2
    xy = x + y
    dist = math.sqrt(xy)
    return dist

with con:
    
    #con.row_factory = lite.Row
    cur = con.cursor()
    
    cur.execute("SELECT * FROM ports;")    
    ports = cur.fetchall()

    cur.execute("SELECT * FROM location;")
    locations = cur.fetchall()    
    i = 0
    j = 0
    dista = np.zeros((3, 10))
    for port in ports:
        j = 0
        for location in locations:
            print "hu"
            dista[i][j] = distance(port[0], port[1], location[0], location[1])
            print "ja"
            j += 1
        i += 1