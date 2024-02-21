#!/usr/bin/env python
# coding: utf-8

# # 5. Fitting (Minor) Losses in Pipe Systems
# 
# 

# Pipe networks have numerous fittings: mitre bends, elbow bends,
# large radius bends, sudden expansions and sudden contractions. There are losses due to these fittings which are known as fitting or minor losses which cause noticable pressure drops. Pressure loss across a fitting is the difference between the
# pressure at the upstream and downstream of that fitting.
# 
# ## Expansions and Contractions
# 
# In a sudden expansion, the flow splits when it is entering the bigger diameter pipe from the smaller diameter pipe. Head is lost due to the diffusion
# and eddies in the corners. In sudden contraction, flow area is contracted
# which is known as vena contracta because of the jet formation. Head loss is
# due to vortices and eddies. Figure 1 illustrates loss at a pipe fitting:
# 
# ![](fittingloss.png)
# 
# For the fitting above, the total head loss:
# 
# $$ \Delta H = \Delta h + \frac{V_u^2}{2g} - \frac{V_d^2}{2g} $$
# 
# The loss coefficient K is defined as
# 
# $$ K = \frac{\Delta H~2g}{V_d^2} $$ 
# 
# or
# 
# $$ K = \frac{\Delta H~2g}{V_u^2} $$ 
# 
# Usually the velocity associated with the smaller diameter part of the fitting is used.
# 
# In this experiment, the mitre and elbow have constant pipe diameters. Therefore, $V_u$ and $V_d$ are the same. 
# 
# For the sudden enlargement, the upstream velocity is used to express the velocity head. 
# For the sudden contraction, the downstream velocity characterizes the velocity head.
# 
# ## Bends
# 
# When liquid is flowing through a $90^o$ bend, depending on the ratio of radius of
# curvature to diameter of the pipe ($\frac{R}{D}$), amount of loss differs. Smaller loss is associated with easier flow path and lower the minor loss coefficient, K
# value is. Following table summarizes the typical K values for different bends
# 
# ![](SomeKvalues.png)
# 

# ## Loss Model Structure
# 
# The loss model(s) are usually of the structure 
# 
# $$ \Delta H = K~\frac{V^2}{2g} $$ 
# 
# where the velocity is taken as the larger value  in the case of a diameter change.
# 
# The $K$ values are determined from
# 
# ### Bend
# 
# $$ K = \frac{\Delta H}{\frac{V^2}{2g}} $$ 
# 
# ### Expansion
# 
# $$ K = \frac{\Delta H}{\frac{V_u^2}{2g}} $$ 
# 
# The $K$ value can be approximated from
# 
# $$K=[1- \frac{A_u}{A_d}]^2$$
# 
# ### Contraction
# 
# $$ K = \frac{\Delta H}{\frac{V_d^2}{2g}} $$ 
# 
# The $K$ value can be approximated from
# 
# $$K=[ \frac{A_d}{A_u}-1]^2$$
# 

# ## Apparatus Layout and Operation
# 
# ![](apparatus.png)
# 
# The figure depicts the experimental apparatus used.  The operational procedure is:
# 
# 1. Close the exit valve on the left side of the flow circuit, and then turn on the water source
# 2. Slowly open the exit valve on the apparatus, and watch the water levels in the manometer tubes
# 3. Determine the flow rate of the liquid by measuring the time it takes to fill a known volume.
# 4. Record the differential pressure readings across each of the fittings
# 5. Repeat step 3 and 4 to obtain data for at least five different flow rates by adjusting the exit valve

# ## Link to Laboratory Document
# 
# 1. [Laboratory 5 Tasklist](http://54.243.252.9/ce-3105-webroot/2-Exercises/laboratory5/laboratory5.html)
# 2. [Laboratory 5 Instructional Video by Dr. Uddameri](https://www.youtube.com/watch?v=TXKumBf9Pdc)

# ## References
# 

# 1. [Fitting Loses in Pipes](https://www.ese.iitb.ac.in/sites/default/files/Losses%20Due%20To%20Pipe%20Fittings.pdf)
# 2. [Fitting Loss Coefficients (Tabular)](https://neutrium.net/fluid-flow/pressure-loss-from-fittings-excess-head-k-method/)
# 3. [H-34 Pipe Network Energy Losses (User Manual)](http://54.243.252.9/ce-3105-webroot/7-user-manuals/H34-PipeworkEnergyLosses.pdf)

# In[ ]:




