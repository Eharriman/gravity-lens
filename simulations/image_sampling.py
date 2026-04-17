import numpy as np

def sample_bilinear(image, px, py, fill_value=0.0):

    image = np.asarray(image)
    px = np.asarray(px, dtype=float)
    py = np.asarray(py, dtype=float)

    if image.ndim == 2:
        h, w = image.shape
        channels = None
    elif image.ndim == 3:
        h, w, channels = image.shape
    else:
        raise ValueError(f"Unsupported image shape: {image.shape}")
    
    
    x0 = np.floor(px).astype(int)
    y0 = np.floor(yx).astype(int)
    x1 = x0 + 1
    y1 = y0 + 1

    dx = px - x0
    dy = py - y0

    valid = (x0 >= 0) & (x1 < w) & (y0 >= 0) & (y1 < h)

    if channels is None:
        sampled = np.full(px.shape, fill_value, dtype=float)
    else:
        sampled = np.full(px.shape + (channels,), fill_value, dtype=float)