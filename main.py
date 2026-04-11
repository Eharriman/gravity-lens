from simulations.field_lensing import generate_lensed_field
from render.field_render import plot_lensed_comparison, plot_magnification_and_det
import random


if __name__ == "__main__":

    source_list = [
        {
            "type": "gaussian_circular",
            "center": (0.6, 0.4),
            "sigma": 0.1,
            "amplitude": 50
        },
        {
            "type": "gaussian_elliptical",
            "center": (0.7, -0.6),
            "sigma_major": 0.15,
            "sigma_minor": 0.07,
            "angle": 0.5,
            "amplitude": 100,
        },
        {
            "type": "sersic_source",
            "center": (-0.4, -0.3),
            "amplitude": 3.2,
            "R_eff": 1.4,
            "n_sersic": 1.9
        }
    ]
    
    # Use this example for explicit Einstein ring demonstration
    '''
    source_list = [
        {
            "type": "gaussian_circular",
            "center": (0.6, 0.0),
            "sigma": 0.08,
            "amplitude": 1
        }
    ]
    '''
    
    theta_max = 2.0
    n = 500
    theta_einstein = 0.4

    result = generate_lensed_field(
        theta_max=theta_max,
        n=n,
        theta_einstein=theta_einstein,
        source_list=source_list
    )

    plot_lensed_comparison(
        result["unlensed_image"],
        result["lensed_image"],
        theta_max
    )
    '''
    plot_magnification_and_det(
        result["magnification"],
        result["det_jacobian"],
        theta_max
    )
    '''



    #plot_lensed_comparison(unlensed_image, lensed_image, theta_max)
