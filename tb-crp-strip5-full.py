#!/usr/bin/env python3
"""
Total Battle - Mouse Click Bot for 1536x864 Chrome browser with bookmark tab offset

Converted from Perl5 to Python3

Working correctly as of 2026-01-23

BSD 2-Clause Licensed source code

Copyright (c) 2024-2026, fdd26

"""

import sys
import time
import random
import subprocess
import re
import winsound

from datetime import datetime
from ctypes   import windll, Structure, c_long, byref

# Mouse event constants
MOUSEEVENTF_LEFTDOWN  = 0x02
MOUSEEVENTF_LEFTUP    = 0x04
MOUSEEVENTF_RIGHTDOWN = 0x08
MOUSEEVENTF_RIGHTUP   = 0x10


class POINT(Structure):
    """Windows POINT structure for cursor position"""
    _fields_ = [("x", c_long), ("y", c_long)]


class MouseController:
    """Handles mouse operations using Windows API"""

    def __init__(self):
        self.user32 = windll.user32

    def get_cursor_pos(self):
        """Get current cursor position"""
        pt = POINT()
        windll.user32.GetCursorPos(byref(pt))
        print(f"Cursor is at: {pt.x}, {pt.y}", flush=True)
        return (pt.x, pt.y)

    def set_cursor_pos(self, x, y):
        """Move cursor to specified position"""
        print(f"\nMoving cursor to ({x}, {y})")
        return windll.user32.SetCursorPos(int(x), int(y))

    def mouse_event(self, flags, dx=0, dy=0, data=0, extra_info=0):
        """Send mouse event"""
        windll.user32.mouse_event(flags, dx, dy, data, extra_info)
        return True

    def left_click(self, mx=0, my=0):
        """Perform left mouse click"""
        event = MOUSEEVENTF_LEFTDOWN | MOUSEEVENTF_LEFTUP
        self.mouse_event(event, mx, my, 0, 0)
        return True

    def right_click(self, mx=0, my=0):
        """Perform right mouse click"""
        event = MOUSEEVENTF_RIGHTDOWN | MOUSEEVENTF_RIGHTUP
        self.mouse_event(event, mx, my, 0, 0)
        return True

class SoundManager:
    """Manages sound playback"""

    def __init__(self, enabled=False):
        self.enabled = enabled

    def play_system_start(self, state=-1):
        """Play system start sound"""
        if self.enabled:
            if state >= 0:
                print(f"Play State [{state}]", flush=True)
            try:
                import winsound
                winsound.PlaySound("SystemStart", winsound.SND_ALIAS)
            except Exception as e:
                print(f"Sound playback failed: {e}", flush=True)


