#!/usr/bin/env python
# coding: utf-8

# # 4. Pipe Friction
# 
# This experiment examines the friction in a narrow diameter tube (pipe).
# 
# ## Objectives
# - Observe the behavior of flow with change in velocity and Reynolds number
# - Observe the variation of frictional loss with change in velocity

# ## Modified Bernoulli Equation
# 
# The equation below is the one-dimensional steady flow form of the energy equation typically applied for pressurized conduit hydraulics.
#  
# $$
# \begin{equation}
# \frac{p_1}{\rho g}+\alpha_1 \frac{V_1^2}{2g} + z_1 + h_p =
# \frac{p_2}{\rho g}+\alpha_2 \frac{V_2^2}{2g} + z_2 + h_t + h_l
# \label{eqn:closed-conduit-energy-equation}
# \end{equation}
# $$
# 
# where $\frac{p}{\rho g}$ is the pressure head at a location, $\alpha \frac{V^2}{2g}$ is the velocity head at a location, $z$ is the elevation, $h_p$ is the added head from a pump, $h_t$ is the added head extracted by a turbine, and $h_l$ is the head loss between sections 1 and 2.   {numref}`closed-conduit-energy` is a sketch that illustrates the various components in the energy equation.
# 
# ```{figure} closed-conduit-energy.png
# ---
# width: 400px
# name: closed-conduit-energy
# ---
# Definition sketch for energy equation
# ```
# 
# In pipeline analysis this energy equation is applied to a link that joins two nodes.
# Pumps and turbines would be treated as separate components (links) and their hydraulic behavior must be supplied using their respective pump/turbine curves.

# ## Flow Regimes
# Laminar flow occurs at low velocities when the particles of waters move in
# parallel straight lines. The flow is smooth and well-ordered. As the velocity
# increases, the movement becomes undulating and at some point it breaks into
# vortices. The flow is turbulent in this case. Reynolds number classifies
# whether the flow is laminar or turbulent. For a circular pipe, it can be ex-
# pressed as
# 
# $$Re = \frac{\rho vD}{\mu} = \frac{vD}{\nu}$$
# 
# It is nearly impossible for turbulent flow to occur at Reynolds number less
# than 2000 as the turbulence will be restrained by the viscous resistance.
# However, there is a stage when laminar flow is becoming turbulent or turbulent is becoming laminar. This is transitional flow. 
# 
# For smooth pipes, the common classifications are:
# 
# - Laminar Flow: $Re < 2000$
# - Transitional Flow: $2000 \le Re \le 4000$
# - Turbulent Flow: $Re > 4000$
# 
# For laminar flow, the head loss due to friction is directly proportional to the velocity:
# $\frac{\Delta h}{L} \propto v$
# 
# For turbulent flow, the head loss due to friction is proportional to the velocity
# to a given power, $n$:
# $\frac{\Delta h}{L} \propto v^n$
# 
# The exponent, $n$ varies between 1.75 and 2. 
# 
# The flow velocity, $u$ can be found from the continuity equation when the
# cross-sectional area of the pipe is known:
# 
# $$u = \frac{Q}{A}$$

# ## Friction Factors
# 
# The friction factor, $f$ can be found using Darcy-Weisbach equation:
# 
# $$f = \frac{2 \Delta h~g D}{L v^2} $$
# 
# The necessary physical water properties corresponding to water temperature
# should be used. They can be found in tables such as [http://54.243.252.9/toolbox/fluidmechanics/WaterPropertiesUS/WaterPropertiesUS.html](http://54.243.252.9/toolbox/fluidmechanics/WaterPropertiesUS/WaterPropertiesUS.html), or from any fluid mechanics textbook.
# 
# {numref}`labsetup` is a photograph of the experimental setup
# 
# ```{figure} labsetup.png
# ---
# width: 400px
# name: labsetup
# ---
# Photograph of Laboratory Set-Up (for Low-Flow Measurements)
# ```

# ## Link to Laboratory Document
# 
# 1. [Laboratory 4 Tasklist](http://54.243.252.9/ce-3105-webroot/2-Exercises/laboratory4/laboratory4.html)
# 2. [Laboratory 4 Instructional Video by Dr. Uddameri](https://www.youtube.com/watch?v=Xu132UBglpw)

# ## References
# 
# 1. [Laboratory 4 (circa 2020)](http://54.243.252.9/ce-3105-webroot/pdf-source/Experiment4FrictionLossinaPipe.pdf)
# 2. [H-7 Friction Loss in a Pipe (User Manual)](http://54.243.252.9/ce-3105-webroot/7-user-manuals/H7-FrictionLossInAPipe.pdf)

# In[ ]:




