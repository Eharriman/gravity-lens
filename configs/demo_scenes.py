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


def get_demo_scene(scene_name):
    
    scenes = {
        "simple": build_simple_source_list,
        "einstein_ring": build_einstein_ring_source
    }

    if scene_name not in scenes:
        raise ValueError(f"Unknown scene selection: {scene_name}")
    
    return scenes[scene_name]()