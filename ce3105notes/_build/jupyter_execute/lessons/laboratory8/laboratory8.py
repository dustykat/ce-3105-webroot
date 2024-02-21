#!/usr/bin/env python
# coding: utf-8

# # 8. Open Channel Flow
# 
# This laboratory examines behavior in open channels, in particular determining Manning's n for a portion of a channel, and cerating and observing the alternate and sequent depths in a hydraulic jump.
# 
# ## Background/Theory
# 
# Open channel flow - free surface, gravity driven.  
# 
# > From pg. 1 of [Sturm, T. Open Channel Hydraulics, 1 st Ed.](https://www.amazon.com/Channel-Hydraulics-Third-Terry-Sturm/dp/1260469700)
# >
# >![](open-flow-narrative.png)
# 
# :::{note}
# The gravity "drive" is mostly true - I would say such flows are dominated by momentum conditions, mostly with gravity influence.  Open flow can go uphill (adverse to gravitational drive) but not for much distance (os one will run out of momentum)
# :::
# 
# Common examples of open channels:
# 
# - rivers, streams, brooks, creeks, cricks (Applacian meaning small stream), billabongs, bourns, wadis, and many more localized terms for small streams
# - ditches, canals, aqueducts, storm sewers, sanitary sewers
# 
# > From pg. 1 of [Sturm, T. Open Channel Hydraulics, 1 st Ed.](https://www.amazon.com/Channel-Hydraulics-Third-Terry-Sturm/dp/1260469700) 
# >
# > ![](examples-ocf.png)
# 
# Applications of open channel flow principles
# 
# - Culvert design, bridge design, spillway design
# - Floodway analysis, and nusiance flooding prediction
# - Fate and transport of yummy/yucky stuff (dissolved and/or suspended)
# - Surge estimation and coastal flooding from cyclonic storms [(hurricane,typhoon)](https://en.wikipedia.org/wiki/Tropical_cyclone)
# 
# > From pg. 1 of [Sturm, T. Open Channel Hydraulics, 1 st Ed.](https://www.amazon.com/Channel-Hydraulics-Third-Terry-Sturm/dp/1260469700) 
# >
# > ![](applications-ocf.png)
# 
# 
# Natural and man-made open channels are of interest to engineers. The Manning's equation is a fundamental equation governing open channel flow and is given by
# 
# $$ Q= \frac{K_n}{n}AR^{2/3}S^{1/2} $$
# 
# Where $K_n$ is the conversion factor (1 for SI and 1.49 for English units);
# $n$ is the Manning's roughness coefficient, $A$ is the cross-sectional area and $R$ is the hydraulic radius which is given as:
# 
# $$ R=\frac{A}{P_W}$$
# 
# where $P_W$ is the wetted perimeter.

