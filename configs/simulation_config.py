from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
ASSETS_DIR = PROJECT_ROOT / "assets"
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "output"


@dataclass
class SourceListConfig:
    theta_max: float = 2.0
    n: int = 500
    theta_einstein: float = 0.6
    show_jacobian: bool = False
    save_output: bool = False