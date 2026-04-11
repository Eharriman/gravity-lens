from pathlib import Path
from simulations.field_lensing import generate_lensed_field
from render.field_render import plot_lensed_comparison, plot_magnification_and_det

from ingest.image_ingest import load_image
from simulations.image_lensing import lens_image
from render.image_render import plot_image_comparison

ROOT = Path(__file__).resolve().parent
ASSETS_DIR = ROOT / "assets"


def generate_demo_sourcelist():
    return [
        # --- Compact Gaussian sources (stars / compact galaxies) ---
    {"type": "gaussian_circular", "center": (0.6, 0.2), "sigma": 0.05, "amplitude": 1.5},
    {"type": "gaussian_circular", "center": (-0.8, 0.5), "sigma": 0.04, "amplitude": 1.2},
    {"type": "gaussian_circular", "center": (0.3, -0.7), "sigma": 0.06, "amplitude": 1.8},
    {"type": "gaussian_circular", "center": (-0.2, 0.9), "sigma": 0.05, "amplitude": 1.0},
    {"type": "gaussian_circular", "center": (1.1, -0.4), "sigma": 0.03, "amplitude": 0.8},
    {"type": "gaussian_circular", "center": (-1.2, -0.6), "sigma": 0.04, "amplitude": 1.3},

    # --- Elliptical galaxies ---
    {"type": "gaussian_elliptical", "center": (0.9, 0.6), "sigma_major": 0.14, "sigma_minor": 0.05, "angle": 0.3, "amplitude": 1.5},
    {"type": "gaussian_elliptical", "center": (-0.9, 0.1), "sigma_major": 0.12, "sigma_minor": 0.04, "angle": 1.0, "amplitude": 1.3},
    {"type": "gaussian_elliptical", "center": (0.2, 1.0), "sigma_major": 0.10, "sigma_minor": 0.03, "angle": 0.7, "amplitude": 1.1},
    {"type": "gaussian_elliptical", "center": (-0.6, -1.1), "sigma_major": 0.15, "sigma_minor": 0.06, "angle": 0.2, "amplitude": 1.6},
    {"type": "gaussian_elliptical", "center": (1.2, 0.2), "sigma_major": 0.11, "sigma_minor": 0.05, "angle": 1.3, "amplitude": 1.2},
    {"type": "gaussian_elliptical", "center": (-1.0, -0.2), "sigma_major": 0.13, "sigma_minor": 0.04, "angle": 0.5, "amplitude": 1.4},

    # --- Sérsic galaxies (diffuse structure) ---
    {"type": "sersic_source", "center": (-0.4, -0.3), "R_eff": 0.12, "n_sersic": 1.2, "amplitude": 1.0},
    {"type": "sersic_source", "center": (0.5, -0.9), "R_eff": 0.18, "n_sersic": 0.8, "amplitude": 1.2},
    {"type": "sersic_source", "center": (-1.1, 0.8), "R_eff": 0.10, "n_sersic": 2.0, "amplitude": 1.1},
    {"type": "sersic_source", "center": (1.0, 0.9), "R_eff": 0.14, "n_sersic": 1.5, "amplitude": 1.3},
    {"type": "sersic_source", "center": (-0.2, -1.2), "R_eff": 0.16, "n_sersic": 0.9, "amplitude": 1.2},

    # --- Near-lens interesting sources (strong lensing region) ---
    {"type": "gaussian_circular", "center": (0.25, 0.05), "sigma": 0.05, "amplitude": 2.0},
    {"type": "gaussian_elliptical", "center": (-0.3, 0.1), "sigma_major": 0.12, "sigma_minor": 0.04, "angle": 0.4, "amplitude": 1.8},
    {"type": "sersic_source", "center": (0.1, -0.2), "R_eff": 0.10, "n_sersic": 1.0, "amplitude": 1.5},

    # --- Peripheral faint background ---
    {"type": "gaussian_circular", "center": (1.4, -1.2), "sigma": 0.05, "amplitude": 0.7},
    {"type": "gaussian_circular", "center": (-1.5, 1.2), "sigma": 0.04, "amplitude": 0.6},
    {"type": "gaussian_elliptical", "center": (1.3, 1.3), "sigma_major": 0.10, "sigma_minor": 0.04, "angle": 0.9, "amplitude": 0.8},
    {"type": "sersic_source", "center": (-1.4, -1.3), "R_eff": 0.12, "n_sersic": 1.3, "amplitude": 0.9}
    ]


def run_source_list_sim(theta_max=2.0, n=500, theta_einstein=0.6, show_jacobian=False):

    source_list =  generate_demo_sourcelist()

    result = generate_lensed_field(
        theta_max=theta_max,
        n=n,
        theta_einstein=theta_einstein,
        source_list=source_list,
    )

    plot_lensed_comparison(
        result["unlensed_image"],
        result["lensed_image"],
        theta_max,
    )

    if show_jacobian:
        plot_magnification_and_det(
            result["magnification"],
            result["det_jacobian"],
            theta_max,
        )


def run_image_sim(
    image_filename="el_gordo_james_webb.png",
    theta_max=2.0,
    theta_einstein=0.35,
    grayscale=False,
):
    image_path = ASSETS_DIR / image_filename
    image = load_image(image_path, grayscale=grayscale)

    lensed = lens_image(
        image=image,
        theta_max=theta_max,
        theta_einstein=theta_einstein,
    )

    plot_image_comparison(image, lensed)


if __name__ == "__main__":
    
    SIM_MODE = "image"

    if SIM_MODE == "source_list":
            run_source_list_sim(
            theta_max=2.0,
            n=500,
            theta_einstein=0.6,
            show_jacobian=False,
        )
    
    
    elif SIM_MODE == "image":
        run_image_sim(
            image_filename="el_gordo_james_webb.png",
            theta_max=25,
            theta_einstein=2,
            grayscale=False,
        )
    
    
    else:
         raise ValueError(f"Invalid simulation mode: {SIM_MODE}")
