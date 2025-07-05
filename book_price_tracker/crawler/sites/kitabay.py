import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

def crawl_kitabay(book_name):
    search_url = f"https://kitabay.com/search?q={quote(book_name)}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    product = soup.select_one("product-grid-item")

    if not product:
        return {
            "title": book_name,
            "price": None,
            "available": False,
            "url": search_url
        }

    title = product.get("aria-label", book_name).strip()

    a_tag = product.select_one("a[href]")
    url = a_tag["href"] if a_tag else search_url
    if not url.startswith("http"):
        url = "https://kitabay.com" + url
    price = "Note listed"

    available = True

    return {
        "title": title,
        "price": price,
        "available": available,
        "url": url
    }
