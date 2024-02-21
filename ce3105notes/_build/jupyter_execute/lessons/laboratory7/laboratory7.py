#!/usr/bin/env python
# coding: utf-8

# # 7. Pump Performance
# 
# This laboratory determines performance characteristics of two mechanically identical pumps in various flow configurations.
# 

# ## Background
# 
# ### What is a pump?
# A mechanical device that transfers mechanical energy to move fluid
# - Lift from lower to higher elevation (Lift stations)
# - Increase pressure (Booster stations)
# 
# >Pump Types:
# >- Positive Displacement Pumps (e.g. Archimedes Pumps; Piston Pumps; Progressive Cavity Pumps)
# >  - Fixed volume of fluid is displaced each cycle regardless of static head/pressure
# >  - Low flow rates and higher head than variable displacement pumps
# >-Variable Displacement Pumps (e.g. Axial Pumps; Centrifugal Pumps)
# >  - Volume of fluid is dependent on static head/pressure in system (back pressure)
# 

# ### Pump Hydraulics
# 
# Individual pump performance is based on information from the manufacturer on the performance of pumps in the form of curves.  Information typically includes: 
# - discharge on the x-axis
# - head on the left y-axis
# - pump power input on the right y-axis
# - pump efficiency as a percentage
# - speed of the pump (rpm)
# - NPSH of the pump
# 
# ![](pumpcurve.png)
# 
# Pumps are selected to match system hydraulics (below) for an effective design.

# ### System Hydraulics
# 
# A system (characteristic) curve is a plot of required head versus flow rate in a hydraulic system (H vs. Q) 
# The curve depicts how much energy is necessary to maintain a steady flow under the supplied conditions
# Total head, $H_p$, = elevation head + head losses
# 
# ![](systemcurve.png)
# 
# The system curve is the graphical representation of the system hydraulics such as
# 
# ![](systemequation.png)

# ### Pump Performance/Selection
# 
# A pump is selected to intersect a system curve at a desired design flow rate (usually a range of flows, but a single [operating point](http://54.243.252.9/ce-3305-webroot/ce3305s22book/_build/html/lessons/lesson15/pumpoppoint.html) is fine for discussion) like in the figure below
# 
# ![](operatingpoint.png)
# 
# Different pumps perform differently
# 
# ![](pumpAandB.png) 
# 
# if more flow is desired, usually have to sacrifice added head.  If more head is desired usually have to sacrifice flow.  Hence in many cases multiple pumps are employed to increase pump station flexibility:
# 
# ![](multiplepumps.png)
# 
# Parallel pumps increase total flow rate at about the same added head.
# 
# ![](parallelpumps.png)
# 
# Series pumps increase added head at about the same flow rate.
# 
# ![](seriespumps.png)
# 
# Laboratory 7 uses two identical pumps in a flow circuit that allows either pump to operate independently, or both pumps to operate in series, or parallel configurations.

