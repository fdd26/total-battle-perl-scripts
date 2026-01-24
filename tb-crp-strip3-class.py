#!/usr/bin/env python3
"""
Total Battle - Mouse Click Automation for 1536x864 Chrome browser with bookmark tab offset
Converted from Perl to Python3
"""

import sys
import time
import random
import subprocess
from datetime import datetime
from ctypes import windll, Structure, c_long, byref

# Mouse event constants
MOUSEEVENTF_LEFTDOWN = 0x02
MOUSEEVENTF_LEFTUP = 0x04
MOUSEEVENTF_RIGHTDOWN = 0x08
MOUSEEVENTF_RIGHTUP = 0x10

# Sound settings
NO_SOUND = True
PERL_WITH_SOUND = not NO_SOUND
PYTHON_WITH_SOUND = not NO_SOUND

# Python path
PYTHON3_PATH_EXE = r"C:\Progra~1\Python312\python.exe"

# Mouse delta swing (0 means no random swing)
mouse_delta_x_swing = 0
mouse_delta_y_swing = 0

# Full screen coordinates for 100% Chrome / 25% game zoom + Chrome bookmark bar
full_telescope_mouse_xy = (564, 730)
full_crypt_menu_mouse_xy = (542, 435)

# LAVA oil fix coordinates
full_crypt_menu_first_mouse_xy = (975, 464)
full_crypt_menu_second_mouse_xy = (975, 544)
full_crypt_menu_third_mouse_xy = (975, 624)
full_crypt_menu_fourth_mouse_xy = (975, 699)

full_crypt_first_mouse_xy = full_crypt_menu_third_mouse_xy

full_crypt_middle_mouse_xy = (773, 488)
full_crypt_middle_mouse_lower_xy = (970, 604)

full_crypt_explore_right_mouse_xy = (916, 686)
full_crypt_misclick_top_menu_mouse_xy = (995, 348)
full_crypt_speedup_top_menu_mouse_xy = (995, 200)

full_crypt_speedup_first_mouse_xy = (899, 430)
full_crypt_speedup_second_mouse_xy = (899, 517)
full_crypt_speedup_third_mouse_xy = (899, 606)

full_crypt_speedup_close_mouse_xy = (984, 284)


class POINT(Structure):
    """Windows POINT structure for cursor position"""
    _fields_ = [("x", c_long), ("y", c_long)]


def play_sound_system_start(state=-1):
    """Play system sound (Windows only)"""
    if PERL_WITH_SOUND:
        if state >= 0:
            print(f"Play State [{state}]")
        try:
            import winsound
            winsound.PlaySound("SystemStart", winsound.SND_ALIAS)
        except ImportError:
            pass


def move_mouse_cursor_position(x, y):
    """Move mouse cursor to specified position"""
    print(f"\nMoving cursor to ({x}, {y})")
    windll.user32.SetCursorPos(x, y)
    return True


def get_mouse_xy_coordinates():
    """Get current mouse cursor coordinates"""
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    print(f"Cursor is at: {pt.x}, {pt.y}")
    return pt


def send_mouse_right_click(mx, my):
    """Send right mouse click"""
    event = MOUSEEVENTF_RIGHTDOWN | MOUSEEVENTF_RIGHTUP
    windll.user32.mouse_event(event, mx, my, 0, 0)


def send_mouse_left_click(mx, my):
    """Send left mouse click"""
    event = MOUSEEVENTF_LEFTDOWN | MOUSEEVENTF_LEFTUP
    windll.user32.mouse_event(event, mx, my, 0, 0)


def usleep(microseconds):
    """Sleep for specified microseconds"""
    time.sleep(microseconds / 1000000.0)


def validate_is_crypt_left_menu():
    """Validate if crypt left menu is visible"""
    script = "Is-Crypt-Left-Menu.py"
    try:
        result = subprocess.run(
            [PYTHON3_PATH_EXE, script, str(int(PYTHON_WITH_SOUND))],
            capture_output=True,
            text=True
        )
        output = result.stdout
        
        if "BAD" in output or "#BAD" in output:
            print("is_crypt_left_menu: BAD was found")
            print("Crypt Left Menu was not found, the game is stuck")
            return None
        
        # Look for coordinates in format (x, y)
        import re
        match = re.search(r'\((\d+),\s*(\d+)\)', output)
        if match:
            x = int(match.group(1))
            y = int(match.group(2))
            print(f"is_crypt_left_menu: Found ({x}, {y})")
            return (x, y)
        
        return None
    except Exception as e:
        print(f"Error running validation script: {e}")
        return None


