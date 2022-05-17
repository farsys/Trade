
#import v20
from oandapyV20 import API
from oandapyV20 import V20Error
import oandapyV20.endpoints.accounts as accounts
import oandapyV20.endpoints.trades as trades
import oandapyV20.endpoints.pricing as pricing
import json

import colorama

#api=v20.Context(hostname=TRADING_API_URL,port=443,ssl=True,application='', token=TRADING_API_TOKEN,decimal_number_as_float=True,
# stream_chunk_size=512,stream_timeout=30,datetime_format='RFC3339',poll_timeout=1)
#TRADING_API_TOKEN="471fade33f9283e38f9b9c60beb29693-337b3fd8db72ca0cae02acfd18a309ac"

#Constantes
TRADING_API_URL='api-fxtrade.oanda.com'
TRADING_API_PORT=443
TRADING_API_TOKEN="32815b6367fa1a6173ea6a8841dc6364-e13e7d47ce9a3bf0885206468a89a464"
TRADING_API_ACCOUNT='001-001-441603-002'

parameters={'instruments':'EUR_USD'}

api = API(access_token=TRADING_API_TOKEN,environment='live')
prices = pricing.PricingInfo(accountID=TRADING_API_ACCOUNT, params= parameters)

response = api.request(prices)

print(response)


data ="{'instrument': 'EUR_USD', 'granularity': 'H3', 'candles': [{'complete': True, 'volume': 3052, 'time': '2019-10-25T18:00:00.000000000Z', 'mid': [{'o': '1.10770', 'h': '1.10827', 'l': '1.10762', 'c': '1.10798'}]}]}"

data = data.replace("'","\"")
data = data.replace("True","true")
data = data.replace("False","false")
colorama.init()
print(colorama.Fore.LIGHTCYAN_EX+str(data))
jdata = json.loads(data)
print (jdata['candles'])


for a in jdata['candles']:
    print(a)
    for b in a['mid']:
        print(b)