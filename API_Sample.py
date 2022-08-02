# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 11:02:59 2021

@author: akhil
"""

from ks_api_client import ks_api
import pandas as pd
from authorize import login
from tvDatafeed import TvDatafeed, Interval
import sys
import datetime as dt
import funds_kotak

tv = TvDatafeed(auto_login=(True))

acc = float(tv.get_hist('IDEA', 'NSE', Interval.in_5_minute).loc[dt.time(9,5)]['open'])

dat = tv.get_hist('RELIANCE', 'NSE', Interval.in_5_minute)

client = login.author('Allwyn')
funds = funds_kotak.get_funds(client, 'Allwyn')
sess = client.session_2fa(access_code = "9032")

price1 = float(client.quote(instrument_token = 41509)['success'][0]['ltp'])
price2 = float(client.quote(instrument_token = 1909)['success'][0]['ltp'])
client.place_order(order_type = "MIS", instrument_token = 8658, transaction_type = "SELL",\
                            quantity = 1, price = 0, disclosed_quantity = 0, trigger_price = 0,\
                                validity = "GFD", variety = "REGULAR", tag = "string")

client.place_order(order_type = "MIS", instrument_token = 3886, transaction_type = "SELL",\
                            quantity = 1, price = 0, disclosed_quantity = 0, trigger_price = 0,\
                                validity = "GFD", variety = "REGULAR", tag = "string")
    
pos = client.positions(position_type='OPEN')
openp = client.positions(position_type='OPEN')
fund_each = funds/2

qty1 = int(fund_each/(price1/5))
qty2 = int(fund_each/(price2/5))

    
    
    
    
    
    

 
ltp = round(1.02*float(client.quote(instrument_token = 3886)['success'][0]['ltp']),1)

b = client.place_order(order_type = "MIS", instrument_token = 8658, transaction_type = "BUY",\
                            quantity = 1, price = ltp, disclosed_quantity = 0, trigger_price = ltp,\
                                validity = "GFD", variety = "SQUAREOFF", tag = "string", product='SUPERMULTIPLE')
    
idexit = client.place_order(order_type = "MIS", instrument_token = 8658, transaction_type = "BUY",\
                            quantity = 1, price = 0, disclosed_quantity = 0, trigger_price = 0,\
                                validity = "GFD", variety = "SQUAREOFF", tag = "string", product='SUPERMULTIPLE')
    

union_short = client.place_order(order_type = "MIS", instrument_token = 3898, transaction_type = "SELL",\
                            quantity = 1, price = 0, disclosed_quantity = 0, trigger_price = ltp,\
                                validity = "GFD", variety = "SQUAREOFF", tag = "string", product='SUPERMULTIPLE')

unionsl = client.place_order(order_type = "MIS", instrument_token = 3898, transaction_type = "BUY",\
                            quantity = 1, price = ltp, disclosed_quantity = 0, trigger_price = 0,\
                                validity = "GFD", variety = "SQUAREOFF", tag = "string", product='SUPERMULTIPLE')
    

orders = client.order_report()
orders_sl = client.order_report()
ord_id=[]

for i in range(len(orders['success'])):
    if orders_sl['success'][i]['status'] == 'SLO':
        ord_id.append(orders_sl['success'][i]['orderId'])
        
for j in range(len(ord_id)):
    print(j)
    try:
        client.cancel_order(order_id=ord_id[j])
        print('Cancelled')
    except:
        print('Not able to cancel')
        continue


