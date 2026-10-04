# Books Web Scraper

## Overview
This project scrapes book data from books.toscrape.com, a practice website built for learning web scraping. It uses Python with requests and BeautifulSoup to visit all 50 catalogue pages and collect 1,000 books. The data is cleaned with pandas and saved as a CSV file.

## Dataset (books_data.csv)
| Column | Description |
|---|---|
| title | Full title of the book |
| price | Price in GBP (number) |
| rating | Star rating from 1 to 5 (number) |
| availability | Stock status |

## Tools Used
- Python
- requests
- BeautifulSoup (bs4)
- pandas

## How to Run
```
pip install requests beautifulsoup4 pandas
python scraper.py
```

## How It Works
1. Loops through pages 1 to 50 of the catalogue.
2. Downloads each page and finds every book on it.
3. Extracts the title, price, rating and availability.
4. Cleans the price and rating columns into numbers.
5. Saves everything to books_data.csv.

The script pauses half a second between pages to avoid overloading the website.