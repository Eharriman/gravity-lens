import matplotlib.pyplot as plt

def plot_lensed_comparison(unlensed_image, lensed_image, theta_max):
    extent = [-theta_max, theta_max, -theta_max, theta_max]

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    axes[0].imshow(unlensed_image, origin="lower", extent=extent)
    axes[0].set_title("Unlensed Source")
    axes[0].set_xlabel(r"$\theta_x$")
    axes[0].set_ylabel(r"$\theta_y$")

    axes[1].imshow(lensed_image, origin="lower", extent=extent)
    axes[1].set_title("Lensed Image")
    axes[1].set_xlabel(r"$\theta_x$")
    axes[1].set_ylabel(r"$\theta_y$")

    plt.tight_layout()
    plt.show()