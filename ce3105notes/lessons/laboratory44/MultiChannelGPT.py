import RPi.GPIO as GPIO
import time

# GPIO Pin Definitions
SPICLK = 23
SPIMISO = 21
SPIMOSI = 19
SPICS = 24

# Configurable Parameters
CHANNELS = 8

# Initialize GPIO
def init_gpio():
    GPIO.setwarnings(False)
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(SPIMOSI, GPIO.OUT)
    GPIO.setup(SPIMISO, GPIO.IN)
    GPIO.setup(SPICLK, GPIO.OUT)
    GPIO.setup(SPICS, GPIO.OUT)

# Read SPI data from MCP3008 chip
def read_adc(channel, clockpin, mosipin, misopin, cspin):
    if channel < 0 or channel > 7:
        return -1
    GPIO.output(cspin, True)
    GPIO.output(clockpin, False)
    GPIO.output(cspin, False)

    commandout = channel
    commandout |= 0x18
    commandout <<= 3
    for _ in range(5):
        GPIO.output(mosipin, bool(commandout & 0x80))
        commandout <<= 1
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)

    adcout = 0
    for _ in range(12):
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)
        adcout <<= 1
        if GPIO.input(misopin):
            adcout |= 0x1

    GPIO.output(cspin, True)
    adcout >>= 1
    return adcout

# Log data to console and optionally to file
def log_adc_data(channel, value, log_file=None):
    now = time.strftime("%c")
    log_message = f"{now} | CH: {channel} | ADCVal: {value}"
    print(log_message)
    if log_file:
        log_file.write(log_message + '\n')

# Main function
def main():
    init_gpio()
    print("Multi-Channel Data Logger")

    # User inputs
    output_file_name = input("Enter output file name (default: multichannel.junk.txt): ") or "multichannel.junk.txt"
    sampling_interval = float(input("Enter sampling interval (seconds, default: 1): ") or 1.0)
    max_reads = int(input("Enter total number of cycles (default: 600): ") or 600)

    try:
        with open(output_file_name, "w") as log_file:
            for _ in range(max_reads):
                for channel in range(CHANNELS):
                    adc_value = read_adc(channel, SPICLK, SPIMOSI, SPIMISO, SPICS)
                    log_adc_data(channel, adc_value, log_file=log_file)
                    time.sleep(sampling_interval / CHANNELS)
            print("Data collection complete.")
    except KeyboardInterrupt:
        print("Script interrupted by user.")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()