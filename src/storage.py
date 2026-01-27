import csv
from datetime import datetime

def save_price(url, title, price):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("data/prices.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, url, title, price])
