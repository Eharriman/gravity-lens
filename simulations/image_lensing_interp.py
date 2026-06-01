import numpy as np
from core.lens_mapping import map_theta_to_beta
from simulations.image_sampling import sample_bilinear

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


def lens_image_interp(image, theta_max, theta_einstein, fill_value=0.0, mask_radius=None):

    image = np.asarray(image)

    if image.ndim == 2:
        n_y, n_x = image.shape
    elif image.ndim == 3:
        n_y, n_x, _ = image.shape
    else:
        raise ValueError(f"Unsupported image shape: {image.shape}")

    theta_grid = generate_theta_grid_rect(theta_max, n_x, n_y)
    beta_grid = map_theta_to_beta(theta_grid, theta_einstein)
    px, py = theta_to_pixel_coords(beta_grid, theta_max, n_x, n_y)

    beta_x = beta_grid[..., 0]
    beta_y = beta_grid[..., 1]

    #px = (beta_x + theta_max) / (2.0 * theta_max) * (n_x - 1)
    #py = (beta_y + theta_max) / (2.0 * theta_max) * (n_y - 1)

    lensed = sample_bilinear(image, px, py, fill_value=fill_value)

    if mask_radius is not None and mask_radius > 0:
        theta_x = theta_grid[..., 0]
        theta_y = theta_grid[..., 1]

        r2 = theta_x**2 + theta_y**2

        mask = r2 < (mask_radius**2)

        if image.ndim == 2:
            lensed[mask] = fill_value
        if image.ndim == 3:
            lensed[mask] = fill_value

    return lensed
