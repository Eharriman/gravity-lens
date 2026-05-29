from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ASSETS_DIR = PROJECT_ROOT / "assets"
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "output"


@dataclass
class SourceListConfig:
    theta_max: float = 2.0
    n: int = 500
    theta_einstein: float = 0.6
    scene_name: str = "simple"
    show_jacobian: bool = False
    save_output: bool = False


@dataclass
class ImageLensingConfig:
    image_filename: str = "el_gordo_james_webb.png"
    theta_max: float = 2.0
    theta_einstein: float = 0.35
    grayscale: bool = False

    interpolation_mode: str = "bilinear"  # "nearest" or "bilinear"
    fill_value: float = 0.0
    mask_radius: Optional[float] = 0.08

    save_output: bool = False
    tag: str = None


@dataclass
class AppConfig:
    simulation_mode: str = "source_list"  # "source_list" or "image"

    source_list: SourceListConfig = field(default_factory=SourceListConfig)
    image_lensing: ImageLensingConfig = field(default_factory=ImageLensingConfig)