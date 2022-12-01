from oandapyV20 import API
from oandapyV20 import V20Error
import oandapyV20.endpoints.accounts as accounts
import oandapyV20.endpoints.instruments as instruments
import csv
import json
import pandas as pd
import colorama
#import pyti as _ti 
import ta as ta 
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
#Constantes
#%matplotlib inline
TRADING_API_TOKEN=""
TRADING_API_ACCOUNT=''
CANDLES=5000


SYMBOL='EUR_JPY'
#EUR_USD

parameters={"count": CANDLES,#how many registers i want
            "granularity": "H4",# time frame
            }

#long is buy
#short is sell

api = API(access_token=TRADING_API_TOKEN,environment='live')
data = instruments.InstrumentsCandles(SYMBOL,params= parameters)

response = api.request(data)

colorama.init()
print(colorama.Fore.YELLOW+'='*200)
#response = str(response).replace("'","\"")



#back yo json

response= str(response).replace("'","\"").replace("True","true").replace("False","false").replace("}}","}]}").replace(": {",": [{")

#print(colorama.Fore.LIGHTCYAN_EX+response)


print(colorama.Fore.YELLOW+'='*200)
print(colorama.Fore.RESET)




dresponse = json.loads(response)



print(colorama.Fore.LIGHTYELLOW_EX)
#print(dataframe)

print(colorama.Fore.LIGHTGREEN_EX)

#print(dresponse)


dataframe = pd.DataFrame.from_dict(dresponse['candles'])

res ={}
count =0
direction ={}
for a in dresponse['candles']:
    #print (a)
    for b in a['mid']:
        del a['mid']
        b['o']=float(b['o'])
        b['c']=float (b['c'])
        b['l']=float(b['l'])
        b['h']=float (b['h'])


        _open=b['o']
        _close=b['c']

        if _open >=_close :
            direction={'Up':'True'}
      
        else:
            direction={'Up':'False'}
      
        percent_charged =((_close - _open ) /  _close)*100
       # bbUpper = {'BB_Upper':ta.bollinger_hband(_close)}

        pip={'PIP':((_close-_open)*10000)*50}
   
        percent_charged={'percent_changed':percent_charged}
   
        res[count]={**a,**b,**direction,**pip,**percent_charged}
        count=count+1
        

print(colorama.Fore.LIGHTYELLOW_EX)
#print(dataframe)
#print(res)

data = pd.DataFrame.from_dict(res,orient='index')

# data['h'] = pd.to_numeric(data['h'])
# data['l'] = pd.to_numeric(data['l'])
# data['o'] = pd.to_numeric(data['o'])
# data['c'] = pd.to_numeric(data['c'])


#data.columns=columns=['Complete','Volume','Time','Open','Hight','Low','Close','Up','percent_changed','BB_upper','BB_Lower','BB_MA']

#####BOLLINGER BANDS
data['BB_upper'] = ta.bollinger_hband(data['c'])
data['BB_Lower'] = ta.bollinger_lband(data['c'])
data['BB_MA'] = ta.bollinger_mavg(data['c'])
data['BB_isNarrowing'] = np.where((data['BB_upper'] <= data['BB_upper'].shift()) & (data['BB_Lower'] > data['BB_Lower'].shift()),True,False)

#####RSI
data['RSI'] = ta.rsi(data['c'])


#####Moving Averages
data['MA_Fast'] = ta.ema_indicator(close=data['c'],n=20)
data['MA_Slow'] = ta.ema_indicator(close=data['c'],n=50)
data['MA_UP'] = np.where(data['MA_Fast'] >= data['MA_Slow'],True, False)

data['MA_200'] = ta.ema_indicator(close=data['c'],n=200)

data['MA_200UP'] = np.where(data['c'] >= data['MA_200'],True, False)

#####AVERAGE TRUE RANGE
data['ATR'] = ta.average_true_range(data['h'],data['l'],data['c'],n=20)

#####Moving average convengence
data['MACD_sinal'] = ta.macd_signal(data['c'])
data['MACD_diff'] = ta.macd_diff(data['c'])
data['MACD_line'] = ta.macd(data['c'])

###date split
data['time'] = pd.to_datetime( data['time'])
data['Month'] = pd.DatetimeIndex(  data['time']).month
data['Day'] = pd.DatetimeIndex(  data['time']).day
data['Hour'] = pd.DatetimeIndex(  data['time']).hour
data['dayofweek'] = pd.DatetimeIndex(  data['time']).dayofweek
#data['Frame'] 

data['isVolumeRaising'] = np.where(data['volume'] >= data['volume'].shift(),True,False)


data.columns=columns=['Complete','Volume','Time','Open','High','Low','Close','Up','PIP','percent_changed',
'BB_upper','BB_Lower','BB_MA','BB_isNarrowing',
'RSI',
'MA_Fast','MA_Slow','MA_UP','MA_200','MA_200UP',
'ATR',
'MACD_sinal','MACD_diff','MACD_line',
'Month','Day','Hour','dayofweek','isVolumeRaising']


print(data)
data.to_csv("./data.csv")

# data[['Close','BB_upper','BB_Lower','BB_MA']].plot()
# data[['Close','MA_Fast','MA_Slow',]].plot()
# data[['Close','MA_200',]].plot()

plt.show()

#fig =plt.Figure(12,8)











def _fileWriter(tofile):

   file_path = "./data.csv"
   try:
       file_data = open(file=file_path, mode='w')
     # csv_writer = csv.writer(file_data)
       file_data.write(tofile)
       file_data.close()
   except Exception as e:
       print(e.__str__()) 
