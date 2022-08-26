#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_cell_magic('html', '', '<style> table {margin-left: 0 !important;} </style>')


# # CE 3105 - Mechanics of Fluids Laboratory
# 
# ## Laboratory 1 - Fluid Properties

# ## Objectives
# - Measure density, specific gravity of various fluids
# - Measure the viscosity of a fluid

# ## Background 
# 
# **Density** is a fundamental property of all materials including fluids. Density
# is typically denoted using symbol $\rho$ and is defined as the ratio of mass to
# volume of the material of interest. 
# 
# As an equation in words:
# $$\text{Density} = \frac{\text{Mass of the Fluid}}{\text{Volume occupied by the fluid}}$$
# 
# or more conventionally
# 
# $$\rho = \frac{M}{V}$$
# 
# At a given temperature and pressure the density of a given fluid is constant.
# Let us say we keep pouring some liquid into a beaker, as the mass increases
# so does the volume and density which is the ratio of mass to volume stays
# constant. 
# 
# In SI, the units of density are $\frac{kg}{m^3}$. 
# 
# In FPS system density is reported either as $\frac{\text{slugs}}{ft^3}$ or  $\frac{\text{lbm}}{ft^3}$ where [*lbm*](https://en.wikipedia.org/wiki/Pound_(mass)) is pound mass.

# **Specific Weight** is the **weight** per unit volume of the material. 
# Remember that weight is a force obtained by multiplying mass and gravitational acceleration (g). 
# 
# As an equation in words:
# 
# $$\text{Specific Weight} = \frac{\text{weight}}{\text{volume}}$$
# 
# or more conventionally
# 
# $$\gamma = \frac{W}{V} = \frac{m \cdot g}{V}$$
# 
# At a given temperature, pressure and location, the specific weight of a fluid
# is constant. However, the acceleration due to gravity varies slightly with
# location. The specific weight of a fluid is slightly lower at the poles than at the equator even when the temperature and pressure of the fluid are the same at both
# locations.

# **Specific Gravity** is another important fluid property which is defined as the
# ratio of the density of a fluid to the density of water at the same temperature.
# Clearly, the specific gravity is equal to 1.0 for water. Fluids denser than
# water have a specific gravity greater than 1 while those lighter than water
# have specific gravity less than 1.
# 
# $$SG = \frac{\rho_s}{\rho_{H2O}} $$
# 
# Being a ratio of two densities, specific gravity is a dimensionless quantity.
# Specific gravity can tell us whether an object will float or sink in water. Specific
# Gravity also provides consistency to compare fluids across different units.

# **Viscosity** quantifies the ability of the fluid to resist shear stress (i.e.,
# internal resistance). One can also conceptualize viscosity as the frictional
# forces that exist between two layers of fluid that are in relative motion.
# 
# **Dynamic Viscosity** measures the tangential force per unit area required to move one horizonal plane relative to another at a unit velocity when maintaining unit distance separation. The shear stress applied causes the fluid to flow (or flow causes stress). 
# 
# Newton's law of viscosity states that the shear stress, $\tau$, is proportional to the velocity gradient (across the flow flow), $\frac{du}{dy}$ (see Figure 1). 
# Dynamic viscosity ,$\mu$, is the constant of proportionality.
# 
# <figure align="center">
# <!--<img src="./Hydropower.png" width="300" >-->
# <img src="http://54.243.252.9/ce-3105-webroot/2-Exercises/laboratory1/shearstress.png" width="300" >
# <figcaption>Figure 1: Shear stress conceptual diagram </figcaption>
# </figure>
# 
# Newton's law expressed as an equation is:
# $$\tau = \mu \cdot \frac{du}{dy} $$
# 
# thus dynamic viscosity is the ratio of shear force to the velocity gradient. It has units of $ Pa \cdot s = \frac{kg \cdot m}{s^2} \cdot \frac{s}{m^2}$. 
# 
# In cgs system the units of dynamic viscosity is Poise (or more commonly centipoise, cP). 
# 
# In US Customary units we express viscosity as $\frac{lbf}{ft \cdot s}$. 
# 
# In practical fluid mechanics, we often encounter the ratio of dynamic viscosity to density. This term is the **kinematic viscosity**. 
# 
# Expressed as an equation in commonly used notation:
# 
# $$ \nu = \frac{\mu}{\rho}$$
# 
# The kinematic viscosity has SI units of $$\frac{m^2}{s}$$.
# 
# A useful method to determine viscosity of liquids is to record the rate at which a
# sphere will fall through a liquid of interest. 
# Under equilibrium conditions, the frictional forces experienced by the sphere will be equal to its weight. The sphere will fall at a constant speed known as the terminal velocity. 
# The phenomenon is called Stokes law (or Stokes flow). 
# 
# A simple force balance is depicted in Figure 2, where the bouyant force and drag force are equal to the weight of the sphere.
# 
# <figure align="center">
# <!--<img src="./Hydropower.png" width="300" >-->
# <img src="http://54.243.252.9/ce-3105-webroot/2-Exercises/laboratory1/sphereforces.png" width="300" >
# <figcaption>Figure 2: Force balance on a sphere falling at constant velocity </figcaption>
# </figure>
# 
# Stokes flow occurs at pretty low Reynolds numbers so the laminar correlation for the drag coefficient is appropriate
# 
# $$ c_d = \frac{24}{Re}+\frac{4}{\sqrt{Re}}+0.4 $$
# 
# If the Reynolds number is less than $\frac{1}{2}$ the drag coefficient is $c_d = \frac{24}{Re}$, using this representation of drag the force balance for the sphere allows us to solve for velocity, $u$,
# 
# $$ u = \frac{g \cdot d^2}{18 \nu}(\frac{\sigma}{\rho} -1)$$
# 
# where, *g* is the acceleration due to gravity, *d* is the diameter of the sphere,
# $\nu$ is the kinematic viscosity, $\rho$ is the density of the sphere, $\rho$ is the density of the fluid.
# 
# We can apply the formula to get an idea of how fast to expect a sphere to fall if Stokes flow holds.  In the experiment we willuse Glycerine as the liquid phase, and small steel spheres the largest is about 2.5 millimeters.

