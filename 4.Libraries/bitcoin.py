import sys
import requests


API_KEY = "YOUR_API_KEY"


if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    price = float(data["data"]["priceUsd"])
except requests.RequestException:
    sys.exit("Request failed")

total = bitcoins * price

print(f"${total:,.4f}")

