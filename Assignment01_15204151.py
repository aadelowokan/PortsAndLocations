# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 22:22:12 2015

@author: adedayoadelowokan
"""

import sqlite3 as lite
import math
import numpy as np

con = lite.connect('renewable.db')

def distance(x1, y1, x2, y2):
    x = (x2 - x1)**2
    y = (y2 - y1)**2
    xy = x + y
    dist = math.sqrt(xy)
    return dist

with con:
    
    cur = con.cursor()
    
    cur.execute("SELECT * FROM ports;")    
    ports = cur.fetchall()
    cur.execute("SELECT * FROM location;")
    locations = cur.fetchall()
    
    i = 0
    j = 0
    dista = np.zeros((10, 4))
    for location in locations:
        j = 0
        for port in ports:
            dista[i][j] = distance(location[0], location[1], port[0], port[1])
            j += 1
        dista[i][3] = location[2]
        i += 1
    
    i = 0
    for location in locations:
        print dista[i,:].min(), " ", dista[i, 3]
        i += 1
    
    i = 0
    array = np.zeros(10)
    for row in dista:
        array[i] = dista[i, 3]/dista[i,:].min()
        i+=1
        
    print "Location number ", array.argmax()

    i = 0
    for x in range(3):
        if(dista[array.argmax(), i] == dista[array.argmax(),:].min()):
            print "Port number ", i
        i += 1
    
con.close()