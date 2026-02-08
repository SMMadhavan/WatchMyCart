import csv
from notifier import send_email_alert

# Function Definition
def analyze_prices(target_url):
    prices = []

    with open("data/prices.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["url"] == target_url:
                clean_price = row["price"].replace("Â", "").strip()
                prices.append(float(clean_price))

    if len(prices) < 2:
        print("Not enough data to analyze yet for this product.")
        return

    current = prices[-1]
    average = sum(prices) / len(prices)
    minimum = min(prices)
    maximum = max(prices)

    print("Current price:", current)
    print("Average price:", round(average, 2))
    print("Minimum seen:", minimum)
    print("Maximum seen:", maximum)

    if current <= average * 0.95:
        print("Signal: This is cheaper than usual. Good time to buy.")
    else:
        print("Signal: Price is normal or high.")

def check_alert(target_url, target_price, user_email):
    with open("data/prices.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = [row for row in reader if row["url"] == target_url]

    if not rows:
        return

    latest = rows[-1]
    latest_price = float(latest["price"].replace("Â", "").strip())
    product = latest["product"]

    if latest_price <= target_price:
        print("ALERT: Price reached your target!")
        send_email_alert(user_email, product, latest_price, target_price)
    else:
        print("No alert. Waiting for price drop.")

