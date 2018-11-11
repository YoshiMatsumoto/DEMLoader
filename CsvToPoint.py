import sys
import re
import math
import rhinoscriptsyntax as rs

def ReadPointsDef():
    crvList =[]
    filter = "csv file (*.csv)|*.csv|All Files (*.*)|*.*||"
    fileList = rs.OpenFileNames("Open Point File", filter)
    if not fileList: return
    for filename in fileList:
            with open(filename, "r") as f:
                contents = list(f.readlines())
                for text in contents:
                    pts = []
                    items = text.strip("()\n").split(",")    
                    if len(items)==3:
                        x = float(items[0])
                        y = float(items[1])
                        z = float(items[2])
                        pt = rs.AddPoint(x,z,y)
                        pts.append(pt)
                crvList = rs.AddInterpCurve(pts)
    return crvList

if( __name__ == "__main__" ):
    ReadPointsDef()