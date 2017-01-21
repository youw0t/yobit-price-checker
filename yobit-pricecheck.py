import requests
import json


def coin_price(coin):
    url = 'http://yobit.net/api/3/ticker/' + coin + "_btc"
    obj = requests.get(url).text
    data = json.loads(obj)
    try:
        item = data[coin + '_btc']
        final = item['last']
    except:
        final = "Error"
    print(final)


coin_price("trump")
