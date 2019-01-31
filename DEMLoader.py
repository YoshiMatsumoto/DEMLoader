import sys
import re
import math
import rhinoscriptsyntax as rs


def ImportXML():
    #prompt the user for a file to import
    filter = "xml file (*.xml)|*.xml|All Files (*.*)|*.*||"
    filename = rs.OpenFileName("Open Point File", filter)
    if not filename: return
    
    with open(filename, "r") as f:
        #mesh
        r = re.compile("<mesh>(.+)</mesh>")
        for ln in f:
            m = r.search(ln)
            if m != None:
                mesh = m.group(1)
                break

        # Corner
        r = re.compile("<gml:lowerCorner>(.+) (.+)</gml:lowerCorner>")
        for ln in f:
            m = r.search(ln)
            if m != None:
                xlower = float(m.group(1))
                ylower = float(m.group(2))
                break

        # grid len
        r = re.compile("<gml:high>(.+) (.+)</gml:high>")
        for ln in f:
            m = r.search(ln)
            if m != None:
                xlen = int(m.group(1)) + 1
                ylen = int(m.group(2)) + 1
                break

        # start
        r = re.compile("<gml:tupleList>")
        for ln in f:
            m = r.search(ln)
            if m != None:
                break

        # data
        z_point = []
        r  = re.compile("</gml:tupleList>")
        r2 = re.compile(",(.+)")
        for ln in f:
            m = r.search(ln)
            if m != None:
                break
            else:
                m = r2.search(ln)
                if m != None:
                    z_point.append(float(m.group(1)))

        # start point
        startx = starty = 0
        r = re.compile("<gml:startPoint>(.+) (.+)</gml:startPoint>")
        for ln in f:
            m = r.search(ln)
            if m != None:
                startx = int(m.group(1))
                starty = int(m.group(2))
                break

    ##Create Matrix
    data2 = [i for i in range(xlen*ylen)]
    start_pos = starty*xlen + startx
    for i in range(xlen*ylen):
        if i < start_pos:
            data2[i] = -9999.
        else:
            data2[i] = z_point[i-start_pos]
    
    z_point = [0 if i == -9999 else i for i in z_point]

    #radius in Earth
    r = 6378150
    
    long = (2*math.pi*r/ (360 * 60 * 60))*0.2
    lat = (r* math.cos(xlower/180*math.pi)*2*math.pi/(360*60*60))*0.2

    x_point = []
    for i in range(xlen):
        x = [(xlen - i)*lat for i in range(xlen)]
        x_point.extend(x)
    x_point.reverse()
        
    y_point = []
    for i in range(ylen):
        y_ini = [i*long for _ in range(xlen)]
        y_point.extend(y_ini)
    y_point.reverse()

    points = []
    for i in range(xlen*ylen):
        points.append(rs.AddPoint(x_point[i], y_point[i], z_point[i]))


if( __name__ == "__main__" ):
    ImportXML()