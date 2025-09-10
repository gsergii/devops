from flask import Flask, render_template, request
import requests

# URL free API for exchange rates
# we are using free API from ExchangeRate-API.
# you dont need API-key for base usage.
API_URL = "https://open.er-api.com/v6/latest/USD"

app = Flask(__name__)

def get_exchange_rates():
    """
    get exchange rates from API.
    """
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # we will have an error, in case of unsuccessfull call
        data = response.json()
        return data.get("rates", {})
    except requests.exceptions.RequestException as e:
        print(f"Error while getting data: {e}")
        return None

def convert_currency(rates, amount, from_currency, to_currency):
    """
    to convert from one currency to another.
    """
    # if currency the same we wil return the amount
    if from_currency == to_currency:
        return amount

    # check if exchange rate exist for both currencies 
    if from_currency not in rates or to_currency not in rates:
        print("Error: wrong currency code.")
        return None

    # convert initial amount to base currency (USD)
    amount_in_usd = amount / rates[from_currency]

    # convert from USD to desired currency
    converted_amount = amount_in_usd * rates[to_currency]

    return converted_amount

# web interface
@app.route("/", methods=["GET", "POST"])
def index():
    rates = get_exchange_rates()
    result = None

    if request.method == "POST":
        try:
            from_currency = request.form["from_currency"].upper()
            to_currency = request.form["to_currency"].upper()
            amount = float(request.form["amount"])

            converted_amount = convert_currency(rates, amount, from_currency, to_currency)

            if converted_amount is not None:
                result = f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}"
            else:
                result = "Error: wrong currency code."

        except ValueError:
            result = "Error: enter valid amount."

    return render_template("index.html", rates=rates, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
