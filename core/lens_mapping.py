import numpy as np
from core.deflection import point_lens_deflection

def map_theta_to_beta(theta_vec, theta_einstein):

    theta_vec = np.asarray(theta_vec, dtype=float)
    
    alpha = point_lens_deflection(theta_vec, theta_einstein)

    beta = theta_vec - alpha

    return beta
