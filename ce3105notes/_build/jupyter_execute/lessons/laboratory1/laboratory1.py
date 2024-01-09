#!/usr/bin/env python
# coding: utf-8

# # 1. Fluid Properties
# 
# 

# ## Density
# 
# **Density** is a fundamental property of all materials including fluids. Density
# is typically denoted using symbol $\rho$ and is defined as the ratio of mass to
# volume of the material of interest. 
# 
# As an equation in words:
# 
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

# ## Specific Weight
# 
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

# ## Specific Gravity
# 
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

# ## Viscosity
# 
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
# $$ u = \frac{g \cdot d^2}{18 \nu}(\sigma-\rho)$$
# 
# where, *g* is the acceleration due to gravity, *d* is the diameter of the sphere,
# $\nu$ is the kinematic viscosity, $\sigma$ is the density of the sphere, $\rho$ is the density of the fluid.
# 
# We can apply the formula to get an idea of how fast to expect a sphere to fall if Stokes flow holds.  In the experiment we will use Glycerine as the liquid phase, and small steel spheres the largest is about 2.5 millimeters

# In[1]:


# Estimate Sphere Falling Speed assuming laminar flow
gravity = 9.81 #m/s^2
viscosity = 15.103 # Ns/m^2
density_liquid = (69.5/50)*1000*1000 #kg/m^3
density_sphere = (11.350)*1000*1000 #kg/m^3
diameter = 0.0125 #meters - nominal 2.5mm
upper_support_terminal_speed = (gravity*diameter**2)*(density_sphere-density_liquid)/(18.0*viscosity)
print("Stokes flow speed limit = ",round(upper_support_terminal_speed,6)," millimeters per second")


# So using the above script we conclude that we should be able to make measurements for spheres as large as 25 mm, using a stopwatch and visual observation, our spheres are quite a bit smaller, so we should have no issues.

# ## References
# 
# 1. [Engineering Fluid Mechanics](http://54.243.252.9/ce-3105-webroot/2-Exercises/laboratory1/EFM-2.pdf)
# 2. [Engineering Fluid Mechanics (Cd for spheres) go to p.414](http://54.243.252.9/ce-3105-webroot/2-Exercises/laboratory1/EFM-22.pdf)
# 3. [Holman, J.P., (2012) Experimental Methods for Engineers, 8th Ed. (Chapters 1-3)](https://mech.at.ua/HolmanICS.pdf)
# 
# 

# ## Link to Laboratory Document
# 
# 1. [Laboratory 1 Tasklist](http://54.243.252.9/ce-3105-webroot/2-Exercises/laboratory1/laboratory1.html)
# 2. [Laboratory 1 Instructional Video by Dr. Uddameri](https://www.youtube.com/watch?v=WwV-azCJWis)

# In[ ]:




