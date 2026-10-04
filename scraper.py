import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

all_books = []

for page in range(1, 51):
    page_url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(page_url)
    response.encoding = "utf-8"

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

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

    print(f"Page {page} done, total books so far: {len(all_books)}")
    time.sleep(0.5)
df = pd.DataFrame(all_books)
df.to_csv("books_data.csv", index=False, encoding="utf-8-sig")

print(df.shape)
print(df.head())