def validate_is_crypt_gray_title():
    """Validate if crypt gray title is visible"""
    script = "Is-Crypt-Gray-Title.py"
    try:
        result = subprocess.run(
            [PYTHON3_PATH_EXE, script, str(int(PYTHON_WITH_SOUND))],
            capture_output=True,
            text=True
        )
        output = result.stdout
        
        if "BAD" in output or "#BAD" in output:
            print("is_crypt_gray_title: BAD was found")
            return None
        
        import re
        match = re.search(r'\((\d+),\s*(\d+)\)', output)
        if match:
            x = int(match.group(1))
            y = int(match.group(2))
            print(f"is_crypt_gray_title: Found ({x}, {y})")
            return (x, y)
        
        return None
    except Exception as e:
        print(f"Error running validation script: {e}")
        return None


def validate_is_crypt_green_misclick_title():
    """Validate if crypt green misclick title is visible"""
    script = "Is-Crypt-Green-Misclick-Title.py"
    try:
        result = subprocess.run(
            [PYTHON3_PATH_EXE, script, str(int(PYTHON_WITH_SOUND))],
            capture_output=True,
            text=True
        )
        output = result.stdout
        
        if "BAD" in output or "#BAD" in output:
            print("is_crypt_green_misclick_title: BAD was found")
            return None
        
        import re
        match = re.search(r'\((\d+),\s*(\d+)\)', output)
        if match:
            x = int(match.group(1))
            y = int(match.group(2))
            print(f"is_crypt_green_misclick_title: Found ({x}, {y})")
            return (x, y)
        
        return None
    except Exception as e:
        print(f"Error running validation script: {e}")
        return None


def validate_is_crypt_green_speedup_title():
    """Validate if crypt green speedup title is visible"""
    script = "Is-Crypt-Green-Speedup-Title.py"
    try:
        result = subprocess.run(
            [PYTHON3_PATH_EXE, script, str(int(PYTHON_WITH_SOUND))],
            capture_output=True,
            text=True
        )
        output = result.stdout
        
        if "BAD" in output or "#BAD" in output:
            print("is_crypt_green_speedup_title: BAD was found")
            return None
        
        import re
        match = re.search(r'\((\d+),\s*(\d+)\)', output)
        if match:
            x = int(match.group(1))
            y = int(match.group(2))
            print(f"is_crypt_green_speedup_title: Found ({x}, {y})")
            return (x, y)
        
        return None
    except Exception as e:
        print(f"Error running validation script: {e}")
        return None


def find_crypt_position():
    """Find crypt position on screen"""
    script = "crypt-search.py"
    try:
        result = subprocess.run(
            [PYTHON3_PATH_EXE, script, str(int(PYTHON_WITH_SOUND))],
            capture_output=True,
            text=True
        )
        output = result.stdout
        
        if "BAD" in output or "#BAD" in output:
            print("find_crypt_position: BAD was found")
            return None
        
        import re
        match = re.search(r'\((\d+),\s*(\d+)\)', output)
        if match:
            x = int(match.group(1))
            y = int(match.group(2))
            print(f"find_crypt_position: Found ({x}, {y})")
            return (x, y)
        
        return None
    except Exception as e:
        print(f"Error running search script: {e}")
        return None


