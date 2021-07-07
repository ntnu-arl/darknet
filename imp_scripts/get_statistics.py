import sys
import argparse
import os
import rospy
import string


if len(sys.argv) < 2:
    print "Failed, min required args :", "python get_statistics.py dir_name"
    sys.exit(0)

fname = sys.argv[1]


num_of_survivor = 0
num_of_fireex = 0
num_of_phone = 0
num_of_driller = 0
num_of_backpack = 0
num_of_vent = 0
num_of_helmet = 0
num_of_rope = 0



txtNames = []
file1 = open("statistics.txt","a") 


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

# print('\n', len(txtNames), '\n')

for i in txtNames: ## reformat elements in txtNames:

    txtFile = open(i, 'r')
    
    lines = txtFile.readlines()
    

    for k in lines:
        classs = k[0]
        if (classs == '0'):
            num_of_survivor = num_of_survivor + 1
        elif (classs == '1'):
            num_of_fireex = num_of_fireex + 1
        elif (classs == '2'):
            num_of_phone = num_of_phone + 1
        elif (classs == '3'):
            num_of_driller = num_of_driller + 1
        elif (classs == '4'):
            num_of_backpack = num_of_backpack + 1
        elif (classs == '5'):
            num_of_vent = num_of_vent + 1
        elif (classs == '6'):
            num_of_helmet = num_of_helmet + 1
        else:
            num_of_rope = num_of_rope + 1
        # Now we will append bounding box centers:
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

        xCoords.append(k[2:(counter - 2)])
        ystart = counter - 1
        # Get y coordinates:
        s = k[counter + 1]
        while (s != "."):
            counter = counter + 1
            s = k[counter]
        yCoords.append(k[ystart:(counter - 2)])
    
    # print(len(xCoords))
    # print(len(yCoords))




# file1.write('Number of survivor labels: ')
# file1.write(str(num_of_survivor))
# file1.write('\n')

# file1.write('Number of fireex labels: ')
# file1.write(str(num_of_fireex))
# file1.write('\n')

# file1.write('Number of phone labels: ')
# file1.write(str(num_of_phone))
# file1.write('\n')

# file1.write('Number of driller labels: ')
# file1.write(str(num_of_driller))
# file1.write('\n')

# file1.write('Number of backpack labels: ')
# file1.write(str(num_of_backpack))
# file1.write('\n')

print('Number of survivor labels: ', num_of_survivor, '\n')
print("Number of fireex labels: ", num_of_fireex, "\n")
print("Number of phone labels: ", num_of_phone, "\n")
print("Number of driller labels: ", num_of_driller, "\n")
print("Number of backpack labels: ", num_of_backpack, "\n")
print("Number of vent labels: ", num_of_vent, "\n")
print("Number of helmet labels: ", num_of_helmet, "\n")
print("Number of rope labels: ", num_of_rope, "\n")



