import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from core.lens_equation import image_positions
#from core.lens_equation import image_positions

def plot_image_positions(einstein_angle=1.0):
    beta_vals = np.linspace(0.01, 5, 500)
    theta_p, theta_m = image_positions(beta_vals, einstein_angle)

    plt.plot(beta_vals, theta_p, label="θ+")
    plt.plot(beta_vals, theta_m, label="θ−")
    plt.xlabel("β")
    plt.ylabel("θ")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    plot_image_positions()