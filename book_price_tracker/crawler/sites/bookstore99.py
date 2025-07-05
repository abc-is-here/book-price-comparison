import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

def crawl_99bookstore(book_name):
    search_query = quote_plus(book_name)
    search_url = f"https://99bookstores.com/search?q={search_query}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(search_url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    link_tag = soup.select_one("a.product__title")
    if not link_tag:
        return {
            "title": book_name,
            "price": None,
            "available": False,
            "url": search_url
        }

    product_url = link_tag["href"]
    if not product_url.startswith("http"):
        product_url = "https://99bookstores.com" + product_url

    product_res = requests.get(product_url, headers=headers)
    product_res.raise_for_status()
    product_soup = BeautifulSoup(product_res.text, "html.parser")

    title_tag = product_soup.select_one("div.product__title h1") or product_soup.select_one("div.product__title h2")
    title = title_tag.text.strip() if title_tag else book_name

    price_tag = product_soup.select_one("span.product__price")
    if price_tag:
        price_text = price_tag.text.strip().replace("₹", "").replace(",", "")
        try:
            price = int("".join(filter(str.isdigit, price_text)))
        except ValueError:
            price = None
    else:
        price = None

    return {
        "title": title,
        "price": price,
        "available": price is not None,
        "url": product_url
    }
