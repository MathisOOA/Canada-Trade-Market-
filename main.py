import pandas as pd
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries

api_key =('Z8O8EWVEWLEFPD4X')


import csv
import requests


nomAction = "AAPL"
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
#CSV_URL = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=AAPL&interval=15min&slice=year1month1&apikey=" + api_key
CSV_URL = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol="+ nomAction+ "&interval=60min&slice=year1month1&apikey=" + api_key


with requests.Session() as s :
    download = s.get(CSV_URL)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    list1 = []
    list2 = []
    i = 0

    for row in my_list:
        print(row)

        if i%1 == 0 and i!=0 :
            list1.insert(0, row[0])
            list2.insert(0, row[1])
            #list1.append(row[0])
            #list2.append(row[1])
        i += 1
    lines = plt.plot(list1, list2)
    plt.setp(lines, color='r', linewidth=2.0)
    #plt.xlim(0,1) ########## pour mettre les limite (entre deux valeurs)
    plt.ylabel('Prix ($)')
    plt.xlabel('date')
    plt.show()
