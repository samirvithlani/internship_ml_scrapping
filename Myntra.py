from playwright.sync_api import sync_playwright,Playwright

with sync_playwright() as p:
    chromium = p.chromium
    browser = chromium.launch(headless=False)
    page  = browser.new_page()
    page.goto("https://www.myntra.com/men-tshirts")
    page.wait_for_timeout(2000)
    page.screenshot(path="myntra.png")
    
    products = page.query_selector_all("li.product-base")
    if products:
        for product in products:
            product_meta = product.query_selector("div.product-productMetaInfo")
            if product_meta:
                product_brand = product_meta.query_selector("h3.product-brand")
                print(f"Brand  = {product_brand.inner_text()}")
                product_name = product_meta.query_selector("h4.product-product")
                if product_name:
                    print(f"Name   = {product_name.inner_text()}")
                else:
                    print("Product name not found.")
                product_price_contaier = product_meta.query_selector("div.product-price") #div
                if product_price_contaier:
                    discounted_price = product_price_contaier.query_selector("span.product-discountedPrice")
                    if discounted_price:
                        print(f"Discounted Price = {discounted_price.inner_text()}")    
                