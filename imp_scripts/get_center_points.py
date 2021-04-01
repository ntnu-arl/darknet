import sys
import argparse
import os
import rospy
import string
import random

import matplotlib.pyplot as plt
import numpy as np


if len(sys.argv) < 2:
    print "Failed, min required args :", "python get_center_points.py filename"
    sys.exit(0)

fname = sys.argv[1]

# Lists containg x coordinate for centers:
SurvivorCentersX = []
FireExCentersX = []
CellPhoneCentersX = []
DrillCentersX = []
BackPackCentersX = []
VentCentersX = []
HelmetCentersX = []
RopeCentersX = []
# Lists containg Y coordinate for centers:
SurvivorCentersY = []
FireExCentersY = []
CellPhoneCentersY = []
DrillCentersY = []
BackPackCentersY = []
VentCentersY = []
HelmetCentersY = []
RopeCentersY = []


txtNames = []

f1 = open("DataInformation/SurvivorCenters.txt","a") 
f2 = open("DataInformation/FireExCenters.txt","a") 
f3 = open("DataInformation/CellPhoneCenters.txt","a") 
f4 = open("DataInformation/DrillCenters.txt","a") 
f5 = open("DataInformation/BackPackCenters.txt","a") 
f6 = open("DataInformation/VentCenters.txt","a") 
f7 = open("DataInformation/HelmetCenters.txt","a") 
f8 = open("DataInformation/RopeCenters.txt","a") 

def WriteCentersToFile(fstream, Xlist, Ylist):
    i = 0
    while (i < len(Xlist)):
        fstream.write(str(Xlist[i]))
        fstream.write(", ")
        fstream.write(str(Ylist[i]))
        fstream.write("\n")
        i = i + 1


def PlotCenters(Xlist, Ylist, name):
    
    plt.scatter(Xlist, Ylist)


    # if (name == 'Rope'):
    #     for i in range (len(Xlist)):
    #         Xlist[i] = Xlist[i] + random.uniform(-0.02, 0.02)
    #         Ylist[i] = Ylist[i] + random.uniform(-0.02, 0.02)
    #     plt.scatter(Xlist, Ylist)


    plt.axis([0, 1, 0, 1])
    
    # giving a title to the graph 
    plt.title(name) 
    plt.savefig('DataInformation/' + name + '_centers.png')
    # plt.show()

if os.path.isfile(fname):
    l = len(fname)
    print (fname[l - 4:])
    if (fname[l - 4:] == '.txt'):
        txtNames.append(fname)
elif os.path.exists(fname):
    for root, dirs, files in os.walk(fname):
        ImageFiles = sorted(files)
        for fn in ImageFiles:
            l = len(fn)
            if (fn[l - 4:] == '.txt'):
                txtNames.append(os.path.join(root, fn))
else:
    print("Neither a txt file nor a folder: {0}".format(fname))
    sys.exit(0)

if (len(txtNames) == 0):
    print("Could not find any txt's")
    sys.exit(0)

xCoords = []
yCoords = []

for i in txtNames: ## reformat elements in txtNames:

    txtFile = open(i, 'r')
    
    lines = txtFile.readlines()

    # Now we will append bounding box centers:
        
    

    for k in lines:

        counter = 0
        s = k[counter]
        # Get x coordinates:
        numOfDots = 0
        while (numOfDots != 2):
            while (s != "."):
                counter = counter + 1
                s = k[counter]
            numOfDots = numOfDots + 1
            s = k[counter + 1]

        xcoord = k[2:(counter - 2)]
        
        ystart = counter - 1
        # Get y coordinates:
        s = k[counter + 1]
        while (s != "."):
            counter = counter + 1
            s = k[counter]
        
        ycoord = k[ystart:(counter - 2)]


        classs = k[0]
        if (classs == '0'):
            SurvivorCentersX.append(float(xcoord))
            SurvivorCentersY.append(1 - float(ycoord))
        elif (classs == '1'):
            FireExCentersX.append(float(xcoord))
            FireExCentersY.append(1 - float(ycoord))
        elif (classs == '2'):
            CellPhoneCentersX.append(float(xcoord))
            CellPhoneCentersY.append(1 - float(ycoord))
        elif (classs == '3'):
            DrillCentersX.append(float(xcoord))
            DrillCentersY.append(1 - float(ycoord))
        elif (classs == '4'):
            BackPackCentersX.append(float(xcoord))
            BackPackCentersY.append(1 - float(ycoord))
        elif (classs == '5'):
            VentCentersX.append(float(xcoord))
            VentCentersY.append(1 - float(ycoord))
        elif (classs == '6'):
            HelmetCentersX.append(float(xcoord))
            HelmetCentersY.append(1 - float(ycoord))
        elif (classs == '7'):
            RopeCentersX.append(float(xcoord))
            RopeCentersY.append(1 - float(ycoord))


WriteCentersToFile(f8, RopeCentersX, RopeCentersY)
WriteCentersToFile(f7, HelmetCentersX, HelmetCentersY)
WriteCentersToFile(f6, VentCentersX, VentCentersY)
WriteCentersToFile(f5, BackPackCentersX, BackPackCentersY)
WriteCentersToFile(f4, DrillCentersX, DrillCentersY)
WriteCentersToFile(f3, CellPhoneCentersX, CellPhoneCentersY)
WriteCentersToFile(f2, FireExCentersX, FireExCentersY)
WriteCentersToFile(f1, SurvivorCentersX, SurvivorCentersY)

PlotCenters(RopeCentersX, RopeCentersY, "Rope")
PlotCenters(HelmetCentersX, HelmetCentersY, "Helmet")
PlotCenters(VentCentersX, VentCentersY, "Vent")
PlotCenters(BackPackCentersX, BackPackCentersY, "Backpack")
PlotCenters(SurvivorCentersX, SurvivorCentersY, "Survivor")
PlotCenters(DrillCentersX, DrillCentersY, "Drill")
PlotCenters(CellPhoneCentersX, CellPhoneCentersY, "Cell Phone")
PlotCenters(FireExCentersX, FireExCentersY, "Fire Extinguisher")

