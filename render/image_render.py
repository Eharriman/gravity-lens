import matplotlib.pyplot as plt
from utils.io_utils import save_figure


def plot_image_comparison(original, lensed, save=False, tag=None):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    axes[0].imshow(original, cmap="gray")
    axes[0].set_title("Original Unlensed Image")
    axes[0].axis("off")

    axes[1].imshow(lensed, cmap="gray")
    axes[1].set_title("Lensed Image")
    axes[1].axis("off")

    if save:
        save_figure(fig, prefix="field_lens", tag=tag)

    plt.tight_layout()
    plt.show()