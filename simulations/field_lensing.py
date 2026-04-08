import numpy as np
from core.lens_mapping import generate_theta_grid, map_theta_to_beta
from models.source_field import source_field

def generate_lensed_field(theta_max, n, theta_einstein, 
                           source_list):
    
    theta_grid = generate_theta_grid(theta_max, n)
    beta_grid = map_theta_to_beta(theta_grid, theta_einstein)
    
    unlensed_image = source_field(theta_grid, source_list)
    
    lensed_image = source_field(beta_grid, source_list)

    return theta_grid, beta_grid, unlensed_image, lensed_image


