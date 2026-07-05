import numpy as np

def sample_nearest(image, px, py, fill_value=0.0):
    image = np.asarray(image)
    px = np.asarray(px, dtype=float)
    py = np.asarray(py, dtype=float)

    if image.ndim == 2:
        h, w = image.shape
        sampled = np.full(px.shape, fill_value, dtype=image.dtype)
    elif image.ndim == 3:
        h, w, channels = image.shape
        sampled = np.full(px.shape + (channels,), fill_value, dtype=image.dtype)
    else:
        raise ValueError(f"Unsupported image shape: {image.shape}")

    ix = np.rint(px).astype(int)
    iy = np.rint(py).astype(int)

    valid = (ix >= 0) & (ix < w) & (iy >= 0) & (iy < h)

    if image.ndim == 2:
        sampled[valid] = image[iy[valid], ix[valid]]
    else:
        sampled[valid] = image[iy[valid], ix[valid], :]

    return sampled


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
    y0 = np.floor(py).astype(int)
    x1 = x0 + 1
    y1 = y0 + 1

    dx = px - x0
    dy = py - y0

    valid = (x0 >= 0) & (x1 < w) & (y0 >= 0) & (y1 < h)

    if channels is None:
        sampled = np.full(px.shape, fill_value, dtype=float)
    else:
        sampled = np.full(px.shape + (channels,), fill_value, dtype=float)
    
    if not np.any(valid):
        return sampled

    x0v = x0[valid]
    x1v = x1[valid]
    y0v = y0[valid]
    y1v = y1[valid]

    dxv = dx[valid]
    dyv = dy[valid]

    wa = (1.0 - dxv) * (1.0 - dyv)
    wb = dxv * (1.0 - dyv)
    wc = (1.0 - dxv) * dyv
    wd = dxv * dyv

    if channels is None:
        Ia = image[y0v, x0v]
        Ib = image[y0v, x1v]
        Ic = image[y1v, x0v]
        Id = image[y1v, x1v]

        sampled[valid] = wa * Ia + wb * Ib + wc * Ic + wd * Id
    else:
        Ia = image[y0v, x0v, :]
        Ib = image[y0v, x1v, :]
        Ic = image[y1v, x0v, :]
        Id = image[y1v, x1v, :]

        sampled[valid] = (
            wa[:, None] * Ia
            + wb[:, None] * Ib
            + wc[:, None] * Ic
            + wd[:, None] * Id
        )

    return sampled