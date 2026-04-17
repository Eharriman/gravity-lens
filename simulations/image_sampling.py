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
    
    return