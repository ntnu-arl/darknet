import sys
import argparse
import os
import rospy
import string


if len(sys.argv) < 2:
    print "Failed, min required args :", "python get_statistics.py <input_dir>"
    sys.exit(0)

fname = sys.argv[1]
txtNames = []

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


for i in txtNames: 

    
    with open(i, "r+") as txtFile:

        line = txtFile.readlines() ## In the case of the vent data there's only one line per image label (only vent).
        # txtFile.seek(0)
        numSpaces = 0
        charIndex = 0
        for char in line[0]:
            if (char == " "):
                numSpaces+=1
                if (numSpaces == 3):
                    break
            # print('updating')
            charIndex+=1
    
        newLine = line[0][charIndex+1:]
        i=0
        for char in newLine:
            i+=1
            if (char == " "):
                break

        width = newLine[0:i-1] 
        height = newLine[i:]   

        NewWidth = float(width) * 0.75
        NewHeight = float(height) * 0.75

        NewWidth = str(NewWidth)
        NewHeight = str(NewHeight)

        newLine = line[0][0:charIndex] + " " + NewWidth + " " + NewHeight
        print(newLine)

        txtFile.seek(0)
        txtFile.truncate()
        txtFile.write(newLine)
        
