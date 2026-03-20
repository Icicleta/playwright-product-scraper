from playwright.sync_api import sync_playwright

def crawl_books(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto(url)

        html = page.content()

        browser.close()

        return html
