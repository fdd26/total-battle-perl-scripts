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
# python.exe Is-Monster-Common-25-Flag.py
#
# OR double-click on Is-Monster-Common-25-Flag.py
#
# OPEN common-monster-25b.png to test, you should hear some beeps.
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
#from python_imagesearch.imagesearch import imagesearch

# https://github.com/drov0/python-imagesearch/blob/master/full_examples.py
from python_imagesearch.imagesearch import *

# Merc frequency is set to 600Hz
freqMerc = 600

# duration is set to 100 milliseconds
dur = 500

x0 = 0
y0 = 0
# 773 488
#pos = imagesearcharea("./common-monster-25.png", 540, 440, 820, 600)
#x0 = 600
#y0 = 480
#pos = imagesearcharea("./common-monster-25b.png", x0, y0, 820, 600)

pos = imagesearch("./common-monster-25b.png")
if pos[0] != -1:
    x = x0 + pos[0]
    y = y0 + pos[1]
    print("position : ", x, y)
    pyautogui.moveTo(x, y)
else:
    print("image not found")

