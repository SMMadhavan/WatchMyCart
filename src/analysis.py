import csv

def analyze_prices():
    prices = []

    with open("data/prices.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            prices.append(float(row["price"]))

    if len(prices) < 2:
        print("Not enough data to analyze yet.")
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
