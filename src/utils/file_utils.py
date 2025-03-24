import os
import yaml


def load_config():
    # Get the directory of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(current_dir))
    config_path = os.path.join(project_root, "config", "config.yaml")

    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    # Override API key with environment variable if present
    env_api_key = os.environ.get("OPENAI_API_KEY")
    if env_api_key:
        config["openai"]["api_key"] = env_api_key
    return config
