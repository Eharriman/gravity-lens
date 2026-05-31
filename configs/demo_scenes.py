def build_demo_source_list():
    return [
        {"type": "gaussian_circular", "center": (0.6, 0.2), "sigma": 0.05, "amplitude": 1.5},
        {"type": "gaussian_circular", "center": (-0.8, 0.5), "sigma": 0.04, "amplitude": 1.2},
        {"type": "gaussian_elliptical", "center": (0.9, 0.6), "sigma_major": 0.14, "sigma_minor": 0.05, "angle": 0.3, "amplitude": 1.5},
        {"type": "sersic_source", "center": (-0.4, -0.3), "R_eff": 0.12, "n_sersic": 1.2, "amplitude": 1.0},
    ]


def build_simple_source_list():
    return [
        {
            "type": "gaussian_circular",
            "center": (0.6, 0.2),
            "sigma": 0.06,
            "amplitude": 2.2,
        },
        {
            "type": "gaussian_elliptical",
            "center": (-0.5, 0.4),
            "sigma_major": 0.14,
            "sigma_minor": 0.05,
            "angle": 0.6,
            "amplitude": 5.5,
        },
        {
            "type": "sersic_source",
            "center": (-0.3, -0.4),
            "amplitude": 1.0,
            "R_eff": 0.12,
            "n_sersic": 1.2,
        },
    ]


def build_einstein_ring_source():
    return [
        {
           "type": "gaussian_circular",
            "center": (0.0, 0.0),
            "sigma": 0.08,
            "amplitude": 1.0, 
        }
    ]


def build_populated_source_list():
    return [
        {"type": "gaussian_circular", "center": (0.6, 0.2), "sigma": 0.05, "amplitude": 1.5},
        {"type": "gaussian_circular", "center": (-0.8, 0.5), "sigma": 0.04, "amplitude": 1.2},
        {"type": "gaussian_circular", "center": (0.3, -0.7), "sigma": 0.06, "amplitude": 1.8},
        {"type": "gaussian_circular", "center": (-0.2, 0.9), "sigma": 0.05, "amplitude": 1.0},
        {"type": "gaussian_circular", "center": (1.1, -0.4), "sigma": 0.03, "amplitude": 0.8},
        {"type": "gaussian_circular", "center": (-1.2, -0.6), "sigma": 0.04, "amplitude": 1.3},

        {"type": "gaussian_elliptical", "center": (0.9, 0.6), "sigma_major": 0.14, "sigma_minor": 0.05, "angle": 0.3, "amplitude": 1.5},
        {"type": "gaussian_elliptical", "center": (-0.9, 0.1), "sigma_major": 0.12, "sigma_minor": 0.04, "angle": 1.0, "amplitude": 1.3},
        {"type": "gaussian_elliptical", "center": (0.2, 1.0), "sigma_major": 0.10, "sigma_minor": 0.03, "angle": 0.7, "amplitude": 1.1},
        {"type": "gaussian_elliptical", "center": (-0.6, -1.1), "sigma_major": 0.15, "sigma_minor": 0.06, "angle": 0.2, "amplitude": 1.6},
        {"type": "gaussian_elliptical", "center": (1.2, 0.2), "sigma_major": 0.11, "sigma_minor": 0.05, "angle": 1.3, "amplitude": 1.2},
        {"type": "gaussian_elliptical", "center": (-1.0, -0.2), "sigma_major": 0.13, "sigma_minor": 0.04, "angle": 0.5, "amplitude": 1.4},

        {"type": "sersic_source", "center": (-0.4, -0.3), "R_eff": 0.12, "n_sersic": 1.2, "amplitude": 1.0},
        {"type": "sersic_source", "center": (0.5, -0.9), "R_eff": 0.18, "n_sersic": 0.8, "amplitude": 1.2},
        {"type": "sersic_source", "center": (-1.1, 0.8), "R_eff": 0.10, "n_sersic": 2.0, "amplitude": 1.1},
        {"type": "sersic_source", "center": (1.0, 0.9), "R_eff": 0.14, "n_sersic": 1.5, "amplitude": 1.3},
        {"type": "sersic_source", "center": (-0.2, -1.2), "R_eff": 0.16, "n_sersic": 0.9, "amplitude": 1.2},

        {"type": "gaussian_circular", "center": (0.25, 0.05), "sigma": 0.05, "amplitude": 2.0},
        {"type": "gaussian_elliptical", "center": (-0.3, 0.1), "sigma_major": 0.12, "sigma_minor": 0.04, "angle": 0.4, "amplitude": 1.8},
        {"type": "sersic_source", "center": (0.1, -0.2), "R_eff": 0.10, "n_sersic": 1.0, "amplitude": 1.5},

        {"type": "gaussian_circular", "center": (1.4, -1.2), "sigma": 0.05, "amplitude": 0.7},
        {"type": "gaussian_circular", "center": (-1.5, 1.2), "sigma": 0.04, "amplitude": 0.6},
        {"type": "gaussian_elliptical", "center": (1.3, 1.3), "sigma_major": 0.10, "sigma_minor": 0.04, "angle": 0.9, "amplitude": 0.8},
        {"type": "sersic_source", "center": (-1.4, -1.3), "R_eff": 0.12, "n_sersic": 1.3, "amplitude": 0.9},
    ]


def get_demo_scene(scene_name):
    
    scenes = {
        "simple": build_simple_source_list,
        "einstein_ring": build_einstein_ring_source,
        "populated": build_populated_source_list
    }

    if scene_name not in scenes:
        raise ValueError(f"Unknown scene selection: {scene_name}")
    
    return scenes[scene_name]()

def list_demo_scenes():
    return["simple","einstein_ring","populated"]