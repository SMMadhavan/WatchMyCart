from collector import get_product_data
from storage import save_price
from analysis import analyze_prices, check_alert

url = input("Enter product URL: ")
target = float(input("Enter your target price: "))

title, price = get_product_data(url)
save_price(url, title, price)

print("Recorded:", title, price)

analyze_prices(url)
check_alert(url, target)
