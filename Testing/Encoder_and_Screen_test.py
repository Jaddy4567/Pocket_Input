#_________________________________________________________________________________________________________________________________________________#

#import Libraries
import time
import board
import rotaryio
import digitalio
import usb_hid
import displayio, os, terminalio
# from Screen_Driver import *
from adafruit_hid.keyboard_layout_us import KeyboardLayoutBase
from Inputs import *
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_matrixkeypad import Matrix_Keypad
from adafruit_display_text import label
import adafruit_displayio_sh1107
 
#_________________________________________________________________________________________________________________________________________________#
mouse = Mouse(usb_hid.devices)
#Test Button
CPS_SWT = digitalio.DigitalInOut(board.GP14)
CPS_SWT.direction = digitalio.Direction.INPUT
CPS_SWT.pull = digitalio.Pull.UP

CPS_BTN = digitalio.DigitalInOut(board.GP15)
CPS_BTN.direction = digitalio.Direction.INPUT
CPS_BTN.pull = digitalio.Pull.UP

E_BTN = digitalio.DigitalInOut(board.GP26)
E_BTN.direction = digitalio.Direction.INPUT
E_BTN.pull = digitalio.Pull.DOWN

SWITCHER = 0

def Click_Active():
    global SWITCHER
    SWITCHER = SWITCHER+1
    if SWITCHER >= 2:
        SWITCHER = 0
    print("Click Active:", SWITCHER)
    
#_________________________________________________________________________________________________________________________________________________#
#Encoder Setup
encoder = rotaryio.IncrementalEncoder(board.GP27, board.GP28)

last_position = encoder.position
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
     print("No Screen Detected")
#_________________________________________________________________________________________________________________________________________________#
#Screen Driver:

text1 = "Macro Set 1"  # overly long to see where it clips
text_area1 = label.Label(terminalio.FONT, text=text1, color=0xFFFFFF, x=8, y=8)

text2 = "Macro Set 2"  # overly long to see where it clips
text_area2 = label.Label(terminalio.FONT, text=text2, color=0xFFFFFF, x=8, y=8)

text3 = "Macro Set 3"  # overly long to see where it clips
text_area3 = label.Label(terminalio.FONT, text=text3, color=0xFFFFFF, x=8, y=8)

text4 = "Macro Set 4"  # overly long to see where it clips
text_area4 = label.Label(terminalio.FONT, text=text4, color=0xFFFFFF, x=8, y=8)

text5 = "Macro Set 5"  # overly long to see where it clips
text_area5 = label.Label(terminalio.FONT, text=text5, color=0xFFFFFF, x=8, y=8)

text6 = "Macro Set 6"  # overly long to see where it clips
text_area6 = label.Label(terminalio.FONT, text=text6, color=0xFFFFFF, x=8, y=8)

def Screen_Driver():
    
    global SET
    try:
        if SET == 1:
            try:
                splash.remove(text_area2)
            except Exception as e:
                ("Failed to remove group or no group to remove ", e)
            splash.append(text_area1)
            
        elif SET== 2:
            try:
                try:
                    splash.remove(text_area1)
                except:
                    splash.remove(text_area3)
            except Exception as e:
                print ("Failed to remove group ", e)
            splash.append(text_area2)

        elif SET == 3:
            try:
                try:
                    splash.remove(text_area2)
                except:
                    splash.remove(text_area4)
            except Exception as e:
                print ("Failed to remove group ", e)
                
            splash.append(text_area3)
        elif SET == 4:
            try:
                try:
                    splash.remove(text_area3)
                except:
                    splash.remove(text_area5)
            except Exception as e:
                print ("Failed to remove group ", e)

            splash.append(text_area4)
        elif SET == 5:
            try:
                try:
                    splash.remove(text_area4)
                except:
                    splash.remove(text_area6)
            except Exception as e:
                print ("Failed to remove group ", e)

            splash.append(text_area5)
        elif SET == 6:
            try:
                splash.remove(text_area5)
            except Exception as e:
                ("Failed to remove group or no group to remove ", e)
            splash.append(text_area6)
        

    except Exception as e:
        print("No Screen Detected")
        print(e)
        
def Screen_driver3():
    try:
        if SWITCHER == 0:
            lcd.clear()
            Screen_Driver()
        elif SWITCHER == 1:
            lcd.clear()
            lcd.set_cursor_pos(0,0)
            time.sleep(0.0000000000001)
            lcd.print("Click Active")
    except Exception as e:
        print("No LCD Detected")

#_________________________________________________________________________________________________________________________________________________#

#RGB Setup and Driver:


Red_LED = digitalio.DigitalInOut(board.GP19)
Red_LED.direction = digitalio.Direction.OUTPUT
Green_LED = digitalio.DigitalInOut(board.GP20)
Green_LED.direction = digitalio.Direction.OUTPUT
Blue_LED = digitalio.DigitalInOut(board.GP21)
Blue_LED.direction = digitalio.Direction.OUTPUT

