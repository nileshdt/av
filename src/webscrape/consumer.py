import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice

# base_url = "http://quotes.toscrape.com"
base_url = "https://www.banyanbotanicals.com/shop/"
# base_url = "https://www.ayurvedicherbsdirect.com/"

# def scrape_quotes():
all_items = []
url = ""
# url = "/page/1"
# while url:
res = requests.get(f'{base_url}')
print(f"Now scraping {base_url}{url}...")
soup = BeautifulSoup(res.text, "html.parser")
# products = soup.find_all(class_="ais-infinite-hits--item")
products = soup.find_all("div", class_="ais-infinite-hits--item")
# products = soup.find_all("li", class_="product-grid-item")
print(products)
for item in products:
    all_items.append({
        "text": item.find(class_="product-item-description").get_text(),
        "price": item.find(class_="price").get_text(),
        "bio-link": item.find("a")["href"]
    })
    print(all_items)
next_btn = soup.find(class_="next")
# url = next_btn.find("a")["href"] if next_btn else None
# sleep(2)
# return
