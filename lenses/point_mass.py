import numpy as np


_DEFAULT_EPSILON = 1e-12


def deflection(theta, theta_einstein, epsilon=_DEFAULT_EPSILON):
    """
    Compute the reduced deflection angle for a point-mass lens.

    Parameters
    ----------
    theta:
        Angular image-plane coordinates with final dimension 2.
        Accepted shapes include ``(2,)`` and ``(..., 2)``.
    theta_einstein:
        Einstein angle in the same angular units as ``theta``.
    epsilon:
        Numerical lower bound applied to |theta|^2 at the lens centre.

    Returns
    -------
    numpy.ndarray
        Deflection vectors with the same shape as ``theta``.
    """
    theta = np.asarray(theta, dtype=float)

    if theta.shape[-1] != 2:
        raise ValueError(
            f"Expected theta to have shape (..., 2); received {theta.shape}"
        )

    radius_squared = np.sum(theta**2, axis=-1, keepdims=True)
    radius_squared = np.maximum(radius_squared, epsilon)

    return (theta_einstein**2 / radius_squared) * theta


def jacobian(theta, theta_einstein, epsilon=_DEFAULT_EPSILON):
    """
    Compute the Jacobian of the point-mass lens mapping beta(theta).
    """
    theta = np.asarray(theta, dtype=float)

    if theta.shape[-1] != 2:
        raise ValueError(
            f"Expected theta to have shape (..., 2); received {theta.shape}"
        )

    theta_x = theta[..., 0]
    theta_y = theta[..., 1]

    radius_squared = theta_x**2 + theta_y**2
    radius_squared = np.maximum(radius_squared, epsilon)
    radius_fourth = radius_squared**2

    einstein_squared = theta_einstein**2

    a11 = (
        1.0
        - einstein_squared / radius_squared
        + 2.0 * einstein_squared * theta_x**2 / radius_fourth
    )
    a12 = (
        2.0
        * einstein_squared
        * theta_x
        * theta_y
        / radius_fourth
    )
    a21 = a12
    a22 = (
        1.0
        - einstein_squared / radius_squared
        + 2.0 * einstein_squared * theta_y**2 / radius_fourth
    )

    result = np.empty(theta.shape[:-1] + (2, 2), dtype=float)

    result[..., 0, 0] = a11
    result[..., 0, 1] = a12
    result[..., 1, 0] = a21
    result[..., 1, 1] = a22

    return result


def determinant(theta, theta_einstein, epsilon=_DEFAULT_EPSILON):
    """
    Compute det[d beta / d theta] for a point-mass lens.
    """
    matrix = jacobian(theta, theta_einstein, epsilon=epsilon)
    return np.linalg.det(matrix)


def magnification(theta, theta_einstein, epsilon=_DEFAULT_EPSILON):
    """
    Compute the absolute point-source magnification field.

    The value is numerically capped near critical curves by ``epsilon``.
    """
    det = determinant(theta, theta_einstein, epsilon=epsilon)
    return 1.0 / np.maximum(np.abs(det), epsilon)


def eigenvalues(theta, theta_einstein, epsilon=_DEFAULT_EPSILON):
    """
    Compute the radial and tangential eigenvalues of the lens mapping.
    """
    theta = np.asarray(theta, dtype=float)

    if theta.shape[-1] != 2:
        raise ValueError(
            f"Expected theta to have shape (..., 2); received {theta.shape}"
        )

    radius_squared = np.sum(theta**2, axis=-1)
    radius_squared = np.maximum(radius_squared, epsilon)

    einstein_squared = theta_einstein**2

    lambda_radial = 1.0 + einstein_squared / radius_squared
    lambda_tangential = 1.0 - einstein_squared / radius_squared

    return lambda_radial, lambda_tangential


def image_positions(beta, theta_einstein):
    """
    Solve the scalar point-mass lens equation.

    Parameters
    ----------
    beta:
        Signed angular source position along a one-dimensional axis.
    theta_einstein:
        Einstein angle.

    Returns
    -------
    tuple[numpy.ndarray, numpy.ndarray]
        The positive- and negative-parity image positions.
    """
    beta = np.asarray(beta, dtype=float)

    discriminant = np.sqrt(beta**2 + 4.0 * theta_einstein**2)

    theta_plus = 0.5 * (beta + discriminant)
    theta_minus = 0.5 * (beta - discriminant)

    return theta_plus, theta_minus