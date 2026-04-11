import matplotlib.pyplot as plt


def plot_image_comparison(original, lensed):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    axes[0].imshow(original, cmap="gray")
    axes[0].set_title("Original Unlensed Image")
    axes[0].axis("off")

    axes[1].imshow(lensed, cmap="gray")
    axes[1].set_title("Lensed Image")
    axes[1].axis("off")

    plt.tight_layout()
    plt.show()