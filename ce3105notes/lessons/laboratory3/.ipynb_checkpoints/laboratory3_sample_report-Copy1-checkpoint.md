# Laboratory 3 Sample Report

## Flow Measurement

### 1. Introduction

The purpose of this laboratory exercise is to determine the flow rate of an incompressible fluid using various flow measurement devices, including Venturi meter, orifice plate meter, and rotameter, and to evaluate their accuracy and suitability for subsequent measurements.

### 2. Experimental Method

#### Apparatus and Materials
- Hydraulic bench with adjustable flow control
- Venturi meter
- Orifice plate meter
- Rotameter
- Stopwatch
- Measuring beaker
- Manometer tubes
- Raspberry Pi Zero-W computer
- Mass Flow Meter
- Safety goggles

#### Procedure
1. **Setup Preparation**:
   - Close all valves and ensure the hydraulic bench pump is turned off.
   - Connect the Venturi meter, orifice plate meter, and rotameter to the hydraulic bench in series.

2. **Flow Initialization**:
   - Open the inlet valve gradually.
   - Start the pump and adjust the discharge valve until the rotameter indicates a reading of approximately 10 mm.
   
3. **Data Collection**:
   - Use the beaker and stopwatch to measure volumetric discharge at the outlet.  Usually record time to fill the beaker, repeat several times (at least 3), then compute the average time to fill the beaker.
   - Record the rotameter and manometer readings for each flow condition.
   - Incrementally increase the rotameter reading to approximately 220 mm, recording at least five measurements.
   - Connect to the Raspberry Pi computer, find and start the measurement program (the instructor will usually get this working in advance as well as plumb the mass flow meter into the system); you can either program it to read meter counts or liters.
   - Collect adequate readings to populate the data tables below (be sure you have 5 different flow rates)

4. **Shutdown**:
   - Stop the mass flow meter program (do an elegant exit from the program).
   - Turn off the Raspberry Pi (from the console type "sudo shutdown -h now")
   - Close the discharge valve, then the inlet valve, and turn off the pump.

### Safety Considerations
- Always wear safety goggles when handling pressurized systems and adding air to manometers.
- Ensure that the bench and surrounding area are free of obstructions to avoid tripping hazards.
- Follow TA instructions when troubleshooting equipment, especially when dealing with flooded manometer tubes.

### 3. Results
The table below is the actual data collected for five (5) different flow settings.  All the values are direct readings except for the time-to-fill, which are arithmetic means from three repeated measurements.

**Notes**

1. Rotometer outlet heads were not read.
2. Time to fill is arithmetic mean of three readings.

|Quantity                |Device           |Trial 1|Trial 2|Trial 3|Trial 4|Trial 5|
|:-----------------------|:----------------|-----:|-----:|-----:|-----:|-----:|
|        |Venturi-In| 158 | 210 | 170 |  214 | 310 |
|        |Venturi-Out| 110 | 132 | 80  | 90 | 302 |
|        |Expansion-In| 150 | 196| 150 | 192 | 306  |
|        |Expansion-Out| 170 | 192 | 170  |  192  | 302  |
|Manometer Reading    |Orifice-In| 152 | 210 | 162 | 220 | 306  |
|  (mm of water)      |Orfice-Out| 108 | 126 | 70  | 78 | 302 |
|        |Elbow-In| 118 | 140 | 88 | 100|  302 |
|        |Elbow-Out| 117 | 138 |  84 | 96 | 303  |
|        |Rotometer-Out| --  |  --  |  --  | -- |  -- |
|________________________|_________________|______|_______|_______|_______|_______|
|Time to Fill (sec)|Beaker (2L)| 12.49 |  9.06 |  7.6 | 6.71 |  27.55 |
|Counts per second |Mass Flow Meter| 85 | 113 | 122 | 146 | 31 |
|Plummet height (mm) |Rotameter| 75 | 100 | 110 | 130 | 20 |
|________________________|_________________|______|_______|_______|_______|_______|

Formulas employed

1. Venturi: $Q =C_{venturi} A_2~(\frac{2g}{1-\frac{A_2^2}{A_1^2}})~\sqrt{\frac{P_1}{\rho g}-\frac{P_2}{\rho g}} $
2. Expansion: $Q = C_{expansion} \frac{\sqrt{2g(h_1-h_2)}}{\frac{1}{A_1}-\frac{1}{A_2}} $
3. Orifice: $Q =  C_{orifice} A_u~(\frac{2g}{1-\frac{A_d^2}{A_u^2}})~\sqrt{\frac{P_u}{\rho g}-\frac{P_d}{\rho g}} $
4. Flow Meter: $Q = C_{meter} \frac{\text{count}}{\text{dwell interval}} $

