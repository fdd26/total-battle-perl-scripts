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
from python_imagesearch.imagesearch import imagesearch

# Merc frequency is set to 600Hz
freqMerc = 600

# duration is set to 100 milliseconds
dur = 500


# while loops
i = 1
while i < 10:
    # 25% resolution square image search
    pos = imagesearch("crypt-gray-title.png")
    if pos[0] != -1:
        winsound.Beep(freqMerc, dur)
        print( pos )
        del pos
        exit( 0 )

    # 25% resolution square image search
    pos = imagesearch("tartaros-crypt-gray-title.png")
    if pos[0] != -1:
        winsound.Beep(freqMerc, dur)
        print( pos )
        del pos
        exit( 0 )

    # Sleep a little before looping
    time.sleep(0.05)

    i += 1
    print( "\n# Try again [" + str( i ) + "]\n" )

print( "\n#BAD\n" )
exit( 1 )
