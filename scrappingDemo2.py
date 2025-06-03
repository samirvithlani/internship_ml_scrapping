import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = "http://books.toscrape.com/"
next_page = "/catalogue/page-2.html"  # Start with the first page



while next_page:
    url = urljoin(base_url, next_page)
    print("Fetching:", url)
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')    
    
    books = soup.find_all('article', class_="product_pod")
    for book in books:
        title = book.h3.a["title"]
        link = book.h3.a["href"]
        price = book.find('p', class_="price_color").text
        
        print(f"Title: {title} \nLink: {base_url + link}\nPrice: {price}\n")
    
    next_button = soup.find('li',class_="next") 
    print("next_button.....................", next_button)   #pag3
    if next_button:
        next_page = next_button.a["href"] #pag3.html
        next_page = "/catalogue/"+next_page.strip()
        print("next_page.....",next_page)
    else:
        print("No more pages to scrape.")
        next_page = None    