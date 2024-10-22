import RPi.GPIO as GPIO
import time

# Set up the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up the LED pins
LED_PINS = [23, 18, 24, 25, 8, 7]  # Use a list for multiple pins
GPIO.setup(LED_PINS, GPIO.OUT)

print("Joel Gonsalves 112")

try:
    while True:
        # Turn the LEDs on
        GPIO.output(LED_PINS, GPIO.HIGH)
        time.sleep(0.5)  # Keep them on for 0.5 seconds

        # Turn the LEDs off
        GPIO.output(LED_PINS, GPIO.LOW)
        time.sleep(0.5)  # Keep them off for 0.5 seconds

except KeyboardInterrupt:
    # Clean up GPIO on CTRL+C exit
    GPIO.cleanup()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Clean up GPIO on normal exit
    GPIO.cleanup()

#G23-16
#G18-12
#G24-18
#G25-22
#G8-24
#G7-26
#GND - 6
