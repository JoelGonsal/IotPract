import time
import matplotlib.pyplot as plt
from drawnow import drawnow
import Adafruit_ADS1x15

# Create an ADS1115 ADC (16-bit) instance
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
val = []
cnt = 0

plt.ion()  # Enable interactive mode for live plotting

# Function to create the figure
def makeFig():
    plt.ylim(-5000, 5000)
    plt.title('Oscilloscope')
    plt.grid(True)
    plt.ylabel('ADC outputs')
    plt.plot(val, 'ro-', label='Channel 0')
    plt.legend(loc='lower right')

# Start continuous ADC conversions on channel 0 using the previous gain value
adc.start_adc(0, gain=GAIN)
print('Reading ADS1x15 channel 0')

while True:
    # Read the ADC value from channel 0
    value = adc.get_last_result()
    print('Channel 0: {0}'.format(value))  # Print the ADC value

    # Append the value to the list
    val.append(value)

    # Update the plot
    drawnow(makeFig)

    # Pause for a short interval
    plt.pause(0.000001)

    # Joel Gonsalves 112
    cnt += 1
    if cnt > 50:
        val.pop(0)  # Remove the oldest value to maintain a fixed length

#vdd - 2
#gnd - 6
#scl - 5
#sda - 3
