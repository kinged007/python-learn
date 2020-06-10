
import requests
from datetime import datetime, date
from time import mktime
import numpy
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


##
##r = requests.get('https://finnhub.io/api/v1/forex/exchange?token=brgf0fvrh5r8gtvep6ng')
##print(r.json())

#r = requests.get('https://finnhub.io/api/v1/forex/symbol?exchange=ic markets&token=brgf0fvrh5r8gtvep6ng')
#print(r.json())

date = "2019-06-01" # format: "%Y-%m-%d"

fromdate = str(datetime.strptime(date,"%Y-%m-%d").timestamp()).split(".",1)[0]
todate = str(datetime.now().timestamp()).split(".",1)[0]

#r = requests.get('https://finnhub.io/api/v1/forex/candle?symbol=IC MARKETS:2&resolution=D&from='+fromdate+'&to='+todate+'&token=brgf0fvrh5r8gtvep6ng')
#print(r.json())

#r = requests.get('https://finnhub.io/api/v1/scan/pattern?symbol=IC MARKETS:2&resolution=D&token=brgf0fvrh5r8gtvep6ng')

#r = requests.get('https://finnhub.io/api/v1/scan/support-resistance?symbol=IC MARKETS:2&resolution=D&token=brgf0fvrh5r8gtvep6ng')

#r = requests.get('https://finnhub.io/api/v1/scan/technical-indicator?symbol=IC MARKETS:2&resolution=D&token=brgf0fvrh5r8gtvep6ng')

r = requests.get('https://finnhub.io/api/v1/indicator?symbol=IC MARKETS:2&resolution=D&from=1583098857&to=1584308457&indicator=sma&timeperiod=3&token=brgf0fvrh5r8gtvep6ng')


#print(r.json())



style.use('ggplot')

#df = pd.read_csv("tsla.csv", parse_dates = True, index_col = 0)
data = r.json()


df = pd.DataFrame(data, index=data['t'])

df.drop(columns='s', inplace=True, errors="raise")
df.drop(columns='t', inplace=True, errors="raise")
#df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
df.dropna(inplace=True)

print( df.head())

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

ax1.plot(df.index, df['c'])
ax1.plot(df.index, df['sma'])
ax2.bar(df.index, df['v'])
# df.plot()
plt.show()