# ## Steady-Uniform Flow
# 
# Uniform flow occurs when the average velocities in successive cross sections of a channel are the same. This occurs only when the cross section is constant. Non-uniform flow results from gradual or sudden changes in the cross sectional area.
# If the water surface is parallel to the channel bottom, flow is uniform and the water surface is at normal depth $y_n$
# 
# Used for design of long open channels with the goal to have the water surface slope equal to the bed slope.  Heres a couple of pictures,
# 
# First a Central Aridzona Project canal
# 
# ![](CAPcanal.png)
# 
# And the Central Valley Project (Callyfornia) canal I grew up swimmin' in.
# 
# ![](CVPcanal.png)
# 
# The line of floaty balls means you are approaching one of these:
# 
# ![](CVPliftStation.png)
# 
# Even though swimmin' in the canals is illegal, the operators dont want to turn a bunch of kids into fish food, so they put up the balls.  
# 
# :::{note}
# Despite the obvious Darwinian advantage of grinding up kids - dead meat does not pay taxes; support old folks; nor serve as a supply of harvestable kidneys.  Hence we try to save them.
# :::
# 
# In these applications the resistance to flow is balanced by a driving force provided by gravity.
# 
# Resistance is a consequence of cross-section shape, soil, vegetation, materials (in engineered channels).  In pipelines the resistance was understood by laboratory experimenters by the 1930's.  In open channels interest started later
# 
# :::{note}
# Obviously people have built working open channels much earlier, but techniques of design were empirical passed down by secret societies who wore wizard hats and flew on brooms!  
# :::
# 
# Consider a generic force balance diagram over a short section of channel, $\Delta L$ long:
# 
# ![](controlvolume1.png)
# 
# Now insert the Energy Grade Line (EGL) 
# 
# ![](cvcomplete.png)
# 
# In the case of uniform flow the flow depths are the same at each end of the section, the section length is such that the end areas are about the same, hence the upstream and downstream pressure force are the same, and the remaining forces are gravity (drive) and friction:
# 
# $$ W sin \theta = \rho g A \Delta L sin \theta = Fr $$
# 
# :::{note}
# In the above expression $Fr$ is the frictional shear force, not the Froude number.  Use the principle of algebraic substitution, and give friction any name you want in the drawing, except Elroy
# :::
# 
# If friction is stipulated to be generated only by the shear force induced at the solid-liquid interface (and not at the free surface) then the expression becomes
# 
# $$ \rho g A \Delta L sin \theta = \tau_0 P \Delta L $$
# 
# where $P$ is the wetted perimeter
# 
# Divide by $P \Delta L$ to obtain
# 
# $$ \frac{\rho g A \Delta L sin \theta}{P \Delta L} = \tau_0  $$ 
# 
# observe the hydraulic radius, $R_h = \frac{A}{P}$ appears
# 
# $$ \rho g R_h sin \theta = \tau_0  $$ 
# 
# The boundary shear stress is the factor that expresses the resistance properties of the fluid (wasser) and the solid material (conduit wall).  A usual simplification is to observe that the angle is usuall pretty small so that
# 
# $$ sin \theta~\approx~S_0 $$
# 
# In pipe flow (CE 3305) the shear stress was something like
# 
# $$ \tau_0 = \frac{f \rho V^2}{8}$$
# 
# Or more usefully (in that context)
# 
# $$ f= \frac{8\tau_0}{\rho V^2}$$
# 
# And one either looked up a value in the Moody chart or applied Swammee-Jain equations to find $f$ for various Reynolds numbers and material relative roughness.  
# 
# Returning to our situation we have
# 
# $$ \frac{\Delta h}{\Delta L}= \frac{\tau_O}{\rho g R}=\frac{\frac{f \rho V^2}{8}}{\rho g R}= \frac{f}{4R}\frac{V^2}{2g}$$
# 
# So now we need some way to express $f$.
# 

# ## Head Loss Models
# 
# **Chezy Correlation**
# 
# $$V = (\frac{8g}{f})^{1/2} \sqrt{R S_0} = C \sqrt{R S_0}$$
# 
# and the value $C$ is the Chezy coefficient.
# 
# **Manning Correlation**
# 
# Manning several years before his football career developed a similar correlation but observed that the hydraulic radius varied by the 2/3 power as
# 
# $$V  = C R^{2/3} S_0^{1/2}$$ 
# 
# There is meaningful theory to relate surface roughness to the "$C$" values
# 
# ![](velocitydistributions.png)
# 
# From here one can relate the friction factor back to Manning's n or the Chezy coefficient:
# 
# ![](mann_n-explain.png)
# 
# The usual way to specify Manning's n is by a table lookup such as [http://54.243.252.9/toolbox/Databases/ManningN/ManningsN.html](http://54.243.252.9/toolbox/Databases/ManningN/ManningsN.html)
# 
# or tables similar to those in our book
# 
# ![](mann1.png)
# ![](mann2.png)
# ![](mann3.png)
# ![](mann4.png)
# 
# or by comparison with photographs of channels
# 
# 1. Barnes, 1967 (A classic reference document) [https://pubs.usgs.gov/wsp/wsp_1849/pdf/wsp_1849.pdf](https://pubs.usgs.gov/wsp/wsp_1849/pdf/wsp_1849.pdf)
# 
# 2. [https://www.usgs.gov/centers/sawsc/science/mannings-roughness-coefficients-south-carolina-streams#overview](https://www.usgs.gov/centers/sawsc/science/mannings-roughness-coefficients-south-carolina-streams#overview)
# 
# 3. [https://pubs.usgs.gov/ds/668/pdf/DataSeries_668_2.pdf](https://pubs.usgs.gov/ds/668/pdf/DataSeries_668_2.pdf) 
# 
# and many others.
# 
# Normal Flow Calculations
# 
# $$Q=VA= \frac{K_n}{n} A R^{2/3} S_0^{1/2}$$
# 
# where $S_0$ is the bed slope, $S_f$ is the slope of the energy grade line (called the friction slope).
# 
# Typical cases:
# 1. Know $y_0$ or $y_n$, shape, $S_0$,$n$, compute $Q$ directly.
# 2. Know $y_0$, shape, $Q$,$n$, compute $S_0$ directly.
# 3. Know shape, $Q$,$n$,$S_0$ compute $y_0$ iteratively.