def full_screen_state_machine(i=-1, skip=0):
    """Main state machine for crypt automation"""
    global full_crypt_first_mouse_xy
    
    if i >= 0:
        i = i % 4
        if i == 1:
            full_crypt_first_mouse_xy = full_crypt_menu_second_mouse_xy
        elif i == 2:
            full_crypt_first_mouse_xy = full_crypt_menu_third_mouse_xy
        elif i == 3:
            full_crypt_first_mouse_xy = full_crypt_menu_fourth_mouse_xy
        else:
            full_crypt_first_mouse_xy = full_crypt_menu_first_mouse_xy
    
    telescope_mouse_xy = full_telescope_mouse_xy
    crypt_menu_mouse_xy = full_crypt_menu_mouse_xy
    crypt_first_mouse_xy = full_crypt_first_mouse_xy
    crypt_middle_mouse_xy = full_crypt_middle_mouse_xy
    crypt_middle_mouse_lower_xy = full_crypt_middle_mouse_lower_xy
    crypt_explore_right_mouse_xy = full_crypt_explore_right_mouse_xy
    crypt_misclick_top_menu_mouse_xy = full_crypt_misclick_top_menu_mouse_xy
    crypt_speedup_top_menu_mouse_xy = full_crypt_speedup_top_menu_mouse_xy
    crypt_speedup_first_mouse_xy = full_crypt_speedup_first_mouse_xy
    crypt_speedup_second_mouse_xy = full_crypt_speedup_second_mouse_xy
    crypt_speedup_third_mouse_xy = full_crypt_speedup_third_mouse_xy
    crypt_speedup_close_mouse_xy = full_crypt_speedup_close_mouse_xy
    
    # Random offset
    dx = random.randint(-mouse_delta_x_swing, mouse_delta_x_swing)
    dy = random.randint(-mouse_delta_y_swing, mouse_delta_y_swing)
    
    dw = 150000 + random.randint(0, 100000)  # 150ms to 250ms wait delta
    
    wait_move_xy = dw + 10000      # 10ms
    wait_click = dw + 60000        # 60ms
    wait_screen = dw + 800000      # 800ms
    wait_crypt = dw + 28000000     # 28000ms
    
    crypt_speedup_mouse_xy = crypt_speedup_second_mouse_xy
    
    if skip < 1:
        move_mouse_cursor_position(telescope_mouse_xy[0] + dx, telescope_mouse_xy[1] + dy)
        usleep(wait_move_xy)
        send_mouse_left_click(0, 0)
        usleep(wait_click)
        
        usleep(wait_screen)
        
        move_mouse_cursor_position(crypt_menu_mouse_xy[0] + dx, crypt_menu_mouse_xy[1] + dy)
        usleep(wait_move_xy)
        send_mouse_left_click(0, 0)
        usleep(wait_click)
        
        usleep(wait_screen)
        
        crypt_left_menu_pos = validate_is_crypt_left_menu()
        if crypt_left_menu_pos is None:
            print("Could not find the crypt LEFT MENU, try again")
            return 1
        
        usleep(wait_screen)
        
        move_mouse_cursor_position(crypt_first_mouse_xy[0] + dx, crypt_first_mouse_xy[1] + dy)
        usleep(wait_move_xy)
        send_mouse_left_click(0, 0)
        usleep(wait_click)
        
        usleep(wait_screen)
        usleep(wait_screen)
        
        move_mouse_cursor_position(crypt_middle_mouse_xy[0] + dx, crypt_middle_mouse_xy[1] + dy)
        usleep(wait_move_xy)
        send_mouse_left_click(0, 0)
        usleep(wait_click)
        
        usleep(wait_screen)
    else:
        crypt_pos = find_crypt_position()
        if crypt_pos is None:
            print("Could not find ANY crypt, try again")
            return 3
        else:
            crypt_middle_mouse_xy = crypt_pos
            print(f"Using NEW CRYPT at = ({crypt_middle_mouse_xy[0] + dx}, {crypt_middle_mouse_xy[1] + dy})")
            
            move_mouse_cursor_position(crypt_middle_mouse_xy[0] + dx, crypt_middle_mouse_xy[1] + dy)
            usleep(wait_move_xy)
            send_mouse_left_click(0, 0)
            usleep(wait_click)
            
            usleep(wait_screen)
    
    crypt_gray_title_pos = validate_is_crypt_gray_title()
    print(f"Gray title position: {crypt_gray_title_pos}")
    
    if crypt_gray_title_pos is None:
        crypt_misclick_green_title_pos = validate_is_crypt_green_misclick_title()
        print(f"Misclick green title position: {crypt_misclick_green_title_pos}")
        
        if crypt_misclick_green_title_pos is None:
            print("Could not find the crypt, nor misclick green title, try again")
            return 21
        else:
            print(f"Misclick green title window was found at [{crypt_misclick_green_title_pos[0]}, {crypt_misclick_green_title_pos[1]}]")
            
            move_mouse_cursor_position(crypt_misclick_top_menu_mouse_xy[0] + dx, crypt_misclick_top_menu_mouse_xy[1] + dy)
            usleep(wait_move_xy)
            send_mouse_left_click(0, 0)
            usleep(wait_click)
            
            usleep(wait_screen)
            
            crypt_misclick_green_title_pos2 = validate_is_crypt_green_misclick_title()
            if crypt_misclick_green_title_pos2 is None:
                print("Misclick window was closed")
                print(f"MOVE MOUSE LOWER [{crypt_middle_mouse_lower_xy[0]}, {crypt_middle_mouse_lower_xy[1]}]")
                
                move_mouse_cursor_position(crypt_middle_mouse_lower_xy[0] + dx, crypt_middle_mouse_lower_xy[1] + dy)
                usleep(wait_move_xy)
                send_mouse_left_click(0, 0)
                usleep(wait_click)
                
                usleep(wait_screen)
                
                print("Validate Crypt Gray Title #2")
                
                crypt_gray_title_pos2 = validate_is_crypt_gray_title()
                print(f"Gray title position #2: {crypt_gray_title_pos2}")
                if crypt_gray_title_pos2 is None:
                    return 23
                else:
                    print("Crypt was shifted below")
            else:
                print("Could not find the lower crypt, try again")
                return 22
    
    move_mouse_cursor_position(crypt_explore_right_mouse_xy[0] + dx, crypt_explore_right_mouse_xy[1] + dy)
    usleep(wait_move_xy)
    send_mouse_left_click(0, 0)
    usleep(wait_click)
    
    usleep(wait_screen)
    
    move_mouse_cursor_position(crypt_speedup_top_menu_mouse_xy[0] + dx, crypt_speedup_top_menu_mouse_xy[1] + dy)
    usleep(wait_move_xy)
    send_mouse_left_click(0, 0)
    usleep(wait_click)
    
    usleep(wait_screen)
    
    move_mouse_cursor_position(crypt_speedup_mouse_xy[0] + dx, crypt_speedup_mouse_xy[1] + dy)
    usleep(wait_move_xy)
    
    crypt_green_title_pos = validate_is_crypt_green_speedup_title()
    
    if crypt_green_title_pos is None:
        print("Could not find the speed up title, try again")
        return 3
    
    send_mouse_left_click(0, 0)
    usleep(wait_click)
    
    # 5 speedup clicks
    for _ in range(5):
        usleep(wait_click)
        send_mouse_left_click(0, 0)
    
    usleep(wait_click)
    usleep(wait_click)
    
    usleep(wait_screen)
    
    play_sound_system_start(8)
    
    usleep(wait_screen)
    
    move_mouse_cursor_position(crypt_speedup_close_mouse_xy[0] + dx, crypt_speedup_close_mouse_xy[1] + dy)
    usleep(wait_move_xy)
    send_mouse_left_click(0, 0)
    usleep(wait_click)
    usleep(wait_screen)
    
    play_sound_system_start(9)
    usleep(wait_crypt)
    play_sound_system_start(10)
    
    return 0


