#!/usr/bin/env python
# Code to record Hall Detector events and convert into flow rate
# Code created by T.G. Cleveland 6 FEB 2019
# Base Code from : https://raspberrypi.stackexchange.com/questions/34480
# This code will operate two different flow meters, modify if only using a single meter
#
# Tested (no sensor) 6 FEB 2019 - exit keyboard OK
#                               - syntax check OK
#
#                    5 JUN 2019 - modify for fixed run length
#                               - fixed run length OK
#                               - modify for multiple sensors
#
#                   11 MAR 2022 - refactor to append to an output file for
#                               - near real-time reporting
import RPi.GPIO as GPIO
import time,sys
from datetime import datetime
#
print('FlowMeterRecord running')
### set the sensor pin ###
flow_sensor_one = 23
### configure GPIO ###
GPIO.setmode(GPIO.BCM)
GPIO.setup(flow_sensor_one, GPIO.IN, pull_up_down = GPIO.PUD_UP)

### initialize counter(s) ###
global count # make count globally accessible to subfunctions
count = 0
### define a counter method ###
def countPulse(channel):
   global count
   if start_counter == 1:
      count = count + 1
### configure GPIO event process ###
GPIO.add_event_detect(flow_sensor_one, GPIO.FALLING, callback=countPulse)
### User inputs - Label Line 1 ###
stationID = input("Enter Comment Line 1 (default: Line 001): ")
if not stationID.strip():  # Check if input is blank or just whitespace
    stationID = "Line 001"  # Set the default value
print(f"Station ID set to: {stationID}")
### User inputs - Label Line 2 ###
sensorID = input("Enter Comment Line 2 (default: Line 002): ")
if not sensorID.strip():  # Check if input is blank or just whitespace
    sensorID = "Line 002"  # Set the default value
print(f"sensor ID set to: {sensorID}")
### User inputs -  dewll time ###
while True:
    try:
        # Prompt user for input
        user_input = input("Enter dwell time (default: 1.0): ").strip()
        
        # Check if input is blank and assign default value
        if not user_input:
            howmany2wait = 1.0
        else:
            # Attempt to convert to float
            howmany2wait = float(user_input)
        
        # If valid, break the loop
        print(f"Dwell time set to: {howmany2wait}")
        break
    
    except ValueError:
        # Handle non-numeric values and assign default
        print("Invalid input. Using default value of 1.0.")
        howmany2wait = 1.0
        break
### User inputs -  how many intervals of length dwell time. ###
while True:
    try:
        # Prompt user for input
        user_input = input("How many intervals (default: 60): ").strip()
        
        # Check if input is blank and assign default value
        if not user_input:
            howmany2read = 60
        else:
            # Attempt to convert to float and cast to int
            howmany2read = int(round(float(user_input)))
        
        # Validate the input is greater than 1
        if howmany2read < 2:
            raise ValueError("Number of intervals must be greater than 1.")
        
        # If valid, break the loop
        print(f"Number of intervals set to: {howmany2read}")
        break
    
    except (ValueError, TypeError):
        # Handle non-numeric values or invalid intervals
        print("Invalid input. Using default value of 60.")
        howmany2read = 60
        break
### User inputs -  meter constant. ###
while True:
    try:
        # Prompt user for input
        user_input = input("Enter the meter constant (a number greater than 0, default: 1.0): ").strip()
        
        # Use default value if input is blank
        if not user_input:
            meterconstant = 1.0
        else:
            # Attempt to convert the input to a float
            meterconstant = float(user_input)

        # Validate that the number is greater than zero
        if meterconstant <= 0:
            raise ValueError("The number must be greater than zero.")

        # If valid, break the loop
        print(f"Meter constant set to: {meterconstant}")
        break

    except ValueError as e:
        # Handle invalid input
        print(f"Invalid input: {e}")

    except KeyboardInterrupt:
        # Gracefully handle keyboard interrupt and exit loop
        print("\nExiting...")
        break


#filename = Afile.readline().rstrip('\n')

### initialize accumulator counters ###
accCount = 0
howmanyRread = 0
# set up header for the output
print('# Flowmeter Recording System ')
print('# ' + stationID),
print('# ' + sensorID),
print('# Sampling Interval Duration (seconds) ' + str(howmany2wait))
print('# Sampling Interval Count (Count * Duration = Elaped Time) ' + str(howmany2read))
print('# Events is number of counted pulses for a sampling interval')
print('# Volume is computed volume in liters for a sampling interval')
print('# 1 and 2 are the two sampling channels; Pin 16 & 18 (GPIO 23 & 24)')
print('DateTime' + ', Events1' + ', Events2 ' + ', Volume1 ' + ', Volume2 ')
#externalfile=open(filename,'a') # output file to append to
# run the datalogger for howmany2read minutes
while True:
   try:
      if howmanyRread >= howmany2read :
         print('\ntime to die!')
         print(' Total Events1 = ' + str(accCount))
         print(' Total Volume1 = ' + str(meterconstant*accCount))
         enow = time.strftime("%a %b %d %Y") # capture system time
         GPIO.cleanup()
         sys.exit()
      howmanyRread = howmanyRread + 1
      start_counter = 1

      time.sleep(howmany2wait)
      start_counter = 0

      flow  = (count *  meterconstant  )

      if howmany2wait < 1.0:
       # Use datetime.now() for microseconds when howmany2wait is less than 1.0
          now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
      else:
    # Use time.strftime for seconds when howmany2wait is greater than or equal to 1.0
          now = time.strftime("%c")

      #now = time.strftime("%c") # capture system time
#      now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f") #alternate form to capture microseconds
      print(now + ' , ' + str(count) + ' , ' + str(flow))
      
      accCount = accCount + count

      count = 0

      time.sleep(0)
   except KeyboardInterrupt:
      print('\ncaught keyboard interrupt!, bye')
      print(' Total Events1 = ' + str(accCount))
      print(' Total Volume1 = ' + str(meterconstant*accCount))
      GPIO.cleanup()
      sys.exit()

 
