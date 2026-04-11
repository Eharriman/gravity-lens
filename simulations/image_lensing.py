import numpy as np
from core.lens_mapping import generate_theta_grid, map_theta_to_beta

def lens_image(image, theta_max, theta_einstein):

    n_y, n_x = image.shape

    theta_grid = generate_theta_grid(theta_max, n_x)

    beta_grid = map_theta_to_beta(theta_grid, theta_einstein)

    beta_x = beta_grid[..., 0]
    beta_y = beta_grid[..., 1]

    beta_x_norm = (beta_x + theta_einstein) / (2 * theta_max)
    beta_y_norm = (beta_y + theta_einstein) / (2 * theta_max)

    px = (beta_x_norm * (n_x - 1)).astype(int)
    py = (beta_y_norm * (n_y - 1)).astype(int)

    px = np.clip(px, 0, n_x - 1)
    py = np.clip(py, 0, n_y - 1)

    lensed = image[py, px]

    return lensed