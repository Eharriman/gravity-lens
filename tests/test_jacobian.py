import numpy as np
from core.jacobian import point_lens_jacobian, point_lens_det_jacobian, point_lens_eigenvalues, point_lens_magnfication_field

def test_jacobian_symmetry():
    theta = np.asarray([1.2,2.4])

    jac = point_lens_jacobian(theta, 0.5)

    assert np.isclose(jac[0,1], jac[1,0], atol=1e-12)


def  test_jacobian_eigenvalues():
    theta = np.asarray([1.2,2.4])
    jac = point_lens_jacobian(theta, 0.5)
    det = point_lens_det_jacobian(theta, 0.5)
    lambda_r, lambda_t = point_lens_eigenvalues(theta, 0.5)

    assert np.isclose(det, lambda_r*lambda_t, atol=1e-12)