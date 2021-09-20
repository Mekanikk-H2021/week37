import numpy as np
from vpython import *

# Initial conditions
m1, m2 = 1, 3
u1, u2 = 2, -1

def elastic_collision(m1, m2, u1, u2):
    """
    Function which given mass and velocity of two objects calculates the velocity after an elastic collision in one dimension between them.

    Parameters:
        m1: float, int
            mass of object 1
        m2: float, int
            mass of object 2 
        u1: float, int
            velocity of object 1
        u2: float, int
            velocity of object 2
    Returns:
        v1: float, int
            velocity of object 1
        v2: float, int
            veolcity of object 2
    """
    # Conservation of momentum and energy => theese are equally large scalar quantities before and after collision
    P = u1 * m1 + u2 * m2
    K = 0.5 * m1 * u1 ** 2 + 0.5 * m2 * u2 ** 2

    # Calculation of velocities after collisions.
    v2 = (np.sqrt(m1 * m2 * (2 * K * m1 + 2 * K * m2 - P ** 2)) + m2 * P) / (m2 ** 2 + m1 * m2)
    v1 = (P - m2 * v2) / m1
    return v1, v2


v1, v2 = elastic_collision(m1, m2, u1, u2)

print("v1 = {}, v2 = {}".format(v1, v2))

# Initial conditions
m_tennis = 0.05 # kg
m_gokart = 50   # kg

v_tennis = 20   # m/s
v_gokart = -20 / 3.6 # m/s

balls = 0
while abs(v_gokart) > 0.05:
    balls += 1
    _, v_gokart = elastic_collision(m_tennis, m_gokart, v_tennis, v_gokart)
    print("Speed of gokart = {0:.3f}, thrown balls = {1:}".format(v_gokart, balls))

# Initial conditions
m_tennis = 0.05  # kg
m_gokart = 50   # kg

v_tennis = 20   # m/s
v_gokart = -20 / 3.6  # m/s


balls = 0
while abs(v_gokart) > 0.05:
    balls += 1

    # For each tennis ball we throw, the ball lands in the gokart
    m_gokart += m_tennis
    _, v_gokart = elastic_collision(m_tennis, m_gokart, v_tennis, v_gokart)
    print("Speed of gokart = {0:.3f}, thrown balls = {1:}".format(v_gokart, balls))
