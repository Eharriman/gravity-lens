from pathlib import Path
from datetime import datetime
import matplotlib as plt

OUTPUT_DIR = Path("output")

def generate_filename(prefix="lens", ext="png", tag=None):
    timestamp = datetime.now()

    if tag:
        return f"{prefix}_{tag}_{timestamp}.{ext}"
    return f"{prefix}_{timestamp}.{ext}"


def save_figure(fig, filename=None, prefix="lens", tag=None, dpi=150):
    
    if filename is None:
        filename = generate_filename(prefix=prefix,tag=tag)

    path = OUTPUT_DIR / filename

    fig.savefig(path, dpi=dpi, bbox_inches="tight")
    print("[Output] Simulation figure saved to -> {path}")