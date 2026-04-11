import matplotlib.pyplot as plt
import numpy as np

def plot_lensed_comparison(unlensed_image, lensed_image, theta_max):
    extent = [-theta_max, theta_max, -theta_max, theta_max]

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    axes[0].imshow(unlensed_image, origin="lower", extent=extent, vmin=0, vmax=4.0, cmap="inferno")
    axes[0].set_title("Unlensed Source")
    axes[0].set_xlabel(r"Angular displacement: $\theta_x$")
    axes[0].set_ylabel(r"Angular displacement: $\theta_y$")

    axes[1].imshow(lensed_image, origin="lower", extent=extent, vmin=0, vmax=4.0, cmap="inferno")
    axes[1].set_title("Lensed Image")
    axes[1].set_xlabel(r"Angular displacement: $\theta_x$")
    axes[1].set_ylabel(r"Angular displacement: $\theta_y$")

    plt.tight_layout()
    plt.show()


def plot_magnification_and_det(magnification, det_jacobian, theta_max):
    extent = [-theta_max, theta_max, -theta_max, theta_max]

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    im0 = axes[0].imshow(
        np.log10(magnification),
        origin="lower",
        extent=extent
    )
    axes[0].set_title(r"$\log_{10}\mu(\theta)$")
    axes[0].set_xlabel(r"$\theta_x$")
    axes[0].set_ylabel(r"$\theta_y$")
    plt.colorbar(im0, ax=axes[0])

    
    im1 = axes[1].imshow(
        det_jacobian,
        origin="lower",
        extent=extent
    )

    axes[1].set_title(r"$\det A(\theta)$")
    axes[1].set_xlabel(r"$\theta_x$")
    axes[1].set_ylabel(r"$\theta_y$")
    plt.colorbar(im1, ax=axes[1])

    plt.tight_layout()
    plt.show()