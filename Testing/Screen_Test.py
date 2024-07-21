# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
"""
Author: Mark Roberts (mdroberts1243) from Adafruit code
This test will initialize the display using displayio and draw a solid white
background, a smaller black rectangle, miscellaneous stuff and some white text.

"""


import board, busio, displayio, os, terminalio

# can try import bitmap_label below for alternative
from adafruit_display_text import label
import adafruit_displayio_sh1107

displayio.release_displays()
# oled_reset = board.D9

board_type = os.uname().machine
print(f"Board: {board_type}")

oled_SCL = board.GP7
oled_SDA = board.GP6
oled_RST = board.GP12
oled_DC = board.GP8
oled_CS = board.GP9

# 128x128 SH1107
OLED_W = 128
OLED_H = 64

oled_spi = busio.SPI(clock=board.GP10, MOSI=board.GP11)
display_bus = displayio.FourWire(oled_spi, command=oled_DC, chip_select=oled_CS, reset=oled_RST)

display = adafruit_displayio_sh1107.SH1107(
    display_bus,
    width=OLED_W, height=OLED_H,

    rotation=0)



# Make the display context
splash = displayio.Group()
display.root_group = splash


# Draw some label text
text1 = "Testing code"  # overly long to see where it clips
text_area = label.Label(terminalio.FONT, text=text1, color=0xFFFFFF, x=8, y=8)
splash.append(text_area)
text2 = "Lol"
text_area2 = label.Label(terminalio.FONT, text=text2, scale=2, color=0xFFFFFF, x=9, y=44   )
splash.append(text_area2)
text3 = "TEXT 3!!!!"
text_area3 = label.Label(terminalio.FONT, text=text3, scale=3, color=0xFFFFFF, x=50, y=44   )
splash.append(text_area3)

while True:
    pass
