import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus, urljoin
from utils.config import get_head
from utils.robots_checker import is_allowed

def crawl_flipkart(book_name):
    base_url = "https://www.flipkart.com"
    search_path = f"/search?q={quote_plus(book_name)}"
    search_url = base_url + search_path

    if not is_allowed(base_url, search_path):
        return {
            "title": book_name,
            "price": None,
            "available": False,
            "url": search_url
        }

    try:
        response = requests.get(search_url, headers=get_head(), timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        return {
            "title": book_name,
            "price": None,
            "available": False,
            "url": search_url
        }

    soup = BeautifulSoup(response.text, "html.parser")

    product_containers = soup.select("div.slAVV4") or soup.select("div._1AtVbE")

    for container in product_containers:
        title_el = container.select_one("a.wjcEIp") or container.select_one("a._1fQZEK")
        price_el = container.select_one("div.Nx9bqj") or container.select_one("div._30jeq3")

        if title_el and price_el:
            title = title_el.get("title") or title_el.text.strip()
            link = urljoin(base_url, title_el["href"])

            try:
                price_text = price_el.text.replace("₹", "").replace(",", "").strip()
                price = int("".join(filter(str.isdigit, price_text)))
            except ValueError:
                continue

            return {
                "title": title,
                "price": price,
                "available": True,
                "url": link
            }

    return {
        "title": book_name,
        "price": None,
        "available": False,
        "url": search_url
    }
