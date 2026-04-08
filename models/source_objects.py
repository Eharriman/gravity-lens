import numpy as np

def gaussian_circular(beta_grid, center=(0.6, 0.0), sigma=0.08, amplitude=1.0):
    '''
    This is your basic amorphous blob. The parameters are the standard for a Gaussian distribution:
    center: tuple indicating the center of the "blob" in the x,y plane
    sigma: the std. deviation. A large sigma produces a blurry/fuzzy shape, whereas a small sigma a sharper picture
    amplitude: the brightness at the center of the galaxy
    '''
    bx = beta_grid[..., 0]
    by = beta_grid[..., 1]
    cx, cy = center

    r2 = (bx - cx)**2 + (by - cy)**2
    return amplitude * np.exp(-r2 / (2 * sigma**2))


def gaussian_elliptical(
    beta_grid,
    center=(0.0, 0.0),
    sigma_major=0.15,
    sigma_minor=0.08,
    angle=0.0,
    amplitude=1.0
):

    bx = beta_grid[..., 0]
    by = beta_grid[..., 1]
    cx, cy = center

    x = bx - cx
    y = by - cy

    cos_a = np.cos(angle)
    sin_a = np.sin(angle)

    x_rot = cos_a * x + sin_a * y
    y_rot = -sin_a * x + cos_a * y

    exponent = (
        (x_rot**2) / (2 * sigma_major**2)
        + (y_rot**2) / (2 * sigma_minor**2)
    )

    return amplitude * np.exp(-exponent)


def sersic_source(beta_grid, center=(0.6, 0.0), amplitude=1.0, R_eff=0.2, n_sersic=1.0):
    '''
    Sersic shape which produces a pretty cute model of a distance circular galaxy.
    center: center of shape
    amplitude: brightness
    R_eff: effective radius (1/2 total light contained within this radius)
    n_sersic: Sersic index -- controls shape
    '''

    bx = beta_grid[..., 0]
    by = beta_grid[..., 1]
    cx, cy = center

    r = np.sqrt((bx - cx)**2 + (by - cy)**2)
    
    bn = 1.9992 * n_sersic - 0.3271
    
    # 3. Sersic formula
    exponent = -bn * ((r / R_eff)**(1 / n_sersic) - 1)
    return amplitude * np.exp(exponent)