# ## Apparatus Overview
# 
# The machine is comprised of two pumps with special arrangements of pipework and valves. It is possible to set the pumps in single, parallel and series connections. Water is pumped from a reservoir through one-way valves and strainers. Water flows through inlet valves, pumps, pipework arrangement and directional valves before it goes through the venturi meter back to the reservoir.
# Pressures readings at different locations in the pipework and across the venturi meter can be observed in digital display. Flow can be calculated using the venturi meter. The pipe flow schematic is shown below
# 
# ![](flowcircuit.png)
# 
# A photograph of the test station is annotated in the figure below
# 
# ![](pumpteststation.png)
# 
# Total head is related to the pressure change across the pump:
# 
# $$\rho g H = P_{out}-P_{in}~~~ (1)$$
# 
# It is the difference between the outlet and inlet pressures for single test (with pump 1). 
# 
# For the parallel pump it is the difference between the combined outlet pressure and the average of the two inlet pressures. 
# 
# For the series connection, it is the difference between outlet pressure of the second pump and the inlet pressure of the first pump.
# 
# The total input power (mechanical power) is
# 
# $$W_1 = \frac{2\pi N T}{60}~~~ (2)$$
# 
# The motor drive display calculates the power automatically.
# 
# The hydraulic power or the horsepower of the pump is
# 
# $$W_2 = (\rho g H)Q~~~ (3)$$
# 
# The overall efficiency of the pump is
# 
# $$\eta = \frac{W_2}{W_1}~~~ (4)$$
# 
# The flowrate can be calculated directly from the pressure drop along the venturi:
# 
# $$Q = C_d~A_1 \sqrt{\frac{2 \Delta P}{\rho (\frac{A_1^2}{A_2^2} - 1)}}~~~ (5)$$
# 
# Dimensionlal analysis and [similarity laws](http://54.243.252.9/ce-3305-webroot/ce3305s22book/_build/html/lessons/lesson15/affinitylaws.html) are often used to represent the performance of a morphologically similar class of pump.
# 
# The useful dimensionless groups for homologous pumps (similar morphology) are:
# > $$C_Q = \frac{Q}{ND^3}$$
# > $$C_H = \frac{gH}{N^2D^2}$$
# > $$C_P = \frac{W_2}{\rho N^3 D^5}$$
# > $$Re_D = \frac{\rho N D^2}{\mu}$$
# > $$N \text{ is in radians per second.}$$
# 
# These dimensionless groups will allow you to plot your data onto a single chart for a given design, usually Reynolds number is on the horizontal axis and the dimensionless group on the vertical axis.
# 
# The relevant variables for the apparatus are:
# 
# ![](Variables.png)
# 
# <hr>
# 

# ## Link to Laboratory Document
# 
# 1. [Laboratory 7 Tasklist](http://54.243.252.9/ce-3105-webroot/2-Exercises/laboratory7/laboratory7.html)
# 2. [Laboratory 7 Instructional Video by Dr. Uddameri](https://www.youtube.com/watch?v=AOJljxHDtms)

# ## References
# 

# 1. [Centrifugal Pump Test Station (User Manual)](http://54.243.252.9/ce-3105-webroot/7-user-manuals/H83-Two-stageCentrifugalPumpTestSet.pdf)
# 2. [Pressure Readout (User Manual)](http://54.243.252.9/ce-3105-webroot/7-user-manuals/DP1-DigitalPressureDisplay.pdf)
# 3. [Data Acquisition System (User Manual)](http://54.243.252.9/ce-3105-webroot/7-user-manuals/VersatileDataAcquisitionSystem.pdf)
# 1. [Laboratory 7 Circa (2019)](http://54.243.252.9/ce-3105-webroot/pdf-source/Experiment7Pumptest.pdf)
# 2. [FHWA Lift Station Design](http://54.243.252.9/ce-3105-webroot/ce3105notes/lessons/laboratory7/FHWA-NHI-01-007-LiftStationDesign.pdf)
# 3. [Pump Selection](http://54.243.252.9/ce-3105-webroot/ce3105notes/lessons/laboratory7/PumpSelection.pdf)
# 4. [Pump Suction Conditions](http://54.243.252.9/ce-3105-webroot/ce3105notes/lessons/laboratory7/PumpSuctionConditions.pdf)
# 5. [Net Positive Suction Head](http://54.243.252.9/ce-3105-webroot/ce3105notes/lessons/laboratory7/NPSH-Explain.pdf)
# 6. [Pumps and Lift Stations (excerpt from Water Systems Design)](http://54.243.252.9/ce-3105-webroot/ce3105notes/lessons/laboratory7/Lecture06.pdf)
# 7. [Submersible Lift Stations Design (City of Houston Manual)](http://54.243.252.9/ce-3105-webroot/ce3105notes/lessons/laboratory7/2011_coh_design_manual_submersible_lift_stations.pdf)
# 8. [Holman, J.P., (2012) Experimental Methods for Engineers, 8th Ed. (Chapters 5,6, and 10)](https://mech.at.ua/HolmanICS.pdf)
# <!--9. [Laboratory 7 Example Report](http://54.243.252.9/ce-3105-webroot/2-Exercises/laboratory7/Goby7.pdf)-->

# In[ ]:




