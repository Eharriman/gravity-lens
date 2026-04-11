import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def load_image(path, grayscale=True, normalize=True):

    img = Image.open(path)

    if grayscale:
        img = img.convert("L")

    img_arr = np.array(img, dtype=float)

    if normalize:
        img_arr /= img_arr.max()

    return img_arr