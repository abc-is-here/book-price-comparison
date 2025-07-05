import logging
from datetime import datetime
import os

def set_logger():
    today = datetime.now().strftime("%Y-%m-%d")
    log_dir = os.path.join("logs", f"{today}.log")
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_dir),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger("Bokk Finder")
