#!/usr/bin/env python

import sys
import argparse
import os
import rospy
import rosbag
import time
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

# How to use: 
# a) Extract images from a bag: python extract_image_from_bag.py <bagfile> <save_folder>
# b) Extract images from all bags in a folder: python extract_image_from_bag.py <bagfolder> <save_folder>

# Change the list of image topic to extract
img_topics_list = ['/cam0/cam0']
# Choose how many frames to skip
SKIP_N_FRAME = 2

if len(sys.argv) < 3:
    print "Failed, min required args :", "python bag_to_image.py <bagfile> <save_folder>"
    sys.exit(0)

fname = sys.argv[1]
fsave = sys.argv[2]

inbags = []
if os.path.isfile(fname):
    l = len(fname)
    print (fname[l - 4:])
    if (fname[l - 4:] == '.bag'):
        inbags.append(fname)
elif os.path.exists(fname):
    for root, dirs, files in os.walk(fname):
        bagfiles = sorted(files)
        for fn in bagfiles:
            l = len(fn)
            if (fn[l - 4:] == '.bag'):
                inbags.append(os.path.join(root, fn))
else:
    print("Neither a bag file nor a folder: {0}".format(fname))
    sys.exit(0)

if (len(inbags) == 0):
    print("Could not find any rosbags")
    sys.exit(0)

if not os.path.exists(fsave):
    print("Save folder not exist: {0}".format(fsave))
    sys.exit(0)
if (fsave[len(fsave) - 1] != '/'):
    fsave = fsave + '/'

count = 1
skip_count = 1
for inbag in inbags:
    print("Loading bag: {0}".format(inbag))
    for topic, msg, t in rosbag.Bag(inbag).read_messages(topics=img_topics_list):
        skip_count = skip_count + 1
        if (skip_count >= SKIP_N_FRAME):
            cv_image = CvBridge().imgmsg_to_cv2(msg, "bgr8")
            cv2.imwrite(fsave + '{0:04d}'.format(count) + '.jpg',
                        cv_image)  # should save to jpg to save memory, can save to png if want to keep high quality
            skip_count = 0
            count = count + 1
