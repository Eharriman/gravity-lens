import argparse

from pathlib import Path
from simulations.field_lensing import generate_lensed_field
from render.field_render import plot_lensed_comparison, plot_magnification_and_det

from ingest.image_ingest import load_image
from simulations.image_lensing import lens_image
from simulations.image_lensing_interp import lens_image_interp
from render.image_render import plot_image_comparison

from configs.simulation_config import AppConfig, ASSETS_DIR
from configs.demo_scenes import build_demo_source_list, get_demo_scene

ROOT = Path(__file__).resolve().parent
ASSETS_DIR = ROOT / "assets"


def parse_args():
    
    parser = argparse.ArgumentParser(description="Gravity-Lens Sim")

    # Mode config
    parser.add_argument("--mode", choices=["source_list", "image"], default=None)

    # Source list mode
    parser.add_argument("--scene", choice=["simple","einstein_ring"], default=None)

    #pass
    return parser.parse_args()


def apply_parse_config(config, args):
    
    if args.mode is not None:
        config.simulation_mode = args.mode

    return config

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


def run_source_list_sim(config):
    #source_list = build_demo_source_list()
    source_list = get_demo_scene(config.scene_name)

    result = generate_lensed_field(
        theta_max=config.theta_max,
        n=config.n,
        theta_einstein=config.theta_einstein,
        source_list=source_list,
    )

    plot_lensed_comparison(
        result["unlensed_image"],
        result["lensed_image"],
        config.theta_max,
    )

    if config.show_jacobian:
        plot_magnification_and_det(
            result["magnification"],
            result["det_jacobian"],
            config.theta_max,
        )


def run_image_sim(config):
    image_path = ASSETS_DIR / config.image_filename
    image = load_image(image_path, grayscale=config.grayscale)

    if config.interpolation_mode == "nearest":
        lensed = lens_image(
            image=image,
            theta_max=config.theta_max,
            theta_einstein=config.theta_einstein,
        )

    elif config.interpolation_mode == "bilinear":
        lensed = lens_image_interp(
            image=image,
            theta_max=config.theta_max,
            theta_einstein=config.theta_einstein,
            fill_value=config.fill_value,
            mask_radius=config.mask_radius,
        )

    else:
        raise ValueError(f"Unknown interpolation mode: {config.interpolation_mode}")


    plot_image_comparison(image, lensed, config.save_output, config.tag)


if __name__ == "__main__":
    
    app_config = AppConfig()

    #app_config.simulation_mode = "source_list"
    app_config.simulation_mode = "image"

    #app_config.source_list.scene_name = "einstein_ring"
    app_config.source_list.scene_name = "simple"
    app_config.image_lensing.image_filename = "el_gordo_james_webb.png"
    app_config.image_lensing.theta_einstein = 0.9

    if app_config.simulation_mode == "source_list":
         run_source_list_sim(app_config.source_list)
    elif app_config.simulation_mode == "image":
        run_image_sim(app_config.image_lensing)
    else:
        raise ValueError(f"Unknown simulation mode: {app_config.simulation_mode}")