class CryptBot:
    """Main bot class for Total Battle crypt automation"""

    def __init__(self, no_sound=True, python_with_sound=False):
        self.mouse = MouseController()
        self.sound = SoundManager(enabled=not no_sound)
        self.python_with_sound = python_with_sound

        # Python script path
        self.python3_path = r"C:\Progra~1\Python312\python.exe"

        # Mouse swing (random offset)
        self.mouse_delta_x_swing = 0
        self.mouse_delta_y_swing = 0

        # Full screen coordinates for 1536x864 Chrome with bookmark bar
        self.full_telescope_mouse_xy               = [564, 730]
        self.full_crypt_menu_mouse_xy              = [542, 435]

        # Crypt menu positions
        self.full_crypt_menu_first_mouse_xy        = [975, 464]
        self.full_crypt_menu_second_mouse_xy       = [975, 544]
        self.full_crypt_menu_third_mouse_xy        = [975, 624]
        self.full_crypt_menu_fourth_mouse_xy       = [975, 699]

        self.full_crypt_first_mouse_xy             = self.full_crypt_menu_third_mouse_xy.copy()

        self.full_crypt_middle_mouse_xy            = [773, 488]
        self.full_crypt_middle_mouse_lower_xy      = [970, 604]

        self.full_crypt_explore_right_mouse_xy     = [916, 686]
        self.full_crypt_misclick_top_menu_mouse_xy = [995, 348]
        self.full_crypt_speedup_top_menu_mouse_xy  = [995, 200]

        self.full_crypt_speedup_first_mouse_xy     = [899, 430]
        self.full_crypt_speedup_second_mouse_xy    = [899, 517]
        self.full_crypt_speedup_third_mouse_xy     = [899, 606]

        self.full_crypt_speedup_close_mouse_xy     = [984, 284]

    def usleep(self, microseconds):
        """Sleep for specified microseconds"""
        time.sleep(microseconds / 1000000.0)
        return True

    def run_python_script(self, script_name):
        """Execute a Python script and return output"""
        try:
            sound_arg = "1" if self.python_with_sound else "0"
            result = subprocess.run(
                [self.python3_path, script_name, sound_arg],
                capture_output=True,
                text=True
            )
            return result.stdout
        except Exception as e:
            print(f"Error running script {script_name}: {e}", flush=True)
            return None

    def validate_is_crypt_left_menu(self):
        """Validate if crypt left menu is visible"""
        output = self.run_python_script("Is-Crypt-Left-Menu.py")
        if not output:
            return None

        if "BAD" in output or "#BAD" in output:
            print("is_crypt_left_menu: BAD was found", flush=True)
            print("Crypt Left Menu was not found, the game is stuck", flush=True)
            return None

        # Parse coordinates from output
        import re
        match = re.search(r'\((\d+),\s*(\d+)\)', output)
        if match:
            (x, y) = int(match.group(1)), int(match.group(2))
            print(f"is_crypt_left_menu: Found ({x}, {y})", flush=True)
            return [x, y]

        return None

    def validate_is_crypt_gray_title(self):
        """Validate if crypt gray title is visible"""
        output = self.run_python_script("Is-Crypt-Gray-Title.py")
        if not output:
            return None

        if "BAD" in output or "#BAD" in output:
            print("is_crypt_gray_title: BAD was found", flush=True)
            return None

        import re
        match = re.search(r'\((\d+),\s*(\d+)\)', output)
        if match:
            (x, y) = int(match.group(1)), int(match.group(2))
            print(f"is_crypt_gray_title: Found ({x}, {y})", flush=True)
            return [x, y]

        return None

    def validate_is_crypt_green_misclick_title(self):
        """Validate if crypt green misclick title is visible"""
        output = self.run_python_script("Is-Crypt-Green-Misclick-Title.py")
        if not output:
            return None

        if "BAD" in output or "#BAD" in output:
            print("is_crypt_green_misclick_title: BAD was found", flush=True)
            return None

        import re
        match = re.search(r'\((\d+),\s*(\d+)\)', output)
        if match:
            (x, y) = int(match.group(1)), int(match.group(2))
            print(f"is_crypt_green_misclick_title: Found ({x}, {y})", flush=True)
            return [x, y]

        return None

    def validate_is_crypt_green_speedup_title(self):
        """Validate if crypt green speedup title is visible"""
        output = self.run_python_script("Is-Crypt-Green-Speedup-Title.py")
        if not output:
            return None

        if "BAD" in output or "#BAD" in output:
            print("is_crypt_green_speedup_title: BAD was found", flush=True)
            return None

        import re
        match = re.search(r'\((\d+),\s*(\d+)\)', output)
        if match:
            (x, y) = int(match.group(1)), int(match.group(2))
            print(f"is_crypt_green_speedup_title: Found ({x}, {y})", flush=True)
            return [x, y]

        return None

    def find_crypt_position(self):
        """Find crypt position on screen"""
        output = self.run_python_script("crypt-search.py")
        if not output:
            return None

        if "BAD" in output or "#BAD" in output:
            print("find_crypt_position: BAD was found", flush=True)
            return None

        import re
        match = re.search(r'\((\d+),\s*(\d+)\)', output)
        if match:
            (x, y) = int(match.group(1)), int(match.group(2))
            print(f"find_crypt_position: Found ({x}, {y})", flush=True)
            return [x, y]

        return None

    def full_screen_state_machine(self, i=-1, skip=0):
        """Main state machine for crypt automation"""

        # Update crypt position based on iteration
        if i >= 0:
            i = i % 4
            if i == 1:
                self.full_crypt_first_mouse_xy = self.full_crypt_menu_second_mouse_xy.copy()
            elif i == 2:
                self.full_crypt_first_mouse_xy = self.full_crypt_menu_third_mouse_xy.copy()
            elif i == 3:
                self.full_crypt_first_mouse_xy = self.full_crypt_menu_fourth_mouse_xy.copy()
            else:
                self.full_crypt_first_mouse_xy = self.full_crypt_menu_first_mouse_xy.copy()

        # Random offset
        dx = random.randint(-self.mouse_delta_x_swing, self.mouse_delta_x_swing)
        dy = random.randint(-self.mouse_delta_y_swing, self.mouse_delta_y_swing)

        # Wait times (in microseconds)
        dw = 150000 + random.randint(0, 100000)  # 150-250ms
        wait_move_xy = dw + 10000        # 10ms
        wait_click   = dw + 60000        # 60ms
        wait_screen  = dw + 800000       # 800ms
        wait_crypt   = dw + 28000000     # 28000ms

        crypt_speedup_mouse_xy = self.full_crypt_speedup_second_mouse_xy

        if skip < 1:
            # Click telescope
            self.mouse.set_cursor_pos(self.full_telescope_mouse_xy[0] + dx,
                                      self.full_telescope_mouse_xy[1] + dy)
            self.usleep(wait_move_xy)
            self.mouse.left_click(0, 0)
            self.usleep(wait_click)
            self.usleep(wait_screen)

            # Click crypt menu
            self.mouse.set_cursor_pos(self.full_crypt_menu_mouse_xy[0] + dx,
                                      self.full_crypt_menu_mouse_xy[1] + dy)
            self.usleep(wait_move_xy)
            self.mouse.left_click(0, 0)
            self.usleep(wait_click)
            self.usleep(wait_screen)

            # Validate crypt left menu
            crypt_left_menu_pos = self.validate_is_crypt_left_menu()
            if not crypt_left_menu_pos:
                print("Could not find the crypt LEFT MENU, try again", flush=True)
                return 1

            self.usleep(wait_screen)

            # Click first crypt position
            self.mouse.set_cursor_pos(self.full_crypt_first_mouse_xy[0] + dx,
                                      self.full_crypt_first_mouse_xy[1] + dy)
            self.usleep(wait_move_xy)
            self.mouse.left_click(0, 0)
            self.usleep(wait_click)
            self.usleep(wait_screen)
            self.usleep(wait_screen)

            # Click middle crypt
            self.mouse.set_cursor_pos(self.full_crypt_middle_mouse_xy[0] + dx,
                                      self.full_crypt_middle_mouse_xy[1] + dy)
            self.usleep(wait_move_xy)
            self.mouse.left_click(0, 0)
            self.usleep(wait_click)
            self.usleep(wait_screen)
        else:
            # Find crypt position
            crypt_pos = self.find_crypt_position()
            if not crypt_pos:
                print("Could not find ANY crypt, try again", flush=True)
                return 3

            crypt_middle_mouse_xy = crypt_pos
            print(f"Using NEW CRYPT at = ({crypt_middle_mouse_xy[0] + dx}, {crypt_middle_mouse_xy[1] + dy})", flush=True)

            self.mouse.set_cursor_pos(crypt_middle_mouse_xy[0] + dx,
                                      crypt_middle_mouse_xy[1] + dy)
            self.usleep(wait_move_xy)
            self.mouse.left_click(0, 0)
            self.usleep(wait_click)
            self.usleep(wait_screen)

        # Validate gray title
        crypt_gray_title_pos = self.validate_is_crypt_gray_title()

        if not crypt_gray_title_pos:
            # Check for misclick
            crypt_misclick_green_title_pos = self.validate_is_crypt_green_misclick_title()

            if not crypt_misclick_green_title_pos:
                print("Could not find the crypt, nor misclick green title, try again", flush=True)
                return 21

            print(f"Misclick green title window was found at "
                  f"[{crypt_misclick_green_title_pos[0]}, {crypt_misclick_green_title_pos[1]}]")

            # Close misclick window
            self.mouse.set_cursor_pos(self.full_crypt_misclick_top_menu_mouse_xy[0] + dx,
                                      self.full_crypt_misclick_top_menu_mouse_xy[1] + dy)
            self.usleep(wait_move_xy)
            self.mouse.left_click(0, 0)
            self.usleep(wait_click)
            self.usleep(wait_screen)

            # Verify misclick closed
            crypt_misclick_green_title_pos2 = self.validate_is_crypt_green_misclick_title()
            if not crypt_misclick_green_title_pos2:
                print("Misclick window was closed", flush=True)
                print(f"MOVE MOUSE LOWER [{self.full_crypt_middle_mouse_lower_xy[0]}, "
                      f"{self.full_crypt_middle_mouse_lower_xy[1]}]", flush=True)

                self.mouse.set_cursor_pos(self.full_crypt_middle_mouse_lower_xy[0] + dx,
                                          self.full_crypt_middle_mouse_lower_xy[1] + dy)
                self.usleep(wait_move_xy)
                self.mouse.left_click(0, 0)
                self.usleep(wait_click)
                self.usleep(wait_screen)

                print("Validate Crypt Gray Title #2", flush=True)
                crypt_gray_title_pos2 = self.validate_is_crypt_gray_title()
                if not crypt_gray_title_pos2:
                    return 23
                print("Crypt was shifted below", flush=True)
            else:
                print("Could not find the lower crypt, try again", flush=True)
                return 22

        # Click explore right
        self.mouse.set_cursor_pos(self.full_crypt_explore_right_mouse_xy[0] + dx,
                                  self.full_crypt_explore_right_mouse_xy[1] + dy)
        self.usleep(wait_move_xy)
        self.mouse.left_click(0, 0)
        self.usleep(wait_click)
        self.usleep(wait_screen)

        # Click speedup top menu
        self.mouse.set_cursor_pos(self.full_crypt_speedup_top_menu_mouse_xy[0] + dx,
                                  self.full_crypt_speedup_top_menu_mouse_xy[1] + dy)
        self.usleep(wait_move_xy)
        self.mouse.left_click(0, 0)
        self.usleep(wait_click)
        self.usleep(wait_screen)

        # Move to speedup position
        self.mouse.set_cursor_pos(crypt_speedup_mouse_xy[0] + dx,
                                  crypt_speedup_mouse_xy[1] + dy)
        self.usleep(wait_move_xy)

        # Validate speedup title
        crypt_green_title_pos = self.validate_is_crypt_green_speedup_title()
        if not crypt_green_title_pos:
            print("Could not find the speed up title, try again", flush=True)
            return 3

        # Perform 6 speedup clicks
        for _ in range(6):
            self.mouse.left_click(0, 0)
            self.usleep(wait_click)

        self.usleep(wait_screen)
        self.sound.play_system_start(8)
        self.usleep(wait_screen)

        # Close speedup window
        self.mouse.set_cursor_pos(self.full_crypt_speedup_close_mouse_xy[0] + dx,
                                  self.full_crypt_speedup_close_mouse_xy[1] + dy)
        self.usleep(wait_move_xy)
        self.mouse.left_click(0, 0)
        self.usleep(wait_click)
        self.usleep(wait_screen)

        self.sound.play_system_start(9)
        self.usleep(wait_crypt)
        self.sound.play_system_start(10)

        return 0

    def run(self, max_iterations=9000):
        """Main execution loop"""
        retry = 0
        good  = 0
        total = 0

        # Get initial cursor position
        self.mouse.get_cursor_pos()

        print("Sleep 5 seconds... GO!\n", flush=True)
        self.sound.play_system_start(1)
        time.sleep(5)

        self.sound.play_system_start(2)

        for i in range(1, max_iterations + 1):
            self.mouse.get_cursor_pos()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{i}]\t{timestamp}\t with GOOD [{good}] / [{total}]", flush=True)

            if retry < 1:
                print("Wait 300ms...", flush=True)
                self.usleep(300000)  # 300ms
            else:
                print("Skip wait...", flush=True)

            r2 = self.full_screen_state_machine(i % 4)

            if r2 == 1:
                retry += 1
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"BAD RETRY... [{retry}] after GOOD [{good}] / [{total}]", flush=True)
                print(f"{timestamp}", flush=True)
                good = 0
            elif r2 == 0:
                good  += 1
                total += 1

                if good >= 10:
                    print(f"RESET BAD RETRY... [{retry}] after GOOD [{good}] / [{total}]", flush=True)
                    retry = 0

            if retry > 20:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"BAD RETRY EXITING... [{retry}] after GOOD [{good}] / [{total}]", flush=True)
                print(f"{timestamp}", flush=True)
                sys.exit(1)

            self.sound.play_system_start(3)

            # DEBUG
            # sys.exit(0)

        self.sound.play_system_start(4)


def main():
    """Entry point"""
    print(f"GO!", flush=True)
    bot = CryptBot(no_sound=True, python_with_sound=False)
    bot.run(max_iterations=9000)


if __name__ == "__main__":
    main()