def RGB_Driver():
    
    global SET
    if SET == 1:
        Green_LED.value = True
        Blue_LED.value = True
        Red_LED.value = False
    elif SET== 2:
        Green_LED.value = False
        Blue_LED.value = True
        Red_LED.value = True
    elif SET == 3:
        Green_LED.value = True
        Blue_LED.value = False
        Red_LED.value = True
    elif SET == 4:
        Green_LED.value = False
        Blue_LED.value = False
        Red_LED.value = True
    elif SET == 5:
        Green_LED.value = True
        Blue_LED.value = False
        Red_LED.value = False
    elif SET == 6:
        Green_LED.value = False
        Blue_LED.value = True
        Red_LED.value = False
#_________________________________________________________________________________________________________________________________________________#
#Creating the global "SET" value:
SET = 1

def Macro_Set_increase():
    global SET
    SET = SET+1
    if SET >= 7:
        SET = 6
    print("Macro Set", SET)
    
def Macro_Set_decrese():
    global SET
    
    SET = SET-1
    if SET <= 0:
        SET = 1
    print("Macro Set", SET)
    
#_________________________________________________________________________________________________________________________________________________#
#Creating the global "SET" value:
CPS = 0.25

def CPS_increase():
    global CPS
    CPS = CPS+0.25
    if CPS >= 10.25:
        CPS = 10
    print("CPS:", CPS)
    
def CPS_decrese():
    global CPS
    
    CPS = CPS-0.25
    if CPS <= 0:
        CPS = 0.25
    print("CPS:", CPS)
#_________________________________________________________________________________________________________________________________________________#
#clicking function
def Clicking():
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(CPS)
    
#_________________________________________________________________________________________________________________________________________________#
#Screen Driver 2
def Screen_Driver2():
    
    global CPS
    
    if CPS == 0.25:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("0.25s")
    elif CPS== 0.5:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("0.50s")
    elif CPS == 0.75:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("0.75s")
    elif CPS == 1:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("1.00s")
    elif CPS == 1.25:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("1.25s")
    elif CPS == 1.5:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("1.50s")
    elif CPS == 1.75:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("1.75s")
    elif CPS == 2:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("2.00s")
    elif CPS == 2.25:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("2.25s")
    elif CPS == 2.5:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("2.50s")
    elif CPS== 2.25:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("2.75s")
    elif CPS== 3:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("3.00")
    elif CPS== 3.25:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("3.25s")
    elif CPS == 3.5:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("3.50s")
    elif CPS == 3.75:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("3.75s")
    elif CPS == 4:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("4.00s")
    elif CPS == 4.25:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("4.25s")                
    elif CPS == 4.5:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("4.50s")
    elif CPS == 4.75:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("4.75s")
    elif CPS == 5:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("5.00s")
    elif CPS == 5.25:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("5.25s")                
    elif CPS == 5.5:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("5.50s")
    elif CPS == 5.75:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("5.75s")
    elif CPS == 6:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("6.00s")
    elif CPS == 6.25:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("6.25s")                
    elif CPS == 6.5:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("6.50s")
    elif CPS == 6.75:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("6.75s")
    elif CPS == 7:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("7.00s")
    elif CPS == 7.25:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("7.25s")                
    elif CPS == 7.5:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("7.50s")
    elif CPS == 7.75:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("7.75s")
    elif CPS == 8:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("8.00s")
    elif CPS == 8.25:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("8.25s")                
    elif CPS == 8.5:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("8.50s")
    elif CPS == 8.75:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("8.75s")
    elif CPS == 9:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("9.00s")
    elif CPS == 9.25:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("9.25s")                
    elif CPS == 9.5:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("9.50s")
    elif CPS == 9.75:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("9.75s")
    elif CPS == 10:
        lcd.set_cursor_pos(1,0)
        lcd.clear
        lcd.print("10.0s")
#_________________________________________________________________________________________________________________________________________________#

#Main Loop:
while True:
    if E_BTN.value:
        Click_Active()
        time.sleep(0.01)
        Screen_Driver2()
        time.sleep(0.01)
        Screen_driver3()
        time.sleep(0.25)
        
    if not CPS_SWT.value:
        Clicking()

    if not CPS_BTN.value:
        Clicking()
        
    #Macro Sets
    if SET == 1:
        Macro_Set_1()
        time.sleep(0.05)
    elif SET == 2:
        Macro_Set_2()
        time.sleep(0.05)
    elif SET == 3:
        Macro_Set_3()
        time.sleep(0.05)
    elif SET == 4:
        Macro_Set_4()
        time.sleep(0.05)
    elif SET == 5:
        Macro_Set_5()
        time.sleep(0.05)
    elif SET == 6:
        Macro_Set_6()
        time.sleep(0.05)

    #Rotary Encoder
    if SWITCHER == 0:
        current_position = encoder.position
        position_change = current_position - last_position
        if position_change > 0:
            for _ in range(position_change):
                Macro_Set_decrese()
                Screen_Driver()
                RGB_Driver()
#         	print(current_position)
        elif position_change < 0:
            for _ in range(-position_change):
                Macro_Set_increase()
                Screen_Driver()
                RGB_Driver()
#         	print(current_position)
        last_position = current_position

    if SWITCHER == 1:
        current_position = encoder.position
        position_change = current_position - last_position
        if position_change > 0:
            for _ in range(position_change):
                CPS_decrese()
                Screen_Driver2()
#         	print(current_position)
        elif position_change < 0:
            for _ in range(-position_change):
                CPS_increase()
                Screen_Driver2()
#         	print(current_position)
        last_position = current_position
    


    
