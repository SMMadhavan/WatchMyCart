from collector import get_product_data
from storage import save_price
from analysis import analyze_prices

# Prompting Product URL
url = input("Enter product URL: ")

title, price = get_product_data(url)
save_price(title, price)

print("Recorded:", title, price)

analyze_prices()
