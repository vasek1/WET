from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

load_dotenv()
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")
def main():
     with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://www.moodle-trebesin.cz")

        page.click('span[class="login pl-2"]')

        page.fill('input[id="username"]',login)
        page.fill('input[id="password"]',password)
        page.click('button[id="loginbtn"]')
        
        stranka = page.locator('span[class ="multiline"]')
        print(stranka)

        input("vypni")
        browser.close()
if __name__ == "__main__":
    main()