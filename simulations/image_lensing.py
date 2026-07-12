import numpy as np
from core.lens_mapping import generate_theta_grid, map_theta_to_beta
from simulations.image_sampling import sample_bilinear, sample_nearest

from functools import partial

from core.lens_mapping import map_theta_to_beta
from lenses.point_mass import deflection

def generate_theta_grid_rect(theta_max, n_x, n_y):
    x = np.linspace(-theta_max, theta_max, n_x)
    y = np.linspace(-theta_max, theta_max, n_y)
    X, Y = np.meshgrid(x, y, indexing="xy")
    return np.stack((X, Y), axis=-1)


def theta_to_pixel_coords(beta_grid, theta_max, n_x, n_y):
    beta_x = beta_grid[..., 0]
    beta_y = beta_grid[..., 1]

    px = (beta_x + theta_max) / (2.0 * theta_max) * (n_x - 1)
    py = (beta_y + theta_max) / (2.0 * theta_max) * (n_y - 1)

    return px, py


def apply_central_mask(lensed, theta_grid, mask_radius, fill_value=0.0):
    if mask_radius is None or mask_radius <= 0:
        return lensed

    theta_x = theta_grid[..., 0]
    theta_y = theta_grid[..., 1]
    r2 = theta_x**2 + theta_y**2

    mask = r2 < mask_radius**2
    lensed[mask] = fill_value

    return lensed


def lens_image(image, theta_max, theta_einstein, interpolation_mode="bilinear", fill_value=0.0, mask_radius=None):

    if image.ndim == 2:
        n_y, n_x = image.shape
        n_channels = None
    elif image.ndim == 3:
        n_y, n_x, n_channels = image.shape
    else:
        raise ValueError(f"Unsupported image shape: {image.shape}")

    theta_grid = generate_theta_grid(theta_max, n_x)
    #beta_grid = map_theta_to_beta(theta_grid, theta_einstein)
    
    deflection_function = partial(
        deflection,
        theta_einstein=theta_einstein
    )

    beta_grid = map_theta_to_beta(
        theta_grid,
        deflection_function
    )

    px, py = theta_to_pixel_coords(beta_grid, theta_max, n_x, n_y)

    #beta_x = beta_grid[..., 0]
    #beta_y = beta_grid[..., 1]

    #beta_x_norm = (beta_x + theta_max) / (2 * theta_max)
    #beta_y_norm = (beta_y + theta_max) / (2 * theta_max)

    
    #px = (beta_x_norm * (n_x - 1)).astype(int)
    #py = (beta_y_norm * (n_y - 1)).astype(int)

    #px = np.clip(px, 0, n_x - 1)
    #py = np.clip(py, 0, n_y - 1)

    if interpolation_mode == "nearest":
        lensed = sample_nearest(image, px, py, fill_value=fill_value)
    elif interpolation_mode == "bilinear":
        lensed = sample_bilinear(image, px, py, fill_value=fill_value)
    else:
        raise ValueError(f"Unknown interpolation mode: {interpolation_mode}")
    
    '''
    if image.ndim == 2:
        lensed = image[py, px]
    else:
        lensed = image[py, px, :]
    '''

    lensed = apply_central_mask(
        lensed=lensed,
        theta_grid=theta_grid,
        mask_radius=mask_radius,
        fill_value=fill_value,
    )
    
    return lensed