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
from ta.utils import dropna
from ta.volatility import BollingerBands

import matplotlib.pyplot as plt
#Constantes
#%matplotlib inline
TRADING_API_TOKEN="token"
TRADING_API_ACCOUNT='account'


parameters={"count": 100,#how many registers i want
            "granularity": "H4",# time frame
            }



api = API(access_token=TRADING_API_TOKEN,environment='live')
data = instruments.InstrumentsCandles('EUR_USD',params= parameters)

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

        if _open >_close :
            direction={'Up':'False'}
        elif  _open ==_close :
             direction={'Up':'Null'}
        else:
            direction={'Up':'True'}
      
        percent_charged =((_close - _open ) /  _close)*100
       # bbUpper = {'BB_Upper':ta.bollinger_hband(_close)}

        percent_charged={'percent_changed':percent_charged}
   
        res[count]={**a,**b,**direction,**percent_charged}
        count=count+1
        

print(colorama.Fore.LIGHTYELLOW_EX)
#print(dataframe)
#print(res)

data = pd.DataFrame.from_dict(res,orient='index')
data= dropna(data)
# data['h'] = pd.to_numeric(data['h'])
# data['l'] = pd.to_numeric(data['l'])
# data['o'] = pd.to_numeric(data['o'])
# data['c'] = pd.to_numeric(data['c'])


#data.columns=columns=['Complete','Volume','Time','Open','Hight','Low','Close','Up','percent_changed','BB_upper','BB_Lower','BB_MA']
bb=BollingerBands(close=data['c'], window=20, window_dev=2)
data['BB_upper'] = bb.bollinger_hband()
data['BB_Lower'] = bb.bollinger_lband()
data['BB_MA'] = bb.bollinger_mavg()

data.columns=columns=['Complete','Volume','Time','Open','High','Low','Close','Up','percent_changed','BB_upper','BB_Lower','BB_MA']

print(data)

data[['Close','BB_upper','BB_Lower','BB_MA']].plot()
#fig =plt.Figure(12,8)


data.to_csv("./test.csv")









def _fileWriter(tofile):

   file_path = "./test.csv"
   try:
       file_data = open(file=file_path, mode='w')
     # csv_writer = csv.writer(file_data)
       file_data.write(tofile)
       file_data.close()
   except Exception as e:
       print(e.__str__()) 