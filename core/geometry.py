# For functions relating to geometric calculations (metrics, radii, etc.)

from core.constants import G, M_sun, c

def generate_schwarzchildradius(mass):

    return (2 * G * mass) / (c**2)


test_mass = (1e11) * M_sun

print(generate_schwarzchildradius(test_mass))
