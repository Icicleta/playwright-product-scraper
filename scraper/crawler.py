from playwright.sync_api import sync_playwright

def get_page_content(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto(url)

        html = page.content()

        browser.close()

        return html


