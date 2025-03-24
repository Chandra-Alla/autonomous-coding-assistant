import os
import yaml

DEFAULT_CONFIG_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    "..",
    "config",
    "config.yaml"
)

def load_config(config_path: str = DEFAULT_CONFIG_PATH) -> dict:
    """
    Load the YAML configuration file and return it as a dictionary.
    :param config_path: The path to the YAML config file.
    :return: Dictionary containing configuration data.
    """
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config
