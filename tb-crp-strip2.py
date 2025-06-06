#!python

# pip install pyautogui pywin32 simpleaudio
#pip install pyautogui pywin32 playsound

import pyautogui
import subprocess
import random
import time
import re
import ctypes
#from playsound import playsound
import simpleaudio

# Constants for mouse events
MOUSEEVENTF_LEFTDOWN  = 0x02
MOUSEEVENTF_LEFTUP    = 0x04
MOUSEEVENTF_RIGHTDOWN = 0x08
MOUSEEVENTF_RIGHTUP   = 0x10

# Optional sound flags
NO_SOUND          = True
PERL_WITH_SOUND   = not NO_SOUND
PYTHON_WITH_SOUND = not NO_SOUND

PYTHON3_PATH_EXE  = r"C:\Progra~1\Python312\python.exe"

# Mouse swing deltas (disabled by default)
mouse_delta_x_swing = 0
mouse_delta_y_swing = 0

def playsound(wav)
    # Load and play the WAV file
    wave_obj = simpleaudio.WaveObject.from_wave_file(wav)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until sound finishes playing


# Mouse click using ctypes (Windows API)
def mouse_event(flags, x, y, data=0, extra=0):
    ctypes.windll.user32.mouse_event(flags, x, y, data, extra)

def move_mouse_cursor(x, y):
    print(f"Moving mouse to: ({x}, {y})")
    pyautogui.moveTo(x, y)

def get_mouse_xy():
    x, y = pyautogui.position()
    print(f"Cursor is at: ({x}, {y})")
    return x, y

def send_left_click(x, y):
    mouse_event(MOUSEEVENTF_LEFTDOWN | MOUSEEVENTF_LEFTUP, x, y)

def send_right_click(x, y):
    mouse_event(MOUSEEVENTF_RIGHTDOWN | MOUSEEVENTF_RIGHTUP, x, y)

def play_sound(state=None):
    if PERL_WITH_SOUND:
        print(f"Play Sound State: {state}")
        try:
            playsound("SystemStart.wav")
        except Exception as e:
            print(f"Sound error: {e}")

# Run a Python script and parse coordinate output
def run_validation_script(script):
    try:
        result = subprocess.check_output([PYTHON3_PATH_EXE, script, str(int(PYTHON_WITH_SOUND))], universal_newlines=True)
        print(f"[{script}] Output:\n{result}")
        if '#BAD' in result:
            return None
        match = re.search(r'\((\d+)[, ]+(\d+)\)', result)
        if match:
            return int(match.group(1)), int(match.group(2))
    except subprocess.CalledProcessError as e:
        print(f"Script error [{script}]: {e}")
    return None

# Coordinate definitions (converted from Perl arrays)
full_telescope_mouse_xy                   = (564, 730)
full_crypt_menu_mouse_xy                  = (542, 435)
full_crypt_menu_first_mouse_xy            = (975, 464)
full_crypt_menu_second_mouse_xy           = (975, 544)
full_crypt_menu_third_mouse_xy            = (975, 624)
full_crypt_menu_fourth_mouse_xy           = (975, 699)
full_crypt_middle_mouse_xy                = (773, 488)
full_crypt_middle_mouse_lower_xy          = (970, 604)
full_crypt_explore_right_mouse_xy         = (916, 686)
full_crypt_misclick_top_menu_mouse_xy     = (995, 348)
full_crypt_speedup_top_menu_mouse_xy      = (995, 200)
full_crypt_speedup_first_mouse_xy         = (899, 430)
full_crypt_speedup_second_mouse_xy        = (899, 517)
full_crypt_speedup_third_mouse_xy         = (899, 606)
full_crypt_speedup_close_mouse_xy         = (984, 284)

