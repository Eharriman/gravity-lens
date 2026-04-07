import numpy as np
from models.source_field import gaussian_source, sersic_source
from core.lens_mapping import generate_theta_grid, map_theta_to_beta
from models.source_field import source_field

def generate_lensed_field(theta_max, n, theta_einstein, 
                           source_list):
    
    theta_grid = generate_theta_grid(theta_max, n)
    beta_grid = map_theta_to_beta(theta_grid, theta_einstein)

    # Beta is unlensed?
    '''
    unlensed_image = gaussian_source(
        theta_grid,
        center=source_center,
        sigma=source_sigma
    )

    lensed_image = gaussian_source(
        beta_grid,
        center=source_center,
        sigma=source_sigma
    ) 
    unlensed_image = sersic_source(
        theta_grid,
        center=source_center
    )

    lensed_image = sersic_source(
        beta_grid,
        center=source_center
    )
    '''
    
    unlensed_image = source_field(theta_grid, source_list)
    
    lensed_image = source_field(beta_grid, source_list)

    return theta_grid, beta_grid, unlensed_image, lensed_image


