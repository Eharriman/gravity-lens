import numpy as np

def image_positions(beta, einstein_angle):

    beta = np.asarray(beta)
    sqrt_term = np.sqrt(beta**2 + 4 * einstein_angle**2)

    theta_plus = 0.5 * (beta + sqrt_term)
    theta_minus = 0.5 * (beta - sqrt_term)

    return theta_plus, theta_minus

