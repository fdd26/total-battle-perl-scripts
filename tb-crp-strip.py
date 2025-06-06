#!python

#pip install pyautogui pywin32 playsound

import pyautogui
import time
import subprocess
import random
from playsound import playsound

# Settings
NO_SOUND = True
PERL_WITH_SOUND   = not NO_SOUND
PYTHON_WITH_SOUND = not NO_SOUND

PYTHON3_PATH_EXE = r"C:\Progra~1\Python312\python.exe"  # Modify if needed

# Sound
def play_sound_system_start(state=None):
    if PERL_WITH_SOUND:
        if state is not None:
            print(f"Play State [{state}]")
        # Replace with actual WAV file if needed
        try:
            playsound("SystemStart.wav")
        except Exception as e:
            print(f"Error playing sound: {e}")

# Mouse functions
def move_mouse_cursor(x, y):
    print(f"\nMoving cursor to ({x}, {y})")
    pyautogui.moveTo(x, y)

def get_mouse_xy():
    x, y = pyautogui.position()
    print(f"Cursor is at: {x}, {y}")
    return x, y

def left_click():
    pyautogui.click(button='left')

def right_click():
    pyautogui.click(button='right')

# Coordinates (same as Perl)
full_telescope_mouse_xy        = (564, 730)
full_crypt_menu_mouse_xy       = (542, 435)
full_crypt_menu_third_mouse_xy = (975, 624)
full_crypt_middle_mouse_xy     = (773, 488)

# Run external Python script and parse output
def run_validation_script(script_name):
    try:
        output = subprocess.check_output([PYTHON3_PATH_EXE, script_name, str(PYTHON_WITH_SOUND)],
                                         stderr=subprocess.STDOUT, universal_newlines=True)
        print(output)
        if "#BAD" in output:
            return None
        import re
        match = re.search(r"\((\d+),\s*(\d+)\)", output)
        if match:
            x, y = int(match.group(1)), int(match.group(2))
            print(f"Found: ({x}, {y})")
            return (x, y)
    except subprocess.CalledProcessError as e:
        print(f"Script error: {e}")
    return None

# Main automation step (simplified)
def full_screen_state_machine(i=-1):
    dx = random.randint(-2, 2)
    dy = random.randint(-2, 2)

    # Move to telescope
    move_mouse_cursor(full_telescope_mouse_xy[0] + dx, full_telescope_mouse_xy[1] + dy)
    time.sleep(0.15)
    left_click()
    time.sleep(0.15)

    # Move to crypt menu
    move_mouse_cursor(full_crypt_menu_mouse_xy[0] + dx, full_crypt_menu_mouse_xy[1] + dy)
    time.sleep(0.15)
    left_click()
    time.sleep(0.15)

    pos = run_validation_script("Is-Crypt-Left-Menu.py")
    if pos is None:
        print("Crypt LEFT MENU not found")
        return 1

    # Move to first crypt
    move_mouse_cursor(full_crypt_menu_third_mouse_xy[0] + dx, full_crypt_menu_third_mouse_xy[1] + dy)
    time.sleep(0.15)
    left_click()

    # Enter crypt
    move_mouse_cursor(full_crypt_middle_mouse_xy[0] + dx, full_crypt_middle_mouse_xy[1] + dy)
    time.sleep(0.15)
    left_click()

    print("Crypt entered successfully.")
    return 0

# Main loop
def main():
    get_mouse_xy()
    print("Sleeping for 5 seconds before starting...")
    play_sound_system_start(1)
    time.sleep(5)

    for i in range(1, 100):
        print(f"[{i}] - Running automation step")
        result = full_screen_state_machine(i % 4)
        if result == 0:
            print(f"Success iteration {i}")
        else:
            print(f"Failure at iteration {i}")
            break
        play_sound_system_start(3)
        time.sleep(1)

    play_sound_system_start(4)

if __name__ == "__main__":
    main()
