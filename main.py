from scraper.crawler import crawl_books
from scraper.parser import parse_books
from scraper.exporter import export_to_csv

if __name__ == "__main__":
    url = "http://books.toscrape.com/"
    html = crawl_books(url)
    books = parse_books(html)
    export_to_csv(books, "books.csv")

print(f"Scraped {len(books)} books")
