def build_demo_source_list():
    return [
        {"type": "gaussian_circular", "center": (0.6, 0.2), "sigma": 0.05, "amplitude": 1.5},
        {"type": "gaussian_circular", "center": (-0.8, 0.5), "sigma": 0.04, "amplitude": 1.2},
        {"type": "gaussian_elliptical", "center": (0.9, 0.6), "sigma_major": 0.14, "sigma_minor": 0.05, "angle": 0.3, "amplitude": 1.5},
        {"type": "sersic_source", "center": (-0.4, -0.3), "R_eff": 0.12, "n_sersic": 1.2, "amplitude": 1.0},
    ]