# ## Steady-Rapid Varied Flow
# 
# Momentum is a property of moving things and is the product of mass and velocity.  Angular momentum is the similar property in rotating geometries.  It takes an external force to change the momentum of an object.
# 
# :::{note}
# Except at faster than light travel (FTL) when impulse-momentum no longer applies; instead ones survival depends largely on the skill of the scriptwriter.  As engineers we wear the red shirts and are usually sacrificed, although Scottish engineers seem to last many episodes!
# :::
# 
# In the context of hydraulics many phenomenon which cannot be analyzed using the energy equation succumb nicely to momentum. The primary advantage of the momentum equation are that details of internal (to the control volume) flow patterns are irrelevant, only the external forces and momentum fluxes need to be considered.  The momentum balance was used earlier to solve the head loss caused by a bridge pier and this is a typical application of momentum balances.
# 
# It matters greatly in computational hydraulics in unsteady flow. 
# 
# ### Hydraulic Jump
# 
# A [hydraulic jump](https://www.youtube.com/watch?v=7tjf8HWiR3Y) occurs:
# 
# 1. when you startle a sugary liquid, it jumps and spills.  
# 2. when flow transitions for supercritical flow to subcritical flow over a short distance.
# 3. when a lowrider activates the car hydraulics and hops.
# 
# well for this lab its the second answer.
# 
# :::{note}
# The highest lowrider hop 414.65 cm (163.25 in) and was achieved by Robert White (USA) at the Los Magnificos car show in Austin, Texas, USA on 21 November 2015. The hop was made by a converted school bus called the Honeybadger.
# :::
# 
# 
# Here's a useful sketch.  Supercritical flow upstream meets subcritical downstream.  Downstream controls the flow, $Q$ is same but the downstream velocity os exchanged for flow depth, a bit of energy is lost in the transition.  The jump itself is quite turbulent and has a practical value in chemical mixing as well as energy dissipation.
# 
# ![](hydjump-sketch.png)
# 
# Engineering design is typically concerned with forcing jumps in armored channel sections otherwise the energy will chew away at the channel and destroy thangs.
# 
# A control volume around the jump might look like
# 
# ![](controlvolume2.png)
# 
# The jumps occur over a short distance, so the friction term is usually small compared to the other forces and change in momentum flux.
# 
# Conservation of momentum is
# 
# $$ \sum F_x = Fp_1 - Fp_2 - Fr = \rho Q(V_2 - V_1)$$
# 
# The pressure forces assume hydrostatic distributions so that 
# 
# $$ Fp = p_i A_i = \rho g \bar h_{i} A_i$$
# 
# where $\bar h_i$ is the depth to the centroid of the cross section ($\frac{y}{2}$
# 
# Making the substitutions and neglecting the friction term yields
# 
# $$  (\rho~g~\bar h_{1}~A_1) - (\rho~g~\bar h_{2}~A_2) = \rho Q(V_2 - V_1)$$
# 
# Rearrangement gives
# 
# $$  (\rho~g~\bar h_{1}~A_1) + \rho Q~V_1 = (\rho~g~\bar h_{2}~A_2) + \rho Q~V_2$$
# 
# Divide by $\rho~g$
# 
# 
# $$  (h_{1}~A_1) + \frac{Q^2}{gA_1} = (h_{2}~A_2) + \frac{Q^2}{gA_2}$$
# 
# The result above is called the momentum function, and interestingly looks similar to the specific energy function with the section geometry explicitly part of the balance.
# 
# $$ M_1 = M_2$$
# 
# The balance is at the two sections implies that the two different depths have the same momentum function, and these are called the alternate (upstream) and sequent (downstream) depths.
# 
# The function itself is dependent on section geometry a few analytical examples are:
# 
# ![](momentumfunctions.png)
# 
# 
# For other cross sections, numerical methods are employed.
# 

