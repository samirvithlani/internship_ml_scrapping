import requests
from bs4 import BeautifulSoup

base_url = "http://books.toscrape.com/"
response = requests.get(base_url)

#print(response.status_code) #200

soup = BeautifulSoup(response.text,'html.parser')
#print(soup.prettify())
#print(soup.title.string) 

books = soup.find_all('article',class_ ="product_pod")

for book in books:
    title= book.h3.a["title"]
    link = book.h3.a["href"]
    price = book.find('p',class_="price_color").text
    
    print(f"Title: {title} \nLink: {base_url + link}\nPrice: {price}\n")


