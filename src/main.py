# main.py
import logging
from utils.file_utils import load_config
from core.agent import run_agent

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

def main():
    setup_logging()
    config = load_config()  # defaults to config/config.yaml

    logging.info("Configuration loaded successfully")
    logging.info("Initializing agent...")

    run_agent(config)

if __name__ == "__main__":
    main()
