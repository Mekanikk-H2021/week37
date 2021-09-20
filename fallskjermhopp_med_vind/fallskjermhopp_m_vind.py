from vpython import *

def sidewind(z, ur=vec(7, 0, 0), zr=5, alpha=1/7):
    """
    Function which calculates the effect of a sidewind at zr meters vertically on a object at z meters.

    Args:
        z: Height in meters
        ur: windspeed as vector in meters per second
        zr: Height of wind
        alpha: Wind coefficient
    """
    return ur * (z / zr) ** alpha

# initial conditions
m = 75   # kg
g = 9.81 # ms^-2
pos = vec(0, 0, 3000)
vel = vec(0, 0, 0)

# Air resistance parameters. Found at http://labman.phys.utk.edu/phys221core/modules/m3/drag.html
D = 0.7    # Drag coefficient of baseball
A = 0.2    # Frontal area (m^2)
rho = 1.29 # Air density (kg / m^3)

# time conditions
t = 0
dt = 0.1
tmax = 500

# Plots
posz_graf = graph(title="Høydeplott", xtitle="t (s)", ytitle="høyde z (m)", fast=False)
posz_curve = gcurve(graph=posz_graf)
posx_graf = graph(title="Bevegelse i x-retning", xtitle="t (s)", ytitle="x (m)", fast=False)
posx_curve = gcurve(graph=posx_graf)

# animation
box_pos = vec(0, 0, -20)        # Setting the ground position at the origin, but translated 20 units "into" the background
box_size = vec(2000, 2000, 10)  # Setting size of ground to 2000 units in the xy-plane, and a thickness of 10 units.

ground = box(pos=box_pos, size=box_size, color=color.green)
skydiver = sphere(vel=vec(0, 0, 0), radius=10)

# Center point to compare landing position to
center = sphere(pos=vec(0, 0, 0), radius=10, color=color.blue)

while t <= tmax and pos.z >= 0:

    # Fix rate and update time
    rate(1/dt * 10)
    t += dt

    # Force of gravity
    Fg = - m * g * vec(0, 0, 1)
    
    # Force from wind
    u = sidewind(pos.z)

    # We use the relative velocity in the wind force equation
    rel_vel = u - vel

    # Force which wind exerts on the skydiver. For a more realistic simulation, tweak the parameters of D and A and think about how the wind hits the skydiver from the side.
    Fw = 0.5 * D * rho * A * rel_vel.mag2 * rel_vel.hat

    # Air resistance
    Fr = 0.5 * D * rho * A * vec(0, 0, vel.z ** 2)

    # Summation of forces
    Fnet = Fg + Fr + Fw

    # Update velocity
    vel = vel + (Fnet / m) * dt

    # Update position
    pos = pos + vel * dt

    # Update animated figure position and velocity
    skydiver.pos = pos
    skydiver.vel = vel

    # Plot height and x displacement
    posz_curve.plot(t, pos.z)
    posx_curve.plot(t, pos.x)
    
