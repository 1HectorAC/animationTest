import math
import os
#-------Requirement 3-------- This is a module. It has variables like "color" and functions like "cosHelp" that are at module scope
outfile = 'temp.pov'
#-------Requirement 6-------- Here is the use of a tuple
color = ("Yellow","Blue","Red")

#help get cos with height of 2
def cosHelp(*nums, value=1, degree=1):
    return math.cos(value * degree * math.pi / 180 ) * -2

#help get sin with height of 2
def sinHelp(*num,value=1, degree=1):
    return math.sin(value * degree * math.pi / 180 ) * -2

#builds circle object string in pov format
def circlePovBuilder(x,y,z,size,color):
    return "sphere{" + "<" + str(x) + "," + str(y) + "," + str(z) + ">" + ","+str(size)+" pigment {" + color + "}}"

#build vector string with format
def vectorBuilder(x,y,z):
    return "<" + str(x) + "," + str(y) + "," + str(z) + ">"

#build a png
def makePNG(num):
    pov_cmd = 'pvengine.exe +I%s +O%s -D -V +A +H600 +W800 /exit'
    cmd = pov_cmd % ('temp.pov', "temp" + str(num).zfill(4) + ".png")
    os.system(cmd)
    
#writes over temp.pov file
def addToTemp(sdl):
    fout = open( outfile, 'w' ) 
    fout.write( sdl ) 
    fout.close()
        