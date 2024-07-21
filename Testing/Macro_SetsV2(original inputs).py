#_________________________________________________________________________________________________________________________________________________#
#Import all Libraries
import time
import board
import digitalio
import usb_hid
import displayio, os, terminalio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.Keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_matrixkeypad import Matrix_Keypad
from adafruit_hid.keyboard_layout_us import *
import busio
from adafruit_display_text import label
import adafruit_displayio_sh1107
#_________________________________________________________________________________________________________________________________________________#
#Setting up Maxtrix
# define the pins for the keypad
# cols = [digitalio.DigitalInOut(board.GP2), digitalio.DigitalInOut(board.GP3), digitalio.DigitalInOut(board.GP4)]
# rows = [digitalio.DigitalInOut(board.GP6), digitalio.DigitalInOut(board.GP7), digitalio.DigitalInOut(board.GP8)]
# 
# # define the keymap for the keypad
# keys = ((1, 2, "Blank"),
#         (3, 4, 5),
#         (6, 7, 8))
# 
# # create the keypad object
# keypad = Matrix_Keypad(rows, cols, keys)

# create the keyboard and consumer control objects
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayout(kbd)
cc = ConsumerControl(usb_hid.devices)

# define the Keycodes for the consumer control keys
PLAY_PAUSE = ConsumerControlCode.PLAY_PAUSE
MUTE = ConsumerControlCode.MUTE
NEXT_TRACK = ConsumerControlCode.SCAN_NEXT_TRACK
PREV_TRACK = ConsumerControlCode.SCAN_PREVIOUS_TRACK
VOLUME_UP = ConsumerControlCode.VOLUME_INCREMENT
VOLUME_DOWN = ConsumerControlCode.VOLUME_DECREMENT

# define the Keycodes for the modifier keys
SHIFT = Keycode.SHIFT
CONTROL = Keycode.CONTROL
ALT = Keycode.ALT
GUI = Keycode.GUI
#_________________________________________________________________________________________________________________________________________________#
#LCD Setup
# try:
#     
#     displayio.release_displays()
#     # oled_reset = board.D9
# 
#     board_type = os.uname().machine
#     print(f"Board: {board_type}")
# 
#     oled_SCL = board.GP7
#     oled_SDA = board.GP6
#     oled_RST = board.GP12
#     oled_DC = board.GP8
#     oled_CS = board.GP9
# 
#     # 128x128 SH1107
#     OLED_W = 128
#     OLED_H = 64
# 
#     oled_spi = busio.SPI(clock=board.GP10, MOSI=board.GP11)
#     display_bus = displayio.FourWire(oled_spi, command=oled_DC, chip_select=oled_CS, reset=oled_RST)
# 
#     display = adafruit_displayio_sh1107.SH1107(display_bus,width=OLED_W, height=OLED_H,rotation=0)
# 
# 
# 
#     # Make the display context
#     splash = displayio.Group()
#     display.root_group = splash
#     
#     print("Display Found")
#     
#     
# except Exception as e:
#     print("No Screen Detected")

#_________________________________________________________________________________________________________________________________________________#
#Define Macro SETS
    
def Macro_Set_1():
#     keys = keypad.pressed_keys
#     if keys:
#         # loop through all the pressed keys and send the appropriate key press
#         for key in keys:
#             if key == 1:
#                 cc.send(ConsumerControlCode.BRIGHTNESS_DECREMENT)
#                 kbd.release_all
#             elif key == 2:
#                 cc.send(ConsumerControlCode.BRIGHTNESS_INCREMENT)
#                 kbd.release_all
#             elif key == 5:
#                 cc.send(PLAY_PAUSE)
#                 kbd.release_all
#             elif key == 8:
#                 cc.send(MUTE)
#             elif key == 4:
#                 cc.send(NEXT_TRACK)
#             elif key == 3:
#                 cc.send(PREV_TRACK)
#             elif key == 7:
#                 cc.send(VOLUME_UP)
#             elif key == 6:
#                 cc.send(VOLUME_DOWN)
#             else:
#                 print(keys)
    time.sleep(0.05)
#     print("Macro 1")
    
def Macro_Set_2():
#     keys = keypad.pressed_keys
#     if keys:
#         # loop through all the pressed keys and send the appropriate key press
#         for key in keys:
#             if key == 1:
#                 kbd.send(Keycode.ONE)
#             elif key == 2:
#                 kbd.send(Keycode.TWO)
#             elif key == 3:
#                 kbd.send(Keycode.THREE)
#             elif key == 4:
#                 kbd.send(Keycode.FOUR)
#             elif key == 5:
#                 kbd.send(Keycode.FIVE)
#             elif key == 6:
#                 kbd.send(Keycode.SIX)
#             elif key == 7:
#                 kbd.send(Keycode.SEVEN)
#             elif key == 8:
#                 kbd.send(Keycode.EIGHT)
# 
#             else:
#                 print(keys)
    time.sleep(0.05)
#     print("Macro 2")

def Macro_Set_3():
#     keys = keypad.pressed_keys
#
    time.sleep(0.05)
#     print("Macro 3")
def Macro_Set_4():
#     keys = keypad.pressed_keys
#     if keys:
#         # loop through all the pressed keys and send the appropriate key press
#         for key in keys:
#             if key == 1:
#                 kbd.send(Keycode.F1)
#             elif key == 2:
#                 kbd.send(Keycode.F2)
#             elif key == 3:
#                 kbd.send(Keycode.F3)
#             elif key == 4:
#                 kbd.send(Keycode.F4)
#             elif key == 5:
#                 kbd.send(Keycode.F5)
#             elif key == 6:
#                 kbd.send(Keycode.F6)
#             elif key == 7:
#                 kbd.send(Keycode.F7)
#             elif key == 8:
#                 kbd.send(Keycode.F8)
#             else:
#                 print(keys)
    time.sleep(0.05)
#     print("Macro 4")
def Macro_Set_5():
#     keys = keypad.pressed_keys
#     if keys:
#         # loop through all the pressed keys and send the appropriate key press
#         for key in keys:
#             if key == 1:
#                 kbd.send(Keycode.CONTROL, Keycode.C)
#             elif key == 2:
#                 kbd.send(Keycode.CONTROL, Keycode.V)
#             elif key == 3:
#                 kbd.send(Keycode.CONTROL, Keycode.A)
#             elif key == 4:
#                 kbd.send(Keycode.CONTROL, Keycode.X)
#             elif key == 5:
#                 kbd.send(Keycode.CONTROL, Keycode.P)
#             elif key == 6:
#                 kbd.send(Keycode.F6)
#             elif key == 7:
#                 kbd.send(Keycode.F7)
#             elif key == 8:
#                 #Github Token
#					#thought you had me didnt you haha not today
#             else:
#                 print(keys)
    time.sleep(0.05)
#     print("Macro 5")
def Macro_Set_6():
#     keys = keypad.pressed_keys
    time.sleep(0.05)
#     print("Macro 6")