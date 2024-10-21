#!python3

#####################################################################
#
# Works with Python 3.12+
#
# Tested successfully on Windows Desktop
#
#
# GO HERE:
# https://www.python.org/downloads/
#
# DOWNLOAD THIS:
# https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe
#
# [x] Install Python3 for all users
# [x] Add Python3 to your PATH environment
#
# DOWNLOAD THIS:
# https://codeload.github.com/fdd26/Exchange-Beep/zip/refs/heads/main?file=Exchange-Beep-main.zip
#
# Extract it
#
# OPEN cmd.exe in that folder
#
# TYPE THIS to install Python3 dependencies:
# pip3 install pyautogui
# pip3 install python_imagesearch
#
# TYPE THIS to run the program
# python.exe Is-Crypt-Gray-Title.py
#
# OR double-click on Is-Crypt-Gray-Title.py
#
# OPEN crypt-gray-title.png to test, you should hear some beeps.
#
#####################################################################
#
# Original Python3 script forked from:
# https://github.com/TotalBattleBots/Exchange-Beep
#
#####################################################################

import winsound
import pyautogui as pag
import time
from python_imagesearch.imagesearch import *

# Merc frequency is set to 500Hz
freqMerc = 500

# Gold frequency is set to 800Hz
freqGold = 800

# duration is set to 100 milliseconds
dur = 500

# List of images
# "common-crypt-25-flag1.png", "common-crypt-25-flag2.png",
images_to_search = ["common-crypt-adamant.png", "common-crypt-cogwheel.png", "common-crypt-dragon-scale.png", "common-crypt-hide.png", "common-crypt-hydra.png", "common-crypt-iron-shard.png", "common-crypt-leather.png", "common-crypt-magma.png", "common-crypt-runic.png", "common-crypt-silk.png", "common-crypt-sirens.png", "common-crypt-thorium1.png", "common-crypt-thorium2.png"]

# while loops
i = 1
xpos   = [-1, -1]
ximage = ""
while i < 2:
    for image in images_to_search:
        pos = imagesearch(image)
        if pos[0] != -1:
            if "crypt" in image:
                winsound.Beep(freqMerc, dur)
                print( image )
                print( pos )
                xpos = pos
                ximage = image
                del pos

    # Sleep a little before looping
    time.sleep(0.05)

    i += 1
    print( "\n# Try again [" + str( i ) + "]\n" )


if xpos[0] != -1:
    print( xpos )
    print( ximage );
    del xpos
    del ximage
    exit( 0 )

print( "\n#BAD\n" )
exit( 1 )
