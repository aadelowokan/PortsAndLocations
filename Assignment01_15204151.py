# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 22:22:12 2015

@author: adedayoadelowokan
"""

import sqlite3 as lite

con = lite.connect('renewable.db')

#cur = con.cursor()
#cur.execute("SELECT * FROM ports;")
#cur.execute("SELECT * FROM location;")
#    
#for item in cur:
#    print item

with con:
    
    #con.row_factory = lite.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM ports;")
    
    rows = cur.fetchall()
    
    for row in rows:
        print row