Scripts to accomplish the calculations are included below.

The table below is populated with calculated values.  The flow rates are computed using the formulas listed above with meter constants set to 1.0. Once these flows are computed the appropriate meter constant is computed from the *true* flow, which is the value determined using the beaker and stopwatch.  These meter constants appear in the following table.

**Notes**

1. Flows in table are with meter constant of unity.
2. Elbow not useful to meter flow, $\Delta h$ values are too small (unreadable)

|Quantity                |Device           |Trial 1|Trial 2|Trial 3|Trial 4|Trial 5|
|:-----------------------|:----------------|-----:|-----:|-----:|-----:|-----:|
|Volume Flow (l/sec)|Beaker|0.1601|0.2208|0.2632|0.2981|0.0726|
|Volume Flow (l/sec)|Venturi|1.0082|1.2852|1.3806|1.6205|0.4116|
|Volume Flow (l/sec)|Expansion|0.4437|0.1984|0.4437|0.1403|0.1984|
|Volume Flow (l/sec)|Orifice|8.8957|12.2911|12.8631|15.9807|2.6821|
|Volume Flow (l/sec)|Elbow|--|--|--|--|--|
|________________________|_________________|______|_______|_______|_______|_______|

The table below is a listing of the meter constants for the various devices.

**Notes**

1. Divide Beaker flow (above) by device flow to determine meter constant; use to populate table below.

|Quantity                |Device           |Trial 1|Trial 2|Trial 3|Trial 4|Trial 5|
|:-----------------------|:----------------|-----:|-----:|-----:|-----:|-----:|
|Meter Constant|Rotameter|0.0021|0.0022|0.0024|0.0023|0.0036|
|Meter Constant|Venturi|0.1587|0.1718|0.1906|0.1839|0.1764|
|Meter Constant|Expansion|0.3608|1.1129|0.5931|2.1247|0.3659|
|Meter Constant|Orifice|0.0179|0.0179|0.0205|0.0186|0.0271|
|Meter Constant|Mass Flow Meter|0.0019|0.002|0.0022|0.002|0.0023|
|________________________|_________________|______|_______|_______|_______|_______|

The flows can be converted to mass flows by multiplication of the flow rate with the specific mass (density) of the liquid.

### 4. Discussion of Experimental Results

The purpose of this experiment was to analyze the accuracy and reliability of different flow measurement devices and compare their performance against theoretical predictions. Each device was calibrated using a stopwatch and beaker—our reference measurement—which provided the most direct and fundamental means of determining flow rate. The devices under evaluation included a mass flow meter (hall effect counter), a venturi device, an expansion fitting, an orifice plate, and a rotameter.

#### Accuracy and Reliability of Devices

Among the devices tested, the mass flow meter, orifice plate, and rotameter demonstrated the most stable performance, returning consistent meter constants across multiple trials. This suggests that their measurement mechanisms are inherently more reliable under our test conditions. The mass flow meter, in particular, relies on a turbine rotation count correlated to flow rate through a predefined meter constant. While the theoretical meter constant was used initially, some deviation from expected values was observed. Refining this constant based on experimental data may yield a more accurate calibration.

|Device           |Meter Constant|Standard Deviation|
|:----------------|-----:|-----:|
|Venturi          |0.1763|0.0122|
|Expansion        |0.0911|0.7441|
|Orifice          |0.0204|0.0039|
|Rotameter        |0.0025|0.0006|
|Mass Flow Meter  |0.0021|0.0001|
|________________________|_________________|______|

In contrast, the venturi device and expansion fitting exhibited significant measurement variability, with standard deviations comparable to or exceeding the mean constant value by an order of magnitude.

One probable source of error was the use of manometers to gauge pressure differences. The manometers proved difficult to read with sufficient precision, and minor fluctuations in fluid levels led to inconsistencies in derived flow rates. Additionally, the pressure changes measured across these devices were not large enough to generate a distinct and meaningful difference between readings, reducing the effectiveness of these methods for accurate flow measurement.

#### Comparison with Theoretical Predictions