# ## Laboratory Apparatus
# 
# The apparatus is a recirculating water flume (photo below), width 1 ft, comprising a supply tank (in the flumw base) a head tank, two pumps, rectangular channel with side rails, depth gauges, total head tubes, bed tappings and downstream control gate.
# 
# ![](flumephoto.png)
# 
# Two parts of the experiment are : 
# 1. measure depth and flow over a rock bed (already in the flume) and determine Manning's n for the rock bed and compare to literature values, and 
# 2. create a hydraulic jump (by using the tail-race valve), stabilizing it, then measuring the alternate and sequent depths and comparing these to calculated values based on the discharge.
# 
# ### Discharge Measurements
# 
# The flowrate is determined using the calibration chart below. 
# 
# ![](calibration.png)
# 
# The y-axis is the difference of the manometers readings($\Delta H$) and the x-axis is the flowrate (Q). The following equation belongs to the "Large Orifice" line on the chart. 
# 
# $$ log_{10}(Q) = \frac{log_{10}(\Delta H)- 1.47}{2.096} $$
# 
# ### Flow Depth Measurements
# 
# Flow depth measurements are made using a digital distance gage (a ruler widda digital readout) if the battery is dead, you will still uset the device but make manual measurements using a ruler from different device settings.
# 
# ![](depthreadings.png)
# 
# The digital device reports distnace from the rail top to the pointer setting ($h_D$, in our case depth to water.  The total depth of the channel is $h_b$ = 44 mm.  The flow depth is the difference in these readings.
# 
# $$ h_{flow} = h_b - h_D$$
# 
# A second reading is made when the V-notch weir is in place.  It is used to check the pump flow calibration (it needs to be removed to create a stable hydraulic jump.  
# 
# $$ h_{flow@weir} = h_{M}+h_{notch}$$
# 
# ### Procedure
# 
# **Part 1**
# This part is to validate the flow calibration chart and equation.
# 0. Set the slope to 1-percent.
# 1. Ensure flume tailgate is down.
# 2. Close the red valves for both pumps.
# 3. Start the pumps.
# 4. Move the depth logger to the same elevation as the height of V notch and reset the value to zero.
# 5. Make sure the manometer valves corresponding to the selected orifice(s) is(are) open.
# 4. Ensure the manometers are free of air bubbles.
# 5. Open the red valve(s) to let flow into the flume.
# 6. Move the depth logger till it touches the top of the water level. Measure the height. Record this measurement.
# 7. Record the manometer readings for each pump.
# 8. Repeat the procedure for 4 different flowrates keeping the slope constant.  Use the red valves to adjust flowrates.
# 
# **Part2**
# This can be conducted with the weir in place
# 1. Move the depth logger to top of one of the rocks and reset the value to zero.
# 2. Make sure the manometer valves corresponding to the selected orifice is/are open
# 3. Ensure the manometers are free of air bubbles.
# 4. Open the Orifice to let flow into the flume
# 5. Move the depth logger till it touches the top of the water level. Measure the height
# 6. Repeat the procedure for 2 other flowrates keep the slope constant
# 7. Repeat the above steps for a total of 3 different **slopes**
# 
# **Part 3**
# This part will create a stable hydraulic jump.  It is easiest to remove the weir.
# 1. Shut down the pumps, close the red valves, and remove the weir - everything else can be left as-is.
# 2. Set the slope to 4-percent (its going to look steep, but the machine can handle it!)
# 3. Start the pumps (you can try with just a single pump if you wish).
# 4. Raise the tailgate a lot!
# 5. Zero the depth gage to the channel bottom.
# 6. Open the red valve(s) to start the flow.  
# 7. Raise the headgate to just above the water height.
# 8. Lower the tailgate a little bit at a time - you will likely observe two jumps, one near the head gate and one after the rocks.  The stable one is the one at the head gate.
# 9. Lower the headgate until it just touches the water surface - you are forcing supercritical depth at this location.  You should be able to create a stable jump about 0.5 to 1-foot from the head gate, and the water surface after the jump should be fairly established at the rocks.
# 10. Record the manometer readings for the pump(s)
# 11. Measure the flow depth befor the jump (halfway between the headgate and the jump should do). This is the alternate depth.
# 12. Measure the flow depth after the jump where the surface waves have dissipated (probably at the rocks).  This is the sequent depth.
# 

# ## Link to Laboratory Document
# 
# 1. [Laboratory 8 Tasklist](http://54.243.252.9/ce-3105-webroot/2-Exercises/laboratory8/laboratory8.html)
# 2. [Laboratory 8 Instructional Video by Dr. Uddameri](https://www.youtube.com/watch?v=_3ZBN_Ec9q4)

# ## References
# 
# 1. [V-Notch Weir Theory](https://siris.co.uk/v-notch-weir-design-how-does-it-work/)
# 2. [Hydraulic Jump Theory](https://en.wikipedia.org/wiki/Hydraulic_jump)
# 3. [Hydraulic Jump Calculator](https://www.omnicalculator.com/physics/hydraulic-jump)
# 4. [V-Notch Weir Calculator](http://ponce.sdsu.edu/onlineveenotchdescription.html)
# <!--5. [Example Report](http://54.243.252.9/ce-3105-webroot/2-Exercises/laboratory8/GoBy8.pdf)-->
# 5. [B-16 Hydraulic Demonstration Channel (User Manual)](http://54.243.252.9/ce-3105-webroot/7-user-manuals/ModelB-16-HydraulicDemonstrationChannel.pdf)
# 

# In[ ]:




