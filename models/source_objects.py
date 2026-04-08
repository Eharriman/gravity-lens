import numpy as np

def gaussian_source(beta_grid, center=(0.6, 0.0), sigma=0.08, amplitude=1.0):
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


def sersic_source(beta_grid, center=(0.6, 0.0), amplitude=1.0, R_eff=0.2, n_sersic=1.0):

    bx = beta_grid[..., 0]
    by = beta_grid[..., 1]
    cx, cy = center

    r = np.sqrt((bx - cx)**2 + (by - cy)**2)
    
    bn = 1.9992 * n_sersic - 0.3271
    
    # 3. Sersic formula
    exponent = -bn * ((r / R_eff)**(1 / n_sersic) - 1)
    return amplitude * np.exp(exponent)