#API Trading talker

#imports
import v20
import pandas as pd
import json
import requests
import colorama
#from socketIO_client import SocketIO
#import socketIO


v20.user.
#Constantes
TRADING_API_URL='https://api-fxtrade.oanda.com'
TRADING_API_PORT=443
#TRADING_API_TOKEN="471fade33f9283e38f9b9c60beb29693-337b3fd8db72ca0cae02acfd18a309ac"
TRADING_API_TOKEN="471fade33f9283e38f9b9c60beb29693-337b3fd8db72ca0cae02acfd18a309ac"

# #Funciones
# def on_connect():
#   #  print('Connection Open!'+ socketio.Client._engineio_client_class())
#   print()

# def on_close():
#   #  print('Connection Close!')
#   print()


#more stuff

#socketio_A= SocketIO()


  # Request headers
headers = { 
    'Content-Type': 'application/json',
    'Authorization': TRADING_API_TOKEN
}

 # Request parameters
parameters_str ={
    'count': '6',
    'price': 'M',
    'granularity': 'S5'
}


address=TRADING_API_URL+'/v3/instruments/EUR_USD/candles?'



response = requests.post(address,headers=headers,params=parameters_str )


# Display the JSON results returned
results = response.json()

print(json.dumps(results))