def main():
    """Main function - runs the automation loop"""
    # Seed random number generator
    random.seed(time.time())
    
    max_iterations = 9000
    r2 = 0
    retry = 0
    good = 0
    total = 0
    
    pt = get_mouse_xy_coordinates()
    
    print("Sleep 5 seconds... GO!\n")
    play_sound_system_start(1)
    time.sleep(5)
    
    play_sound_system_start(2)
    
    for i in range(1, max_iterations + 1):
        pt = get_mouse_xy_coordinates()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{i}]\t{timestamp}\t with GOOD [{good}] / [{total}]")
        
        if r2 < 1:
            print("Wait 300ms...")
            usleep(300000)  # 300ms
        else:
            print("Skip wait...")
        
        r2 = full_screen_state_machine(i % 4)
        
        if r2 == 1:
            retry += 1
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"BAD RETRY... [{retry}] after GOOD [{good}] / [{total}]")
            print(timestamp)
            good = 0
        elif r2 == 0:
            good += 1
            total += 1
            
            if good >= 10:
                print(f"RESET BAD RETRY... [{retry}] after GOOD [{good}] / [{total}]")
                retry = 0
        
        if retry > 20:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"BAD RETRY EXITING... [{retry}] after GOOD [{good}] / [{total}]")
            print(timestamp)
            sys.exit(1)
        
        play_sound_system_start(3)
    
    play_sound_system_start(4)


if __name__ == "__main__":
    main()
