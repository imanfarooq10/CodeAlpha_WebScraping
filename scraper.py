import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)
response.encoding = "utf-8"
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")
print(len(books))

all_books = []

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.find("p", class_="star-rating")["class"][1]
    availability = book.find("p", class_="availability").text.strip()

    all_books.append({
        "title": title,
        "price": price,
        "rating": rating,
        "availability": availability,
    })

print(len(all_books))
print(all_books[0])