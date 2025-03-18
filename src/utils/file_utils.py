import yaml
import os


def load_config():
    # Get the directory of the current file (file_utils.py)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up two levels to reach the project root (from src/utils -> src -> project root)
    project_root = os.path.dirname(os.path.dirname(current_dir))
    # Construct the path to the config file in the project root
    config_path = os.path.join(project_root, "config", "config.yaml")

    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config


if __name__ == "__main__":
    config = load_config()
    print(config)
