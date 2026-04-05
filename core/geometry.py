# For functions relating to geometric calculations (metrics, radii, etc.)

from core.constants import G, M_sun, c, kpsc
import numpy as np

def generate_schwarzchildradius(mass):

    return (2 * G * mass) / (c**2)


def generate_einstein_angle(mass, D_ls, D_s, D_l):
    # Returns the Einstein angle for a given lens mass and astrophysical distances
    # Here:
    #   D_ls: the distance from the lens to the image source
    #   D_l : the distance from the observer to the lens
    #   D_s: the distance from the observer to the source
    #   mass: the mass of the lensing object itself

    schwarz_rad = generate_schwarzchildradius(mass)
    distance_ratio = (D_ls) / (D_l * D_s)

    return np.sqrt(2 * schwarz_rad * distance_ratio)





test_mass = M_sun
D_ls = D_s = D_l = 1e22

print(generate_schwarzchildradius(test_mass))
print(generate_einstein_angle(test_mass, D_ls, D_l, D_s))

