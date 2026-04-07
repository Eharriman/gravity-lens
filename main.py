from simulations.field_lensing import generate_lensed_field
from render.field_render import plot_lensed_comparison
import random


if __name__ == "__main__":
    
    source_list = [
        {
            "type": "gaussian_source",
            "center": (0.6, 0.0),
            "sigma": 0.08,
            "amplitude": 1.0
        },
        {
            "type": "sersic_source",
            "center": (-1.2, -0.9),
            "amplitude": 1.0,
            "R_eff": 0.3,
            "n_sersic": 1.2
        }
    ]
    
    
    theta_max = 2.0
    n = 500
    theta_einstein = 0.5

    _, _, unlensed_image, lensed_image = generate_lensed_field(
        theta_max=theta_max,
        n=n,
        theta_einstein=theta_einstein,
        source_list=source_list
    )



    plot_lensed_comparison(unlensed_image, lensed_image, theta_max)
