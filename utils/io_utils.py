from pathlib import Path
from datetime import datetime
import matplotlib as plt

OUTPUT_DIR = Path("output")

def generate_filename(prefix="lens", ext="png", tag=None):
    timestamp = datetime.now()

    if tag:
        return f"{prefix}_{tag}_{timestamp}.{ext}"
    return f"{prefix}_{timestamp}.{ext}"