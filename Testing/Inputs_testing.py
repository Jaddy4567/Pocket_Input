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
#Setting up HID

E_BTN = digitalio.DigitalInOut(board.GP26)
E_BTN.direction = digitalio.Direction.INPUT
E_BTN.pull = digitalio.Pull.DOWN

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
#Define Macro SETS
    
def Macro_Set_1():
    if E_BTN.value:
       kbd.send(Keycode.ONE)
       print("encoder Button pressed")
    time.sleep(0.05)
#     print("Macro 1")
    
def Macro_Set_2():
    if E_BTN.value:
       kbd.send(Keycode.TWO)
       print("encoder Button pressed")
    time.sleep(0.05)
#     print("Macro 2")

def Macro_Set_3():
    if E_BTN.value:
       kbd.send(Keycode.THREE)
       print("encoder Button pressed")
    time.sleep(0.05)
#     print("Macro 3")

def Macro_Set_4():
    if E_BTN.value:
       kbd.send(Keycode.FOUR)
       print("encoder Button pressed")
    time.sleep(0.05)
#     print("Macro 4")

def Macro_Set_5():
    if E_BTN.value:
       kbd.send(Keycode.FIVE)
       print("encoder Button pressed")
    time.sleep(0.05)
#     print("Macro 5")

def Macro_Set_6():
    if E_BTN.value:
       kbd.send(Keycode.SIX)
       print("encoder Button pressed")
    time.sleep(0.05)
#     print("Macro 6")