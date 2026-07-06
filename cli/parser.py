import argparse

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