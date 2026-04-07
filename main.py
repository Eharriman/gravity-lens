from simulations.field_lensing import generate_lensed_field
from render.field_render import plot_lensed_comparison
import random


if __name__ == "__main__":
    theta_max = 2.0
    theta_max = 3.4
    n = 500
    theta_einstein = 0.5

    _, _, unlensed_image, lensed_image = generate_lensed_field(
        theta_max=theta_max,
        n=n,
        theta_einstein=theta_einstein,
        source_center=(0.4, 0.3),
        source_sigma=0.08
    )



    plot_lensed_comparison(unlensed_image, lensed_image, theta_max)
