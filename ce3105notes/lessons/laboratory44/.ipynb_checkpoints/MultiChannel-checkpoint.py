#!/usr/bin/env python
# Analog to Digital Converter and Multichannel Recorder
# T.G. Cleveland 2019. Script refactored and reviewed with guidance from OpenAI's ChatGPT. Enhancements included modularization, input validation, time-setting functionality, and general improvements for maintainability and usability. Date of assistance: January 2025.

import RPi.GPIO as GPIO
import time
from RPLCD.gpio import CharLCD

# GPIO Pin Definitions
SPICLK = 23
SPIMISO = 21
SPIMOSI = 19
SPICS = 24
pin_rs = 37
pin_e = 35
D4 = 33
D5 = 31
D6 = 29
D7 = 32

# Configurable Parameters
CHANNELS = 8
DEFAULT_SAMPLING_INTERVAL = 1  # seconds
MAX_READS = 600  # Upper bound on total traverses

# Initialize GPIO
def init_gpio():
    GPIO.setwarnings(False)
    GPIO.cleanup()  # Clean up at the end of your script
    GPIO.setmode(GPIO.BOARD)  # Use board pin numbering
    GPIO.setup(SPIMOSI, GPIO.OUT)
    GPIO.setup(SPIMISO, GPIO.IN)
    GPIO.setup(SPICLK, GPIO.OUT)
    GPIO.setup(SPICS, GPIO.OUT)
    GPIO.setup(pin_rs, GPIO.OUT)
    GPIO.setup(pin_e, GPIO.OUT)
    GPIO.setup(D4, GPIO.OUT)
    GPIO.setup(D5, GPIO.OUT)
    GPIO.setup(D6, GPIO.OUT)
    GPIO.setup(D7, GPIO.OUT)

# Read SPI data from MCP3008 chip
def read_adc(channel, clockpin, mosipin, misopin, cspin):
    if channel < 0 or channel > 7:
        return -1
    GPIO.output(cspin, True)
    GPIO.output(clockpin, False)  # Start clock low
    GPIO.output(cspin, False)  # Bring CS low

    commandout = channel
    commandout |= 0x18  # Start bit + single-ended bit
    commandout <<= 3  # Only 5 bits are sent
    for _ in range(5):
        GPIO.output(mosipin, bool(commandout & 0x80))
        commandout <<= 1
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)

    adcout = 0
    # Read in 12 bits (1 null bit, 1 empty bit, 10 ADC bits)
    for _ in range(12):
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)
        adcout <<= 1
        if GPIO.input(misopin):
            adcout |= 0x1

    GPIO.output(cspin, True)
    adcout >>= 1  # Drop the null bit
    return adcout

# Log data to console
def log_adc_data(channel, value):
    now = time.strftime("%c")  # Capture actual time
    print(f"{now} | CH: {channel} | ADCVal: {value}")

# Main function
def main():
    init_gpio()
    time.sleep(2)  # Allow time for setup
    print("Multi-Channel Data Logger")
    print("Experiment: Sequential polling of channels 0 through 7.")
    print("Data Format: Weekday Month Day HH:MM:SS Year | CH: <Channel> | ADCVal: <Value>")
    print("-" * 50)

    reads = 0  # Track total reads

    try:
        while reads < MAX_READS:
            for channel in range(CHANNELS):
                adc_value = read_adc(channel, SPICLK, SPIMOSI, SPIMISO, SPICS)
                log_adc_data(channel, adc_value)
                time.sleep(DEFAULT_SAMPLING_INTERVAL / CHANNELS)  # Spread sampling evenly
            reads += 1

        print("Maximum read limit reached. Exiting...")
    except KeyboardInterrupt:
        print("Script interrupted by user.")
    finally:
        GPIO.cleanup()
        print("GPIO cleaned up.")

# Run the program
if __name__ == '__main__':
    main()