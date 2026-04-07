import numpy as np
from models.source_field import gaussian_source
from core.lens_mapping import generate_theta_grid, map_theta_to_beta

def generate_lensed_field(theta_max, n, theta_einstein, 
                           source_center=(0.0,0.0), source_sigma=0.08):
    
    theta_grid = generate_theta_grid(theta_max, n)
    beta_grid = map_theta_to_beta(theta_grid, theta_einstein)

    unlensed_image = gaussian_source(
        beta_grid,
        center=source_center,
        sigma=source_sigma
    )

    lensed_image = gaussian_source(
        theta_grid,
        center=source_center,
        sigma=source_sigma
    )

    return theta_grid, beta_grid, unlensed_image, lensed_image


