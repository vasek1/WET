from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

load_dotenv()
hoj = "ok"
def main():
     with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("http://127.0.0.1:5000/form")
        
        page.fill('input[id="name"]',hoj)
        page.fill('input[id="class"]',hoj)
        page.fill('textarea[id="message"]',hoj)
        page.wait_for_timeout(2000)
        page.click('button[id="button"]')
    
        input("vypni")
        browser.close()
if __name__ == "__main__":
    main()