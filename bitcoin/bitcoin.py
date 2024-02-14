import requests
import json
import sys
if len(sys.argv) !=2:
    print("Missing command-line argument")
    # sys.exit()
try:
    no_of_bitcoin = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    # sys.exit()
except requests.RequestException:
    sys.exit()
r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
r=r.json()
# print(r.keys())
rate=float(r["bpi"]["USD"]["rate_float"])
output = rate*no_of_bitcoin
print(f"${output:,.4f}")