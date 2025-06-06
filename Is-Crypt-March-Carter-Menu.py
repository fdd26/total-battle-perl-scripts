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
# python.exe Is-Crypt-March-Carter-Menu.py
#
# OR double-click on Is-Crypt-March-Carter-Menu.py
#
# OPEN crypt-march-carter-menu.png to test, you should hear some beeps.
#
#####################################################################
#
# Original Python3 script forked from:
# https://github.com/TotalBattleBots/Exchange-Beep
#
#####################################################################

import winsound
import pyautogui as pag
import sys
import time
from python_imagesearch.imagesearch import imagesearch

# Merc frequency is set to 400Hz
freqMerc = 400

# duration is set to 100 milliseconds
dur = 500


# while loops
i = 1
notfound = 0
while i < 1800:
    # 25% resolution square image search
    pos = imagesearch("crypt-march-carter-menu.png")
    if pos[0] != -1:
        if len(sys.argv) > 1 and sys.argv[1] == '1':
            winsound.Beep(freqMerc, dur)

        print( str( pos ) )
        # Sleep a little before looping
        time.sleep(0.5)
        del pos
    else:
        i += 1
        notfound += 1
        print( "\n# Try again [" + str( i ) + "]\n" )

    if notfound > 5:
        print( "\n# Clear [" + str( i ) + "]\n" )
        exit( 0 )

print( "\n#BAD\n" )
exit( 1 )
