import numpy as np

def generated_pointLensDeflection(theta_vec, theta_einstein):

    norm_sqr = np.dot(theta_vec, theta_vec)

    return (theta_einstein ** 2 / norm_sqr) * theta_vec


def map_source_to_lens(theta_vec, theta_einstein):
    
    alpha = generated_pointLensDeflection(theta_vec, theta_einstein)

    beta = theta_vec - alpha
