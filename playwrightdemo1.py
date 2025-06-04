from playwright.sync_api import sync_playwright,Playwright

def run(playwright : Playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://google.com/")
    page.wait_for_timeout(2000)
    page.screenshot(path="google.png")
    google_textArea = page.query_selector("textarea.gLFyf")
    if google_textArea:
        google_textArea.fill("Netflix")
        #enter
        page.wait_for_timeout(1000)
        google_textArea.press("Enter")
        page.wait_for_timeout(3000)
    else:
        print("Google text area not found.")    
    browser.close()


with sync_playwright() as playwright:
    run(playwright)    
