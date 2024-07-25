import os
import requests as req
import datetime as dt
import time

api_key = os.environ.get("API_KEY_CRYPTO")
base_url = "https://api.nomics.com/v1/"
currencies = ['BTC', 'ETH', 'BNB', 'ADA', 'DOGE', 'XRP', 'USDT', 'DOT', 'ICP', 'HEX', 'LTC', 'LINK',
              'VET', 'MATIC', 'XMR', 'AAVE', 'NEO', 'SHIB', 'TRX', 'LUNA', 'BCH']

intervals = ['1d']

api_prefix = "http://localhost:5000/"

SUPPLY_INTERVAL = 60   # requesting new data every 5 seconds


def get_currencies():
    currency = ','
    interval = ','
    url = base_url + f"currencies/ticker?key={api_key}" \
                     f"&ids={currency.join(currencies)}" \
                     f"&interval={interval.join(intervals)}"
    curr = req.get(url)
    return curr


def send_data():
    crs = get_currencies().json()
    dt_now = dt.datetime.now()

    print(f'[{dt.datetime.strftime(dt_now, "%Y-%m-%d %H:%M:%S")} SUPPLIER] '
          f'Sending data of {len(crs)} cryptocurrencies with', end=' ')
    url = api_prefix + 'CryptoCurrency/add_list_of_currencies'
    data = {
        "meta": {
            "method": "add_list_of_currencies",
            "args": {
                "crypto_data": crs
            }
        }
    }
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    response = req.post(url, json=data, headers=headers)
    print(response)


if __name__ == '__main__':
    while True:
        send_data()
        time.sleep(SUPPLY_INTERVAL)
