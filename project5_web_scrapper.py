import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/page/2/"

response = requests.get(url)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

quotes = soup.find_all(
    "span",
    class_="text"
)

print("\nQuotes from the Website:\n")

for index, quote in enumerate(quotes, start=1):

    print(f"{index}. {quote.text}")