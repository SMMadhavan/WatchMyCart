import requests
from bs4 import BeautifulSoup

def get_product_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("h1").text
    price = soup.find("p", class_="price_color").text

    # Clean weird characters and ambiguity
    price = price.replace("£", "").replace("Â", "").strip()

    return title, price
