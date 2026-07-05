from configs.demo_scenes import list_demo_scenes

def print_available_scenes():
    print("Available source-list scenes:")
    for scene in list_demo_scenes():
        print(f" {scene}")
        