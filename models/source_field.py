import numpy as np

from models.source_objects import (
    gaussian_circular,
    gaussian_elliptical,
    sersic_source
)

def source_field(beta_grid, source_list):

    total_field = np.zeros(beta_grid.shape[:-1], dtype=float)

    for source in source_list:
        source_type = source["type"]

        if source_type == "gaussian_circular":
            total_field += gaussian_circular(
                beta_grid,
                center=source.get("center", (0.0, 0.0)),
                sigma= source.get("sigma", 0.1),
                amplitude = source.get("amplitude", 1.0),
            )
        
        elif source_type == "sersic_source":
            total_field += sersic_source(
                beta_grid,
                center=source.get("center", (0.0, 0.0)),
                amplitude = source.get("amplitude", 1.0),
                R_eff = source.get("R_eff", 0.2),
                n_sersic = source.get("n_sersic", 1.0)
            )
        
        elif source_type == "gaussian_elliptical":
            total_field += gaussian_elliptical(
                beta_grid,
                center=source.get("center", (0.0, 0.0)),
                sigma_major=source.get("sigma_major", 0.15),
                sigma_minor=source.get("sigma_minor", 0.08),
                angle=source.get("angle", 0.0),
                amplitude=source.get("amplitude", 1.0),
            )
        
        else:
            raise ValueError(f"Source object {source_type} is not in object catalogue source_objects.py")
        
    return total_field