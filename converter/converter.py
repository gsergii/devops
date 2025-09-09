import requests

# URL free API for exchange rates
# we are using free API from ExchangeRate-API.
# you dont need API-key for base usage.
API_URL = "https://open.er-api.com/v6/latest/USD"

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

def main():
    """
    Main function.
    """
    print("Welcome to the simple converter")
    print("Available currency codes for usage: USD, EUR, UAH, JPY, GBP, ...")

    rates = get_exchange_rates()
    if not rates:
        return

    while True:
        try:
            from_currency = input("Enter your (from) currency (ex, USD): ").upper()
            to_currency = input("Enter desired (to) currency (ex, EUR): ").upper()
            amount = float(input("Amount: "))

            result = convert_currency(rates, amount, from_currency, to_currency)

            if result is not None:
                print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
                
            break # to get out after successfull converting

        except ValueError:
            print("Error: enter valid amount.")
            continue_prompt = input("Try again? (yes/no): ").lower()
            if continue_prompt != 'yes':
                break

if __name__ == "__main__":
    main()