import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)
response.encoding = "utf-8"
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")
print(len(books))

book = books[0]

title = book.h3.a["title"]
price = book.find("p", class_="price_color").text

print(title)
print(price)