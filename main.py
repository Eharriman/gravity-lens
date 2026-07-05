import argparse

from pathlib import Path

from render.field_render import plot_lensed_comparison, plot_magnification_and_det

from ingest.image_ingest import load_image

from simulations.field_lensing import generate_lensed_field
from simulations.image_lensing import lens_image
from render.image_render import plot_image_comparison

from configs.simulation_config import AppConfig, ASSETS_DIR
from configs.demo_scenes import build_demo_source_list, get_demo_scene, list_demo_scenes

from cli.commands import print_available_scenes
from cli.parser import parse_args

ROOT = Path(__file__).resolve().parent
ASSETS_DIR = ROOT / "assets"

'''
def parse_args():
    
    parser = argparse.ArgumentParser(description="Gravity-Lens Sim")

    # Mode config
    parser.add_argument("--mode", choices=["source_list", "image"], default=None)

    # Source list mode
    parser.add_argument("--scene", choices=["simple","einstein_ring", "populated"], default=None)
    parser.add_argument("--n", type=int, default=None)

    # Image mode
    parser.add_argument("--image", type=str, default=None)
    parser.add_argument("--interp", choices=["nearest", "bilinear"], default=None)
    parser.add_argument("--grayscale", action="store_true")
    parser.add_argument("--mask-radius", type=float, default=None)

    # Additional
    parser.add_argument("--theta-max", type=float, default=None)
    parser.add_argument("--theta-einstein", type=float, default=None)
    parser.add_argument("--show-jacobian", action="store_true")

    # Helper/User commands
    parser.add_argument("--list-scenes", action="store_true")
    parser.add_argument("--list-modes", action="store_true")
                        
    #pass
    return parser.parse_args()
'''

def apply_parse_config(config, args):
    
    if args.list_scenes:
        print_available_scenes()
        raise SystemExit

    if args.mode is not None:
        config.simulation_mode = args.mode

    if args.scene is not None:
        config.source_list.scene_name = args.scene

    if args.n is not None:
        config.source_list.n = args.n

    if args.theta_max is not None:
        config.source_list.theta_max = args.theta_max
        config.image_lensing.theta_max = args.theta_max

    if args.theta_einstein is not None:
        config.source_list.theta_einstein = args.theta_einstein
        config.image_lensing.theta_einstein = args.theta_einstein

    if args.image is not None:
        config.image_lensing.image_filename = args.image

    if args.interp is not None:
        config.image_lensing.interpolation_mode = args.interp

    if args.grayscale:
        config.image_lensing.grayscale = True

    if args.mask_radius is not None:
        config.image_lensing.mask_radius = args.mask_radius

    if args.show_jacobian:
        config.source_list.show_jacobian = True

    return config


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

    lensed = lens_image(
    image=image,
    theta_max=config.theta_max,
    theta_einstein=config.theta_einstein,
    interpolation_mode=config.interpolation_mode,
    fill_value=config.fill_value,
    mask_radius=config.mask_radius,
    )

    plot_image_comparison(image, lensed, config.save_output, config.tag)

'''
def print_available_scenes():
    print("Available source-list scenes:")
    for scene in list_demo_scenes():
        print(f" {scene}")
'''


if __name__ == "__main__":

    args = parse_args()
    app_config = AppConfig()
    app_config = apply_parse_config(app_config, args)

    #app_config.simulation_mode = "source_list"
    #app_config.simulation_mode = "image"

    #app_config.source_list.scene_name = "einstein_ring"
    #app_config.source_list.scene_name = "simple"
    #app_config.image_lensing.image_filename = "el_gordo_james_webb.png"
    #app_config.image_lensing.theta_einstein = 0.9

    '''
    Running: python .\main.py --mode source_list --scene simple    
    '''

    if app_config.simulation_mode == "source_list":
         run_source_list_sim(app_config.source_list)
    elif app_config.simulation_mode == "image":
        run_image_sim(app_config.image_lensing)
    else:
        raise ValueError(f"Unknown simulation mode: {app_config.simulation_mode}")
