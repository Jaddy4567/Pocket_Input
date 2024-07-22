#import Libraries
import time
import board
import rotaryio
import digitalio
import usb_hid
import displayio, os, terminalio
import microcontroller
import busio
from adafruit_hid.keyboard_layout_us import KeyboardLayoutBase
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_matrixkeypad import Matrix_Keypad
from adafruit_display_text import label
import adafruit_displayio_sh1107

#_________________________________________________________________________________________________________________________________________________#
#LCD Setup

try:
    
    displayio.release_displays()
    # oled_reset = board.D9

    board_type = os.uname().machine
    print(f"Board: {board_type}")

    oled_SCL = board.GP7
    oled_SDA = board.GP6
    oled_RST = board.GP12
    oled_DC = board.GP8
    oled_CS = board.GP9

    # 128x64 SH1107
    OLED_W = 128
    OLED_H = 64

    oled_spi = busio.SPI(clock=board.GP10, MOSI=board.GP11)
    display_bus = displayio.FourWire(oled_spi, command=oled_DC, chip_select=oled_CS, reset=oled_RST)

    display = adafruit_displayio_sh1107.SH1107(display_bus,width=OLED_W, height=OLED_H,rotation=0)



    # Make the display context
    splash = displayio.Group()
    display.root_group = splash
    
    print("Display Found")
    
    
except Exception as e:
     print("No Screen Detected", e)
#_________________________________________________________________________________________________________________________________________________#
#Screen Driver:
     
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White

# Select Square
sm_bitmap = displayio.Bitmap(8, 8, 1)
sm_square1 = displayio.TileGrid(sm_bitmap, pixel_shader=color_palette, x=92, y=4)
sm_square2 = displayio.TileGrid(sm_bitmap, pixel_shader=color_palette, x=92, y=16)
sm_square3 = displayio.TileGrid(sm_bitmap, pixel_shader=color_palette, x=92, y=28)
sm_square4 = displayio.TileGrid(sm_bitmap, pixel_shader=color_palette, x=92, y=40)
sm_square5 = displayio.TileGrid(sm_bitmap, pixel_shader=color_palette, x=92, y=52)

#Main Menu Text Options
text1 = "Volume Control"  # overly long to see where it clips
text_area1 = label.Label(terminalio.FONT, text=text1, color=0xFFFFFF, x=8, y=8)

text2 = "Github Token"  # overly long to see where it clips
text_area2 = label.Label(terminalio.FONT, text=text2, color=0xFFFFFF, x=8, y=20)

text3 = "AutoClicker"  # overly long to see where it clips
text_area3 = label.Label(terminalio.FONT, text=text3, color=0xFFFFFF, x=8, y=32)

text4 = "Macro Set 4"  # overly long to see where it clips
text_area4 = label.Label(terminalio.FONT, text=text4, color=0xFFFFFF, x=8, y=44)

text5 = "Macro Set 5"  # overly long to see where it clips
text_area5 = label.Label(terminalio.FONT, text=text5, color=0xFFFFFF, x=8, y=56)

text6 = "Macro Set 6"  # overly long to see where it clips
text_area6 = label.Label(terminalio.FONT, text=text6, color=0xFFFFFF, x=8, y=8)

text7 = "Macro Set 7"  # overly long to see where it clips
text_area7 = label.Label(terminalio.FONT, text=text7, color=0xFFFFFF, x=8, y=20)

text8 = "Macro Set 8"  # overly long to see where it clips
text_area8 = label.Label(terminalio.FONT, text=text8, color=0xFFFFFF, x=8, y=32)

text9 = "Macro Set 9"  # overly long to see where it clips
text_area9 = label.Label(terminalio.FONT, text=text9, color=0xFFFFFF, x=8, y=44)

text10 = "REBOOT"  # overly long to see where it clips
text_area10 = label.Label(terminalio.FONT, text=text10, color=0xFFFFFF, x=8, y=56)

#Reboot Assets
text_R = "REBOOTING"  # overly long to see where it clips
text_area_R = label.Label(terminalio.FONT, text=text_R, color=0xFFFFFF, x=38, y=32)
text_R5 = "5"  # overly long to see where it clips
text_area_R5 = label.Label(terminalio.FONT, text=text_R5, color=0xFFFFFF, x=95, y=32)
text_R4 = "4"  # overly long to see where it clips
text_area_R4 = label.Label(terminalio.FONT, text=text_R4, color=0xFFFFFF, x=95, y=32)
text_R3 = "3"  # overly long to see where it clips
text_area_R3 = label.Label(terminalio.FONT, text=text_R3, color=0xFFFFFF, x=95, y=32)
text_R2 = "2"  # overly long to see where it clips
text_area_R2 = label.Label(terminalio.FONT, text=text_R2, color=0xFFFFFF, x=95, y=32)
text_R1 = "1"  # overly long to see where it clips
text_area_R1 = label.Label(terminalio.FONT, text=text_R1, color=0xFFFFFF, x=95, y=32)
