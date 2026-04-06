import numpy as np
from core.deflection import point_lens_deflection
from core.lens_mapping import map_theta_to_beta

def test_radial_symmetry():
    # Function tests whether theta vector and beta vector are parallel
    
    theta_E = 1.0

    theta = np.asarray([1.2, 0.8], dtype=float)

    beta = map_theta_to_beta(theta, theta_E)

    # Parallel consistency verified manually with cross product

    cross = (theta[0] * beta[1]) - (theta[1] * beta[0])

    assert np.isclose(cross, 0.0, atol=1e-10)
