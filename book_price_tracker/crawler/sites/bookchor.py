import requests
from bs4 import BeautifulSoup
import urllib.parse
from utils.robots_checker import is_allowed

def crawl_bookchor(book_name):
    base_url = "https://www.bookchor.com"
    search_path = "/search"
    search_url = f"{base_url}{search_path}?search_query={urllib.parse.quote_plus(book_name)}"

    if not is_allowed(base_url, search_path):
        return {
            "title": book_name,
            "price": None,
            "available": False,
            "url": search_url
        }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(search_url, headers=headers, timeout=10)
    if response.status_code != 200:
        return {
            "title": book_name,
            "price": None,
            "available": False,
            "url": search_url
        }

    soup = BeautifulSoup(response.text, "html.parser")
    product = soup.select_one(".product-item")

    if not product:
        return {
            "title": book_name,
            "price": None,
            "available": False,
            "url": search_url
        }

    title_tag = product.select_one(".product-item-info h3 a")
    price_tag = product.select_one(".product-price span")

    if not title_tag or not price_tag:
        return {
            "title": book_name,
            "price": None,
            "available": False,
            "url": search_url
        }

    title = title_tag.text.strip()
    price_text = price_tag.text.strip()
    price = int("".join(filter(str.isdigit, price_text)))

    product_url = title_tag["href"]
    if not product_url.startswith("http"):
        product_url = base_url + product_url

    return {
        "title": title,
        "price": price,
        "available": True,
        "url": product_url
    }
