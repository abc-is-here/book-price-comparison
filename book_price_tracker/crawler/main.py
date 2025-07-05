import os
import json
from datetime import datetime
from utils.logger import set_logger
from crawler.aggregator import crawl_all_sites


def crawl():
    logger = set_logger()
    today = datetime.now().strftime("%Y-%m-%d")
    output_dir = os.path.join("data", today)
    os.makedirs(output_dir, exist_ok=True)

    logger.info("My hands are sticky, I need to crawl some data!")

    books_path = os.path.join(os.path.dirname(__file__), "..", "books.txt")

    with open(books_path, 'r') as books_data:
        books = [line.strip() for line in books_data if line.strip()]
    
    all_data = {}

    for book in books:
        logger.info(f"crawlong on {book}")
        try:
            data = crawl_all_sites(book)
            if data:
                all_data[book] = data
                logger.info(f"Crawled the {book} successfully.")
            else:
                logger.warning(f"I fell because {book} was slippery.")
        except Exception as e:
            logger.error(f"Error while crawling {book}: {e}")
    
    output_dir = os.path.join(output_dir, "prices.json")
    with open(output_dir, 'w') as output_file:
        json.dump(all_data, output_file, indent=2)

    logger.info(f"Book crawling completed. Output saved to {output_dir}")