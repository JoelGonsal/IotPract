import sys
import time
import tm1637
import datetime
import RPi.GPIO as GPIO

Display = tm1637.TM1637(23, 24, tm1637.BRIGHT_TYPICAL)
Display.Clear()
Display.SetBrightness(1)

while True:
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second

    currenttime = [
        int(hour / 10), hour % 10,
        int(minute / 10), minute % 10
    ]

    Display.Show(currenttime)
    Display.ShowDoublepoint(second % 2)  # Show the colon blinking
    time.sleep(1)

#clk - 16
#dio - 18
#vcc - 4
#gnd - 14
