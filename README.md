# Book Price Tracker

A Python-based modular web crawler that checks book prices from multiple Indian online bookstores and outputs a structured JSON report of price, availability, and URLs.

---

## Features

- Scrapes from popular Indian book retailers:
  - Flipkart
  - Bookswagon
  - Kitabay
  - Bookchor
  - 99Bookstore
- Daily price tracking saved to `data/YYYY-MM-DD/prices.json`
- Modular crawler for easy extension to new websites
- Gracefully handles unavailable books
- Random user-agent rotation

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/book-price-tracker.git
cd book-price-tracker

```

### 2. Install the dependencies

```bash
pip install -r requirements.txt

```

### 3. Run

```bash
python main.py

```

Also you can change the book list in books.txt to get your desired results!

Happy Hacking!!