Theoretically, each device should follow well-established flow equations—Bernoulli’s equation for differential pressure-based meters (venturi, expansion, orifice plate), empirical correlations for the rotameter, and manufacturer specifications for the mass flow meter. While the mass flow meter and orifice plate remained within expected tolerances, the venturi and expansion fittings deviated significantly. The expansion fitting, in particular, demonstrated poor reliability, reinforcing the idea that it is not a suitable method for precise flow measurement. Its sensitivity to small pressure changes, compounded by possible air entrapment or minor obstructions, likely contributed to its erratic readings.

#### Sources of Error and Their Impact

Several key sources of error influenced our results:

1. Manometer Reading Difficulties – Small fluid level changes were challenging to distinguish, making pressure-based calculations prone to error.
2. Measurement Resolution – Some devices did not produce large enough differences in readings to be reliably distinguished from background variation.
3. Calibration and Meter Constants – The mass flow meter’s performance was dependent on its meter constant. While generally reliable, refining the constant based on experimental results could improve accuracy.
4. Flow Variability – Minor pulsations or fluctuations in flow rate could have introduced additional inconsistencies, particularly in devices sensitive to small changes in pressure.

Overall, while the mass flow meter, orifice plate, and rotameter provided useful and repeatable data, the venturi device and expansion fitting were less effective in this experimental setup. The expansion fitting, in particular, should not be relied upon for accurate flow measurement due to its inherent instability and sensitivity to measurement errors.

### 5. Conclusion
This experiment evaluated the accuracy and reliability of various flow measurement devices, with results highlighting both effective and ineffective methods under the given conditions. The key findings are summarized as follows:

- Reliable Devices: The mass flow meter, orifice plate, and rotameter produced consistent meter constants, indicating that they can be reliably used for flow measurement when properly calibrated. The mass flow meter, in particular, exhibited a very small standard deviation, making it a strong candidate for precise liquid flow measurements, provided the liquid is compatible with its operating materials.

- Unreliable Devices: The venturi device and expansion fitting showed significant variability, with standard deviations on the same order as or exceeding their mean meter constants. This suggests that these devices, under the tested conditions, were ineffective for accurate flow measurement. The primary sources of error were difficulties in reading manometers and insufficient pressure differentials to yield meaningful readings.

- Experimental Validation of Flow Equations: The experimentally determined meter constants will be presented alongside the governing equations for each instrument, demonstrating how theoretical principles apply in practice and where deviations occur. The mass flow meter and orifice plate aligned well with theoretical expectations, while the venturi and expansion devices deviated significantly due to measurement limitations.

---
#### Mass Flow Meter 

The equation for using the mass flow meter is 

$Q = C_{meter} \frac{\text{count}}{\text{dwell interval}} $

with

$C_{meter} = 0.0021$

<font color='green'>**Recomended for measurements in future laboratory experiments**</font> because it is accurate and portable in contrast to the Rotameter which is nearly as accurate, but not moveable (in our lab).

---

#### Rotameter

The equation for using the Rotameter meter is 

$Q = C_{rotameter} ~\text{Plummet Location} $

with

$C_{rotameter} = 0.0025$

<font color='orange'>**Suitable for measurements in future laboratory experiments**</font> because it is accurate, but not moveable to other lab set ups.

---

#### Orifice Plate
The equation for using the orifice plate as a flow meter is 

$Q =  C_{orifice} A_u~(\frac{2g}{1-\frac{A_d^2}{A_u^2}})~\sqrt{\frac{P_u}{\rho g}-\frac{P_d}{\rho g}} $

with

$C_{orifice} = 0.0204$

---
#### Venturi Meter

The equation for using a venturi meter is 

$Q =C_{venturi} A_2~(\frac{2g}{1-\frac{A_2^2}{A_1^2}})~\sqrt{\frac{P_1}{\rho g}-\frac{P_2}{\rho g}} $

with

$C_{venturi} = 0.1763$

<font color='red'>**Not recomended for vital measurements in future laboratory experiments**</font>

---
#### Expansion Meter

The equation for using an expansion as a meter is 

$Q = C_{expansion} \frac{\sqrt{2g(h_1-h_2)}}{\frac{1}{A_1}-\frac{1}{A_2}} $

with

$C_{expansion} = 0.0911$

<font color='red'>**Not recomended for vital measurements in future laboratory experiments**</font>

---

