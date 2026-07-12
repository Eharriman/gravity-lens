import numpy as np
from functools import partial

from core.lens_mapping import generate_theta_grid, map_theta_to_beta
from lenses.point_mass import (
    deflection,
    determinant,
    eigenvalues,
    magnification
)

from core.jacobian import (
    point_lens_det_jacobian,
    point_lens_magnification_field,
    point_lens_eigenvalues
)
from models.source_field import source_field

def generate_lensed_field(theta_max, n, theta_einstein, 
                           source_list):
    
    theta_grid = generate_theta_grid(theta_max, n)
    beta_grid = map_theta_to_beta(theta_grid, theta_einstein)

    deflection_function = partial(deflection, theta_einstein=theta_einstein)
    
    unlensed_image = source_field(theta_grid, source_list)
    
    lensed_image = source_field(beta_grid, source_list)

    # Equivalent formulation using Jacobian derivation
    det_jacobian = point_lens_det_jacobian(theta_grid, theta_einstein)
    magnification = point_lens_magnification_field(theta_grid, theta_einstein)
    lambda_r, lambda_t = point_lens_eigenvalues(theta_grid, theta_einstein)

    return {
        "theta_grid": theta_grid,
        "beta_grid": beta_grid,
        "unlensed_image": unlensed_image,
        "lensed_image": lensed_image,
        "det_jacobian": det_jacobian,
        "magnification": magnification,
        "lambda_r": lambda_r,
        "lambda_t": lambda_t,
    }
