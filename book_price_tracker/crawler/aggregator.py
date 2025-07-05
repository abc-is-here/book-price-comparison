from crawler.sites.flipkart import crawl_flipkart
from crawler.sites.bookchor import crawl_bookchor
from crawler.sites.bookswagon import crawl_bookswagon
from crawler.sites.kitabay import crawl_kitabay
from crawler.sites.bookstore99 import crawl_99bookstore

def crawl_all_sites(book):
    return{
        "flipkart": crawl_flipkart(book),
        "bookchor": crawl_bookchor(book),
        "bookswagon": crawl_bookswagon(book),
        "kitabay": crawl_kitabay(book),
        "99bookstore": crawl_99bookstore(book),
    }