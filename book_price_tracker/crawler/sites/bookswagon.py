import requests
from bs4 import BeautifulSoup
import urllib.parse
from utils.robots_checker import is_allowed

def crawl_bookswagon(book_name):
    base_url = "https://www.bookswagon.com"
    search_path = f"/search-books/{urllib.parse.quote_plus(book_name)}"
    search_url = base_url + search_path

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

    try:
        response = requests.get(search_url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        return {
            "title": book_name,
            "price": None,
            "available": False,
            "url": search_url
        }

    soup = BeautifulSoup(response.content, "html.parser")
    first_result = soup.select_one(".list-view-books")

    if not first_result:
        return {
            "title": book_name,
            "price": None,
            "available": False,
            "url": search_url
        }

    title_tag = first_result.select_one(".title a")
    title = title_tag.text.strip() if title_tag else book_name

    price_tag = first_result.select_one(".price .sell")
    if price_tag:
        price_text = price_tag.text.strip().replace("₹", "").replace(",", "")
        price = int("".join(filter(str.isdigit, price_text))) if price_text else None
    else:
        price = None

    availability_tag = first_result.select_one(".available-stock")
    available = bool(availability_tag and "Available" in availability_tag.text)

    url = title_tag['href'] if title_tag and 'href' in title_tag.attrs else search_url
    if not url.startswith("http"):
        url = urllib.parse.urljoin(base_url, url)

    return {
        "title": title,
        "price": price,
        "available": available,
        "url": url
    }
