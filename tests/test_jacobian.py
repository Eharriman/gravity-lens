import numpy as np
from core.jacobian import point_lens_jacobian, point_lens_det_jacobian, point_lens_magnification_field, point_lens_eigenvalues
from core.lens_equation import image_positions

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

def test_equivalence_jacobian_scalar():
    theta_E = 1.0
    beta = 0.5

    theta_plus, _ = image_positions(beta, theta_E)
    theta_vec = np.array([theta_plus, 0.0])

    mu_field = point_lens_magnification_field(theta_vec, theta_E)

    expected = 1.0 / abs(1.0 - (theta_E / theta_plus)**4)

    assert np.isclose(mu_field, expected, atol=1e-12)