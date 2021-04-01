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
        lines = txtFile.readlines()
        txtFile.seek(0)
        for line in lines:
            if (line[0] == '5'):
                linelist = list(line)
                linelist[0] = '6'
                linestring = ''.join(linelist)
                txtFile.write(linestring)
            else:
                txtFile.write(line)
        txtFile.truncate()
