import numpy as np

def gaussian_source(beta_grid, center=(0.6, 0.0), sigma=0.08, amplitude=1.0):
    bx = beta_grid[..., 0]
    by = beta_grid[..., 1]
    cx, cy = center

    r2 = (bx - cx)**2 + (by - cy)**2
    return amplitude * np.exp(-r2 / (2 * sigma**2))