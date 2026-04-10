import numpy as np
from core.jacobian import point_lens_jacobian

def test_jacobian_symmetry():
    theta = np.asarray([1.2,2.4])

    jac = point_lens_jacobian(theta, 0.5)

    assert np.isclose(jac[0,1], jac[1,0], atol=1e-12)