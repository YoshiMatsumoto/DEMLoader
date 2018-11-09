import sys
import re
import math
import rhinoscriptsyntax as rs

def ReadPointsDef():
    filter = "csv file (*.csv)|*.csv|All Files (*.*)|*.*||"
    filename = rs.OpenFileName("Open Point File", filter)
    if not filename: return
    
    with open(filename, "r") as f:
        contents = f.readlines()

    points=[]
    for text in contents:
        items = text.strip("()\n").split(",")    
        if len(items)==3:
            x = float(items[0])
            y = float(items[1])
            z = float(items[2])
            rs.AddPoint(x,z,y)

    #contents = [__point_from_string(line) for line in contents]
    return points

if( __name__ == "__main__" ):
    ReadPointsDef()