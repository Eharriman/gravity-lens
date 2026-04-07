import numpy as np

def point_lens_deflection(theta_vec, theta_einstein):

    theta_vec = np.asarray(theta_vec, dtype=float)
    
    eps = 1e-12
    r2 = np.sum(theta_vec**2, axis =-1, keepdims=True)
    r2 = np.maximum(r2, eps)
    #r2 = max(np.dot(theta_vec, theta_vec), eps)
    #r2 = np.dot(theta_vec, theta_vec)
    
    return (theta_einstein ** 2 / r2) * theta_vec

'''
# Moved this method to lens_mapping.py

def map_theta_to_beta(theta_vec, theta_einstein):
    
    alpha = point_lens_deflection(theta_vec, theta_einstein)

    beta = theta_vec - alpha

    return beta
'''
