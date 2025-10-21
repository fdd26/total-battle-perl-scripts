import win32api
import win32con

# pip install pywin32

# Get current cursor position
(x, y) = win32api.GetCursorPos()
print(f"Current Cursor Position: ({x}, {y})")

# Set cursor position (e.g., to 0,0)
#win32api.SetCursorPos((0, 0))

# Simulate mouse click (left button down + up) at current position (0,0)
x2 = x + 10
y2 = y + 10

win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, x2, y2, 0, 0)

