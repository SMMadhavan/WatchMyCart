import csv
from collector import get_product_data
from storage import save_price
from analysis import check_alert

WATCHLIST_FILE = "data/watchlist.csv"

#Product Description
def register_product():
    print("\n--- Add Product to Watchlist ---")
    email = input("Enter your email: ")
    url = input("Enter product URL: ")
    min_price = float(input("Enter minimum acceptable price: "))
    max_price = float(input("Enter maximum acceptable price: "))

    with open(WATCHLIST_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([email, url, min_price, max_price])

    print("Product added to watchlist.\n")


def run_checks():
    print("\n--- Running Price Check for Watchlist ---\n")

    with open(WATCHLIST_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            email = row["email"]
            url = row["url"]
            min_price = float(row["min_price"])
            max_price = float(row["max_price"])

            title, price = get_product_data(url)
            save_price(url, title, price)

            print("\nChecked:", title, "Current price:", price)
            check_alert(url, min_price, max_price, email)

    print("\nAll products checked.\n")


def main():
    print("WatchMyCart")
    print("1. Add new product")
    print("2. Run price check")

    choice = input("Choose option: ")

    if choice == "1":
        register_product()
    elif choice == "2":
        run_checks()
    else:
        print("Invalid option")


if __name__ == "__main__":
    main()
