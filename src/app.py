from flask import Flask, request, render_template
from collector import get_product_data
from storage import save_price
from analysis import analyze_prices, check_alert

#Flask Integration for Backend
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        target = float(request.form["target"])
        email = request.form["email"]

        title, price = get_product_data(url)
        save_price(url, title, price)
        analyze_prices(url)
        check_alert(url, target, email)

        return "Tracking started for " + title

    return render_template("index.html")

app.run(debug=True)
