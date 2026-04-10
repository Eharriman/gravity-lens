import numpy as np

def point_lens_jacobian(theta_vec, theta_einstein):
    
    theta_vec = np.asarray(theta_vec, dtype=float)

    tx = theta_vec[..., 0]
    ty = theta_vec[..., 1]

    r2 = tx**2 + ty**2
    eps = 1e-12
    r2 = np.maximum(r2, eps)
    r4 = r2**2

    te2 = theta_einstein**2

    a11 = 1 - te2 / r2 + 2 * te2 * tx * tx / r4
    a12 = 2 * te2 * tx * ty / r4
    a21 = 2 * te2 * ty * tx / r4
    a22 = 1 - te2 / r2 + 2 * te2 * ty * ty / r4

    jac = np.empty(theta_vec.shape[:-1] + (2, 2), dtype=float)
    jac[..., 0, 0] = a11
    jac[..., 0, 1] = a12
    jac[..., 1, 0] = a21
    jac[..., 1, 1] = a22

    return jac


def point_lens_det_jacobian(theta_vec, theta_einstein):

    jac = point_lens_jacobian(theta_vec, theta_einstein)
    det = jac[...,0,0]*jac[...,1,1] - jac[...,1,0]*jac[...,0,1]

    return det     


def point_lens_magnification_field(theta_vec, theta_einstein):
    '''
    The overall increase in the size of a lensed source is given by the inverse of the determinant of the Jacobian

    mu = 1/|det A|
    '''
    det = point_lens_det_jacobian(theta_vec, theta_einstein)
    eps = 1e-12

    return 1.0 / np.maximum(np.absolute(det), eps)


def point_lens_eigenvalues(theta_vec, theta_einstein):
    """
    Calculates the radial and tangential eigenvalues of the transformation matrix.
    """
    theta_vec = np.asarray(theta_vec, dtype=float)
    r2 = np.sum(theta_vec**2, axis=-1)
    eps = 1e-12
    r2 = np.maximum(r2, eps)

    te2 = theta_einstein**2

    lambda_r = 1 + te2 / r2
    lambda_t = 1 - te2 / r2

    return lambda_r, lambda_t


'''
For a theta = [2,3] and theta_E = 1/3 the Jacobian matrix should be:

A_11 = 0.970414201183
A_12 = A_21 = 0.0710059171598
A_22
'''

'''
theta_vec = np.array([2,3])
theta_E = (1/3)
jac = point_lens_jacobian(theta_vec, theta_E)
det = point_lens_det_jacobian(theta_vec, theta_E)
print(det)
#print(jac)
'''