# In[2]:


# 
gravity = 9.81 #m/s^2
viscosity = 1.41 # Ns/m^2
density_liquid = 1260 #kg/m^3
density_sphere = 7700 #kg/m^3
diameter = 0.025 #meters - nominal 2.5mm
upper_support_terminal_speed = (gravity*diameter**2)*(density_sphere/density_liquid - 1.0)/(18.0*viscosity)
print("Stokes flow speed limit = ",round(1000.0*upper_support_terminal_speed,6)," millimeters per second")


# So using the above script we conclude that we should be able to make measurements for spheres as large as 25 mm, using a stopwatch and visual observation.

# ## Data Aquisition
# 
# ### PART I - Density Measurements
# 1. Measure the temperature of the fluid
# 2. Weigh the beaker provided
# 3. Fill the beaker with fluid, and measure its mass (beaker + fluid)
# 4. Carefully measure or estimate the volume of the fluid in the beaker
# 5. Repeat your measurements (3 duplicates for each fluid assigned to you)

# ### PART II - Specific Gravity
# 1. Carefully place the calibrated hydrometer into the uid and record the value corresponding to the lower [meniscus](https://en.wikipedia.org/wiki/Meniscus_(liquid)),
# 2. Make 3 duplicate measurements for each fluid assigned to you

# ### PART III - Viscosity
# 1. Take a steel ball (sphere) assigned to your group and note its diameter
# 2. Carefully drop the ball into the ball guide
# 3. Note the volume readings corresponding to the upper and lower level markers (i.e., the two rubber bands)
# 4. Start the stopwatch when the ball reaches the first level marker (upperrubber band).
# 5. Stop the stopwatch when the ball reaches the second level marker (lower rubber band).
# 6. The density of the stainless steel sphere is 7800 $\frac{kg}{m^3}$
# 7. Repeat the above steps for each sphere assigned to you

# ## Data Analysis
# 
# ### PART I - Density
# 1. Calculate the density of the uid by dividing the mass over volume for each fluid and sample
# 2. Calculate the mean and standard deviation for the estimated density of each fluid
# 3. Calculate the mass of salt present in the brackish water sample. Calculate mean and standard deviation over all samples.
# 
# ### PART II - Specific Gravity
# 1. Tabulate the specific gravity measurements for each fluid.
# 2. For each fluid calculate [mean and standard deviations](http://54.243.252.9/engr-1330-webroot/engr1330notes/_build/html/examples/8statistical/1descriptivestatistics.html)
# 3. [Plot](http://54.243.252.9/engr-1330-webroot/engr1330notes/_build/html/examples/7graphing/example05.html) density (calculated from PART I) (on X-axis) and specific gravity (on Y-axis). [Fit](http://54.243.252.9/engr-1330-webroot/engr1330notes/_build/html/examples/10datamodels/datamodels.html) a straight line and record the slope, intercept and coefficient of determination $R^2$
# 
# ### PART III - Viscosity
# 1. Calculate kinematic viscosity for each sample using Equation 8.
# 2. Use the density calculated in PART I to calculate dynamic viscosity for each sample.
# 3. Compute and tabulate the [mean and standard deviation](http://54.243.252.9/engr-1330-webroot/engr1330notes/_build/html/examples/8statistical/1descriptivestatistics.html) for both kinematic and dynamic viscosity measurements.

