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