#### Implications for Fluid Mechanics

These findings reinforce the importance of selecting appropriate flow measurement methods based on precision requirements and operating conditions. Devices that rely on pressure differentials must generate sufficiently large and readable values to be effective, while those with inherently stable sensor-based mechanisms, such as the mass flow meter, can provide highly reliable data. The study highlights the necessity of experimental validation in fluid mechanics applications, ensuring that theoretical assumptions align with real-world performance.

### 6. References

1. Holman, J.P., Experimental Methods for Engineers, 8th Ed., McGraw-Hill, 2012.
1. [Engineering Fluid Mechanics - Chapter 2](http://54.243.252.9/ce-3105-webroot/2-Exercises/laboratory1/EFM-2.pdf)
2. [Engineering Fluid Mechanics - Chapter 11 (Cd for spheres, p.414)](http://54.243.252.9/ce-3105-webroot/2-Exercises/laboratory1/EFM-22.pdf)
3. [Holman, J.P. (2012) *Experimental Methods for Engineers*, 8th Ed. (Chapters 1-3)](https://mech.at.ua/HolmanICS.pdf)
4. [Mass Flow Meter & Datalogger Scripts](http://54.243.252.9/ce-3105-webroot/ce3105notes/_build/html/lessons/laboratory3/massflowmeters.html)  Programs used in the laboratory 



### 7. Analysis Scripts


```python
def beakerflow(volume,time2fill):
    beakerflow = volume/time2fill
    return beakerflow

volume = 2 #liters
time2fill = 27.55 #seconds

print("Flow rate by beaker time to fill = ",round(beakerflow(volume,time2fill),4)," liters/second")
```

    Flow rate by beaker time to fill =  0.0726  liters/second



```python
def meterconstant(flowrate,counts):
    meterconstant = flowrate/float(counts)
    return meterconstant

flowrate = 0.0726 #LPS
counts = 31 #counts/dwell time

print("Meter Constant = ",round(meterconstant(flowrate,counts),4)," LPS/count")
```

    Meter Constant =  0.0023  LPS/count



```python
def venturi(cd,a1,a2,h1,h2,g):
    import math
    venturi = cd*a2*((2*g)/(1-(a2**2)/(a1**2)))*math.sqrt(h1-h2)
    return venturi

cventuri = 1.0
area1 = 530.9 #mm^2
area2 = 201.1 #mm^2
h1 = 158 #mm
h2 = 110 #mm
g = 9.800 #m/s^2
area1 = area1/1000/1000
area2 = area2/1000/1000
h1 = h1/1000
h2 = h2/1000

print("Venturi Flow Rate ",round(1000*venturi(cventuri,area1,area2,h1,h2,g),4)," LPS ")
```

    Venturi Flow Rate  1.0082  LPS 



```python
def orifice(cd,a1,a2,h1,h2,g):
    import math
    orifice = cd*a1*((2*g)/(1-(a2**2)/(a1**2)))*math.sqrt(h1-h2)
    return orifice

corifice = 1.0
area1 = 2116 #mm^2
area2 = 314.16 #mm^2
h1 = 306 #mm
h2 = 302 #mm
g = 9.800 #m/s^2
area1 = area1/1000/1000
area2 = area2/1000/1000
h1 = h1/1000
h2 = h2/1000

print("Orifice Flow Rate ",round(1000*orifice(corifice,area1,area2,h1,h2,g),4)," LPS ")
```

    Orifice Flow Rate  2.6821  LPS 



```python
def expansion(cd,a1,a2,h1,h2,g):
    import math
    expansion = cd*math.sqrt(2*g*abs(h1-h2))/((1/a1)-(1/a2))
    return expansion

cexpansion = 1.0
area1 = 530.9 #mm^2
area2 = 2116 #mm^2
h1 = 306 #mm
h2 = 302 #mm
g = 9.800 #m/s^2
area1 = area1/1000/1000
area2 = area2/1000/1000
h1 = h1/1000
h2 = h2/1000

print("Expansion Flow Rate ",round(1000*expansion(cexpansion,area1,area2,h1,h2,g),4)," LPS ")
```

    Expansion Flow Rate  0.1984  LPS 



```python
import math
d = 20/1000
area = 0.25*math.pi*d**2
print("Cross Section Area = ",round(area*1000*1000,3)," sq.mm. ")
```

    Cross Section Area =  314.159  sq.mm. 

