import re
import os
import animateHelp
class Sphere:
    #--------Requirement 5-------- maxFrames is like a static variable (class variable) in a class
    maxFrames = 400
    #-------Requirement 5----- Here is a contructor in a class
    def __init__(self, color, x, y, z, size):
        #-------Requirement 5-------- The variables below are instance variables in a class
        self.color = color
        self.x = x
        self.y = y
        self.z = z
        self.size = size
        #-------Requirement 6-------- Here is the use of a list
        self.animateFrame = [animateHelp.circlePovBuilder(self.x,self.y,self.z,self.size,self.color)]
        self.FrameIndex = 1
        
    #--------Requirement 5-------- The methods below are instance methods in a class 
    #loop circle around the center
    def circleAround(self, loops):
        for i in range(loops):
            #--------Requirement 7-------- a function or method with keyword arguments is called below
            self.x = animateHelp.sinHelp(value=i,degree=4)
            self.z = animateHelp.cosHelp(value=i,degree=4)
            self.animateFrame.append(animateHelp.circlePovBuilder(self.x,self.y,self.z,self.size,self.color))
            self.FrameIndex += 1 
        self.FrameLimitCheck()
        
    #expand size of cicle
    def expand(self,amount):
        for i in range(amount):
            self.size = self.size + .01
            self.animateFrame.append(animateHelp.circlePovBuilder(self.x,self.y,self.z,self.size,self.color))
            self.FrameIndex += 1
        self.FrameLimitCheck()
            
    #contrast size of cicle
    def contrast(self,amount):
        for i in range(amount):
            self.size = self.size - .01
            self.animateFrame.append(animateHelp.circlePovBuilder(self.x,self.y,self.z,self.size,self.color))
            self.FrameIndex += 1
        self.FrameLimitCheck()
            
    #expand then contrast cicle
    def expandThenContrast(self,amount):
        self.expand(int(amount/2))
        self.contrast(int(amount/2))
        
    #cicle will do nothing
    def stillFrame(self, amount):
        for i in range(amount):
            self.animateFrame.append(animateHelp.circlePovBuilder(self.x,self.y,self.z,self.size,self.color))
            self.FrameIndex += 1
        self.FrameLimitCheck()
            
    #print cicle frames
    def printFrames(self):
        for i in range(self.FrameIndex-1):
            print(self.animateFrame[i])
          
    #check if circle has more frames than is allowed
    def FrameLimitCheck(self):
        if self.FrameIndex > Sphere.maxFrames:
            print("Warning. Excceding frame limit")
            
#--------------------------------------------------main----------------------------------------------
#read base.pov file into sdl
fin = open('base.pov') 
sdl = fin.read() 
fin.close() 

#-----Requirement 4----- Sphere objects was created using the Sphere class. It is also a key feature in the program since most of the program involves using it.
Sp1 = Sphere(animateHelp.color[0] ,0,-.75,-2,.25)
Sp2 = Sphere(animateHelp.color[1],0,0,-2,.25)
Sp3 = Sphere(animateHelp.color[2],0,.75,-2,.25)

#add cicle objects to base.pov file
sdl = sdl +"\n"+ Sp1.animateFrame[0] +"\n"+ Sp2.animateFrame[0] +"\n"+ Sp3.animateFrame[0]

#setup frames for circle objects
Sp1.circleAround(90)
Sp2.expandThenContrast(44)
Sp2.expandThenContrast(46)
Sp3.circleAround(90)

Sp1.expandThenContrast(44)
Sp1.expandThenContrast(46)
Sp2.circleAround(90)
Sp3.expandThenContrast(44)
Sp3.expandThenContrast(46)

Sp1.stillFrame(10)
Sp2.stillFrame(10)
Sp3.stillFrame(10)

Sp1.circleAround(90)
Sp2.stillFrame(15)
Sp3.stillFrame(15)

Sp1.stillFrame(15)
Sp2.circleAround(90)
Sp3.stillFrame(15)

Sp1.stillFrame(15)
Sp2.stillFrame(15)
Sp3.circleAround(90)

Sp1.expand(25)
Sp2.expand(25)
Sp3.expand(25)

#animation sequence to make pngs with cicle objects
for i in range(335):
    #-----Requirement 2----- sdl is the read in file. The next part then checks sdl for the circle object frame with "search" and then replaces it in sdl.
    #-------Requirement 6-------- Here is the use of a dictionary
    check = {"one":re.search(Sp1.animateFrame[i],sdl) ,"two":re.search(Sp2.animateFrame[i],sdl) ,"three":re.search(Sp3.animateFrame[i],sdl)}

    #error check in case can't replace circle object in sdl
    if check["one"] and check["two"] and check["three"]:
        #replace old string with new in sdl
        sdl = re.sub(Sp1.animateFrame[i], Sp1.animateFrame[i+1],sdl)
        sdl = re.sub(Sp2.animateFrame[i], Sp2.animateFrame[i+1],sdl)
        sdl = re.sub(Sp3.animateFrame[i], Sp3.animateFrame[i+1],sdl)
        
        #write new sdl to temp.pov
        animateHelp.addToTemp(sdl);
        
        #make png from tmp.pov file
        animateHelp.makePNG(i)
    else:
        print("-----------Error(cant add next animation Frame)-------------")

#encode
print ('Encoding movie')
os.system('mencoder.exe mf://temp*.png -mf type=png:fps=25 -ovc lavc -lavcopts vcodec=msmpeg4:vbitrate=2160000:keyint=5:vhq -o movie2.avi ' )