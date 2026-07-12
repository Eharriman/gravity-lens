from collections.abc import Callable

import numpy as np
from core.deflection import point_lens_deflection

DeflectionFunction = Callable[[np.ndarray], np.ndarray]

def map_theta_to_beta(theta, deflection_function):
    '''
    Method is used to return the source image vector from a given observation angular vector and Einstein Angle.
    A theta vector, the observed location of the image, is provided along with the Einstein angle. 
    The angle of deflection is determeined using the point_lens_deflection method.
    The beta vector is the difference between the theta vector and the deflection angle
    '''

    theta = np.asarray(theta, dtype=float)
    alpha = np.asarray(deflection_function(theta), dtype=float )

    if alpha.shape != theta.shape:
        raise ValueError(
            "Deflection output and theta shape must be the same."  
        )

    #theta_vec = np.asarray(theta_vec, dtype=float)
    #alpha = point_lens_deflection(theta_vec, theta_einstein)
    #beta = theta_vec - alpha

    return theta - alpha


'''

def generate_theta_grid(theta_max, n):
    x = np.linspace(-theta_max, theta_max, n)
    y = np.linspace(-theta_max, theta_max, n)
    #grid = np.stack(np.meshgrid(x,y), axis=-1)

    X, Y = np.meshgrid(x, y, indexing="xy")
    return np.stack((X,Y), axis=-1)

'''

def generate_theta_grid(theta_max, n):
    if theta_max <= 0:
        raise ValueError("theta_max must be a positive number.")
    
    if n < 2:
        raise ValueError("n must be greater than 2")
    
    axis = np.linspace(-theta_max, theta_max, n)

    theta_x, theta_y = np.meshgrid(axis, axis, indexing='xy')

    return np.stack((theta_x, theta_y), axis =-1)

#print(generate_theta_grid(1, 3))
