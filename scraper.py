from playwright.sync_api import sync_playwright


with sync_playwright() as pw:
    browser = pw.chromium.launch()
    page = browser.new_page()

    page.goto("https://books.toscrape.com")
    page.wait_for_selector(".page_inner")

    books = page.query_selector_all(".product_pod")

    for book in books:
        title = book.query_selector("h3 a").inner_text().strip()
        price = book.query_selector(".product_price .price_color").inner_text()
        stock = bool(book.query_selector(".product_price .instock"))
        image = book.query_selector(".image_container img").get_attribute("src")

        print(f"Book Title: {title}\n Book Price: {price} \n Book Stock: {stock} \n Book Image: {image}")

    browser.close()