# Full screen state machine, main automation logic
def full_screen_state_machine(i=-1, skip=0):
    if i >= 0:
        if i == 1:
            crypt_first_mouse = full_crypt_menu_second_mouse_xy
        elif i == 2:
            crypt_first_mouse = full_crypt_menu_third_mouse_xy
        elif i == 3:
            crypt_first_mouse = full_crypt_menu_fourth_mouse_xy
        else:
            crypt_first_mouse = full_crypt_menu_first_mouse_xy
    else:
        crypt_first_mouse = full_crypt_menu_third_mouse_xy

    dx = random.randint(-mouse_delta_x_swing, mouse_delta_x_swing)
    dy = random.randint(-mouse_delta_y_swing, mouse_delta_y_swing)

    # Delays
    dw          = 0.15 + random.random() * 0.10
    wait_click  = 0.06 + random.random() * 0.05
    wait_screen = 0.80 + random.random() * 0.10
    wait_crypt  = 28.0 + random.random() * 2.00

    if skip < 1:
        # Telescope click
        move_mouse_cursor(full_telescope_mouse_xy[0] + dx, full_telescope_mouse_xy[1] + dy)
        time.sleep(dw)
        send_left_click(0, 0)
        time.sleep(wait_click + wait_screen)

        # Crypt menu click
        move_mouse_cursor(full_crypt_menu_mouse_xy[0] + dx, full_crypt_menu_mouse_xy[1] + dy)
        time.sleep(dw)
        send_left_click(0, 0)
        time.sleep(wait_click + wait_screen)

        # Validate left menu
        if not run_validation_script("Is-Crypt-Left-Menu.py"):
            print("Crypt LEFT MENU not found")
            return 1

        # Select crypt
        move_mouse_cursor(crypt_first_mouse[0] + dx, crypt_first_mouse[1] + dy)
        time.sleep(dw)
        send_left_click(0, 0)
        time.sleep(wait_click + wait_screen)

        # Confirm middle entry
        move_mouse_cursor(full_crypt_middle_mouse_xy[0] + dx, full_crypt_middle_mouse_xy[1] + dy)
        time.sleep(dw)
        send_left_click(0, 0)
        time.sleep(wait_click + wait_screen)
    else:
        crypt_pos = run_validation_script("crypt-search.py")
        if crypt_pos is None:
            print("No crypt found")
            return 3
        move_mouse_cursor(crypt_pos[0] + dx, crypt_pos[1] + dy)
        time.sleep(dw)
        send_left_click(0, 0)
        time.sleep(wait_click + wait_screen)

    # Gray title check
    if not run_validation_script("Is-Crypt-Gray-Title.py"):
        # Try green misclick title instead
        green_pos = run_validation_script("Is-Crypt-Green-Misclick-Title.py")
        if not green_pos:
            return 21
        move_mouse_cursor(full_crypt_misclick_top_menu_mouse_xy[0] + dx, full_crypt_misclick_top_menu_mouse_xy[1] + dy)
        time.sleep(dw)
        send_left_click(0, 0)
        time.sleep(wait_click + wait_screen)

        if not run_validation_script("Is-Crypt-Green-Misclick-Title.py"):
            move_mouse_cursor(full_crypt_middle_mouse_lower_xy[0] + dx, full_crypt_middle_mouse_lower_xy[1] + dy)
            time.sleep(dw)
            send_left_click(0, 0)
            time.sleep(wait_click + wait_screen)
            if not run_validation_script("Is-Crypt-Gray-Title.py"):
                return 23
        else:
            return 22

    # Explore crypt
    move_mouse_cursor(full_crypt_explore_right_mouse_xy[0] + dx, full_crypt_explore_right_mouse_xy[1] + dy)
    time.sleep(dw)
    send_left_click(0, 0)
    time.sleep(wait_click + wait_screen)

    # Open speedup
    move_mouse_cursor(full_crypt_speedup_top_menu_mouse_xy[0] + dx, full_crypt_speedup_top_menu_mouse_xy[1] + dy)
    time.sleep(dw)
    send_left_click(0, 0)
    time.sleep(wait_click + wait_screen)

    # Validate speedup title
    if not run_validation_script("Is-Crypt-Green-Speedup-Title.py"):
        return 3

    # Perform speedup clicks
    for _ in range(6):
        move_mouse_cursor(full_crypt_speedup_second_mouse_xy[0] + dx, full_crypt_speedup_second_mouse_xy[1] + dy)
        send_left_click(0, 0)
        time.sleep(wait_click)

    play_sound(8)

    # Close speedup
    move_mouse_cursor(full_crypt_speedup_close_mouse_xy[0] + dx, full_crypt_speedup_close_mouse_xy[1] + dy)
    time.sleep(dw)
    send_left_click(0, 0)
    time.sleep(wait_click + wait_screen)

    play_sound(9)
    time.sleep(wait_crypt)
    play_sound(10)

    return 0

# Main control loop
def main():
    get_mouse_xy()
    print("Starting automation in 5 seconds...")
    play_sound(1)
    time.sleep(5)

    max_loops = 10000
    retry = 0
    good  = 0
