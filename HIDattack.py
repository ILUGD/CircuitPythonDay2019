# IT SUCKS and it's not complete. so DONT FUCKING RUN IT!

from adafruit_circuitplayground.express import cpx
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.mouse import Mouse

kbd = Keyboard()
layout = KeyboardLayoutUS(kbd)
m = Mouse()
cpx.adjust_touch_threshold(200)

with open("tada.txt") as f:
    lines = f.read().splitlines()
      
"""
#ENTER 2
#SLEEP x
#STRING asdasdasdasdasdasd\n
#MOVE x,y
#LCLICK x
#RCLICK x
#_BUTTON_ down
#_BUTTON_ up
"""
print(lines)
sleep(4)
for line in lines:
    if line[0] == "#":
        line = line.lstrip("#").split()
    print(line)

    if line[0] == "BACKSPACE":
        kbd.press(Keycode.BACKSPACE)
    if line[0] == "SPACE":
        kbd.press(Keycode.SPACE)
        
    if line[0] == "RALL": 
        kbd.release_all()

    if line[0] == "RETURN":
        kbd.press(Keycode.RETURN)
    if line[0] == "DELETE":
        kbd.press(Keycode.DELETE)
    if line[0] == "TAB":
        kbd.press(Keycode.TAB)
    if line[0] == "COMMAND":
        kbd.press(Keycode.COMMAND)
    if line[0] == "SHIFT":
        kbd.press(Keycode.SHIFT)
    if line[0] == "ALT":
        kbd.press(Keycode.ALT)
    if line[0] == "APPLICATION":
        kbd.press(Keycode.APPLICATION)
    if line[0] == "DOWN_ARROW":
        kbd.press(Keycode.DOWN_ARROW)
    if line[0] == "UP_ARROW":
        kbd.press(Keycode.UP_ARROW)
    if line[0] == "END":
        kbd.press(Keycode.END)
    if line[0] == "ESCAPE":
        kbd.press(Keycode.ESCAPE)
    if line[0] == "INSERT":
        kbd.press(Keycode.INSERT)
    if line[0] == "RIGHT_ARROW":
        kbd.press(Keycode.RIGHT_ARROW)
    if line[0] == "LEFT_ARROW":
        kbd.press(Keycode.LEFT_ARROW)
    if line[0] == "POWER":
        kbd.press(Keycode.POWER)
    if line[0] == "PRINT_SCREEN":
        kbd.press(Keycode.PRINT_SCREEN)
