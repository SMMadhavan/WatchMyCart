from fastapi import FastAPI
from pydantic import BaseModel
import csv
from collector import get_product_data
from storage import save_price
from analysis import check_alert

app = FastAPI()

WATCHLIST_FILE = "data/watchlist.csv"

class TrackRequest(BaseModel):
    email: str
    url: str
    min_price: float
    max_price: float


@app.post("/add")
def add_product(req: TrackRequest):
    with open(WATCHLIST_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([req.email, req.url, req.min_price, req.max_price])

    title, price = get_product_data(req.url)
    save_price(req.url, title, price)

    return {
        "status": "tracking started",
        "product": title,
        "current_price": price
    }


@app.post("/run")
def run_checks():
    alerts = []

    with open(WATCHLIST_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            email = row["email"]
            url = row["url"]
            min_price = float(row["min_price"])
            max_price = float(row["max_price"])

            title, price = get_product_data(url)
            save_price(url, title, price)

            triggered = check_alert(url, min_price, max_price, email)
            if triggered:
                alerts.append(title)

    return {"alerts_triggered": alerts}
