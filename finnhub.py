
import requests
from datetime import datetime, time
import numpy

##
##r = requests.get('https://finnhub.io/api/v1/forex/exchange?token=brgf0fvrh5r8gtvep6ng')
##print(r.json())

##r = requests.get('https://finnhub.io/api/v1/forex/symbol?exchange=ic markets&token=brgf0fvrh5r8gtvep6ng')
##print(r.json())


fromdate = str(datetime.timestamp(datetime.mktime(2020,6,1))).split(".",1)[0]
todate = str(datetime.now().timestamp()).split(".",1)[0]

print(fromdate)

#r = requests.get('https://finnhub.io/api/v1/forex/candle?symbol=IC MARKETS:2&resolution=D&from='+fromdate+'&to='+todate+'&token=brgf0fvrh5r8gtvep6ng')
#print(r.json())
