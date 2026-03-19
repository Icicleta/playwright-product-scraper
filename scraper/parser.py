from bs4 import BeautifulStoneSoup


def parse_books(html):

    soup = BeautifulStoneSoup(html, features="lxml")

    books = []

    for book in soup.select('.product_pod'):
        title = book.select_one("h3 a")["title"]
        price = book.select_one(".price_color").text
        stock = book.select_one(".availability").text.strip()

        books.append({
            'title': title,
            'price': price,
            'stock': stock.strip()
        })

    return books
