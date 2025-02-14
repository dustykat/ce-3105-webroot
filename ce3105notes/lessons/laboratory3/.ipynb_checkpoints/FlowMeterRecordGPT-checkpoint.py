#!/usr/bin/env python
import RPi.GPIO as GPIO
import time, sys
from datetime import datetime
import subprocess

# Initialize GPIO
def setup_gpio(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    return pin

# Count pulses
def count_pulse(channel):
    global count
    if start_counter == 1:
        count += 1

# Get validated user input
def get_user_input(prompt, default, value_type, validation=None):
    while True:
        try:
            user_input = input(f"{prompt} (default: {default}): ").strip()
            if not user_input:
                return default
            value = value_type(user_input)
            if validation and not validation(value):
                raise ValueError(f"Input does not meet validation criteria.")
            return value
        except (ValueError, TypeError):
            print(f"Invalid input. Using default value of {default}.")
            return default

# Set system time
def set_system_time():
    try:
        new_time = input("Enter new system time (YYYY-MM-DD HH:MM:SS) or press Enter to skip: ").strip()
        if new_time:
            subprocess.run(["sudo", "date", "-s", new_time], check=True)
            print(f"System time updated to: {new_time}")
        else:
            print("System time unchanged.")
    except subprocess.CalledProcessError:
        print("Failed to update system time. Ensure the script runs with sufficient privileges.")

# Main Program
print("FlowMeterRecord running")

# User Inputs
stationID = get_user_input("Enter Comment Line 1", "Line 001", str)
sensorID = get_user_input("Enter Comment Line 2", "Line 002", str)
howmany2wait = get_user_input("Enter dwell time", 1.0, float, lambda x: x > 0)
howmany2read = get_user_input("How many intervals", 60, int, lambda x: x >= 2)
meterconstant = get_user_input("Enter the meter constant", 1.0, float, lambda x: x > 0)

# Optional: Set system time
set_system_time()

# GPIO Setup
flow_sensor_one = setup_gpio(23)
GPIO.add_event_detect(flow_sensor_one, GPIO.FALLING, callback=count_pulse)

# Initialize counters
count = accCount = howmanyRread = 0

# Print headers
print("# Flowmeter Recording System")
print(f"# {stationID}")
print(f"# {sensorID}")
print(f"# Sampling Interval Duration (seconds): {howmany2wait}")
print(f"# Sampling Interval Count: {howmany2read}")
print("# DateTime, Events, Volume")

# Main loop
try:
    while howmanyRread < howmany2read:
        howmanyRread += 1
        start_counter = 1
        time.sleep(howmany2wait)
        start_counter = 0

        flow = count * meterconstant
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f") if howmany2wait < 1.0 else time.strftime("%c")

        print(f"{now}, {count}, {flow}")
        accCount += count
        count = 0
    print("\nNormal Loop Exit, exiting...")
    print(f"Total Events: {accCount}")
    print(f"Total Volume: {accCount * meterconstant}")

except KeyboardInterrupt:
    print("\nCaught keyboard interrupt, exiting...")
    print(f"Total Events: {accCount}")
    print(f"Total Volume: {accCount * meterconstant}")
    GPIO.cleanup()
    sys.exit()
finally:
    GPIO.cleanup()