# ## Discussion/Interpretation Questions (for the Lab Report)
# 1. Why is it important to measure temperature when measuring density and viscosity?
# 2. How do you think the density and viscosity of water would change with temperature.
# 3. How do salts alter the density of groundwater? Why is measurement of brackish water density important for civil and environmental engineers.
# 4. What is standard deviation? 
#   - What does it tell us about the accuracy of the measurements?
#   - What does it tell us about the repeatability of the measurements?
# 5. What are some potential sources of errors in your lab experiments. Discuss in the context of measuring density, specific gravity and viscosity.

# ## Data Records
# 
# ### Part I - Gravimetric Determination of Density
# 
# Complete the table using Jupyter Notebook or Excel and cut-and-paste into the Laboratory Report
# 
# |Substance|Measurement ID|Temp ($^o$C)| Mass (Dry Beaker)| Mass (Beaker + Fluid) |Volume (ml) |Density, $\rho$| SG (computed)|
# |---|---:|---:| ---:| ---:|---:|---:|---:|
# |Water| 1|||||||
# |Water| 2|||||||
# |Water| 3|||||||
# |Salt Water| 1|||||||
# |Salt Water| 2|||||||
# |Salt Water| 3|||||||
# |Glycerine| 1|||||||
# |Glycerine| 2|||||||
# |Glycerine| 3|||||||

# ### Part II - Specific Gravity (by Hydrometer)
# 
# Complete the table using Jupyter Notebook or Excel and cut-and-paste into the Laboratory Report
# 
# |Substance|Measurement ID| SG (computed from above)|SG Hydrometer Reading|
# |---|---:|---:| ---:| 
# |Water| 1|||
# |Water| 2|||
# |Water| 3|||
# |Salt Water| 1|||
# |Salt Water| 2|||
# |Salt Water| 3|||
# |Glycerine| 1|||
# |Glycerine| 2|||
# |Glycerine| 3|||

# ### Part III - Viscosity Determination by Stokes Law
# 
# Complete the table using Jupyter Notebook or Excel and cut-and-paste into the Laboratory Report
# 
# |Team ID |$d_{ball}$|$\sigma$|$\Delta V$|$d_{cyl.}$|L|$t_1$(sec)|$t_2$(sec)|$\nu_{liq.}$|$\rho_{liq.}$|$\mu$|
# |------|---:|---:| ---:| ---:|---:|-----:|-----:|---:|---:|---:|
# |Team 1|$\frac{5}{32}$||||||||||
# |Team 1|$\frac{1}{16}$||||||||||
# |Team 2|$\frac{3}{32}$||||||||||
# |Team 2|$\frac{1}{8}$||||||||||
# |Team 3|$\frac{5}{32}$||||||||||
# |Team 3|$\frac{1}{16}$||||||||||
# |Team 4|$\frac{3}{32}$||||||||||
# |Team 4|$\frac{1}{8}$||||||||||
# |Team 5|$\frac{5}{32}$||||||||||
# |Team 5|$\frac{1}{16}$||||||||||

# ## References
# 
# 1. [Laboratory 1 circa 2021](http://54.243.252.9/ce-3105-webroot/pdf-source/Experiment-1-Fluid-Properties.pdf)
# 2. [Engineering Fluid Mechanics (Cd for spheres) go to p.414](ce-3105-webroot/2-Exercises/laboratory1/EFM-22.pdf)
# 3. [Descriptive Statistics](http://54.243.252.9/engr-1330-webroot/engr1330notes/_build/html/examples/8statistical/1descriptivestatistics.html)
# 4. [Plotting Data](http://54.243.252.9/engr-1330-webroot/engr1330notes/_build/html/examples/7graphing/example05.html)
# 5. [Fitting Data Models](http://54.243.252.9/engr-1330-webroot/engr1330notes/_build/html/examples/10datamodels/datamodels.html)
# 6. [This page as Jupyter ipynb file](http://54.243.252.9/ce-3105-webroot/2-Exercises/laboratory1/laboratory1.ipynb)
