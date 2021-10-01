#!/usr/bin/env python
# coding: utf-8

# In[14]:


import requests, json, itertools
import pandas as pd
import datetime as dt
from datetime import datetime,timedelta
from threading import Timer
import schedule
import time
from datetime import date
from pandas.io.json import json_normalize
import re
import numpy as np


api_token = 'XXXXXXXXXXXXXXXXXXXXXXXX'

api_url_base = 'https://api.flexport.com/ocean/shipment_containers'

headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}

# response = requests.get(api_url_base, headers=headers)

# container = response.json()
def container_script(container):
    
    container_info = container['data']

    container_info = container_info['data']

    df_items = pd.json_normalize(container_info, 'items',['container_number'], errors='ignore')


    df_container = pd.json_normalize(container_info, errors = 'ignore')



    result = pd.merge(df_items, df_container, on="container_number")





    #result.drop(result.columns[[0, 6,9,10,19,20,21,22,24,29,41,42,43,50,49,48,46,45,44]], axis = 1, inplace = True, errors = 'ignore')

    result.rename(columns = {'id_x':'ITEM_ID', 'total_units':'ITEM_TOTAL_UNITS', 
                             'purchase_order_number':'ITEM_PURCHASE_ORDER',
                             'total_weight.value':'ITEM_WEIGHT_VALUE',
                             'total_weight.unit':'ITEM_WEIGHT_UNIT',
                             'total_volume.unit':'ITEM_VOLUME_UNIT',
                             'total_volume.value':'ITEM_VOLUME_VALUE',
                             'product.id':'ITEM_PRODUCT_ID',
                             'product.sku':'ITEM_PRODUCT_SKU',
                             'product.name':'ITEM_PRODUCT_NAME',
                             'product.description':'ITEM_PRODUCT_DESCRIPTION',
                             'product.client_verified':'ITEM_PRODUCT_CLIENT_VERIFIED',
                             'product.archived_at':'ITEM_ARCHIVED_AT',
                             'product.product_category':'ITEM_PRODUCT_CATEGORY',
                             'product.country_of_origin':'ITEM_PRODUCT_COUNTRY_OF_ORIGIN',
                             'container_number':'CONTAINER_NUMBER',
                             'container_type':'CONTANIER_TYPE',
                             'container_size':'CONTAINER_SIZE',
                             'seal_number':'SEAL_NUMBER',
                             'estimated_departure_date':'ESTIMATED_DEPARTURE_DATE',
                             'actual_departure_date':'ACTUAL_DEPARTURE_DATE',
                             'estimated_arrival_date':'ESTIMATED_ARRIVAL_DATE',
                             'actual_arrival_date':'ACTUAL_ARRIVAL_DATE',
                             'estimated_pickup_date':'ESTIMATED_PICKUP_DATE',
                             'actual_pickup_date':'ACTUAL_PICKUP_DATE',
                             'estimated_delivery_date':'ESTIMATED_DELIVERY_DATE',
                             'actual_delivery_date':'ACTUAL_DELIVERY_DATE',
                             'last_free_day_date':'LAST_FREE_DAY_DATE',
                             'empty_returned_date':'EMPTY_RETURNED_DATE',
                             'id_y':'CONTAINER_ID',
                             'cargo_ready_date':'CARGO_READY_DATE',
                            'shipment.id':'SHIPMENT_ID'}, inplace = True, errors = 'ignore')                          



    return(result)





# In[15]:


def split_it(SKU):
    if SKU.startswith('PF') or len(SKU) == 0:
        SKU = SKU.split()[0]
    else: 
        SKU = None
    return SKU
def api_script():
    today = date.today()
    print("Today's date:", today)
    response = requests.get(api_url_base, headers=headers)
    container = response.json()
#     container_info = container['data']
    result = pd.DataFrame()
    data_f = container_script(container)
    result = result.append(data_f,ignore_index=True)
    while container['data']['next'] is not None:
        print("Next page found, downloading", container['data']['next'])
        response = requests.get(container['data']['next'],headers=headers)
        container = response.json()
        data_f = container_script(container)
        result = result.append(data_f,ignore_index=True)
    result.to_excel('FinalOutput_container.xlsx', index=False)
    time.sleep(5)
    df = pd.read_excel("FinalOutput_container.xlsx")
    df['ITEM_PRODUCT_NAME'] = df['ITEM_PRODUCT_NAME'].str.strip()
    df['ITEM_PRODUCT_NAME2'] = df['ITEM_PRODUCT_NAME'].apply(lambda x: split_it(x))
    df.replace('',np.nan,regex=True, inplace=True)
    df['ITEM_PRODUCT_SKU'] = df['ITEM_PRODUCT_SKU'].fillna(df['ITEM_PRODUCT_NAME2'])
    df.to_excel('C:\\Processes\\python_script\\python_code_flexport_data\\Container_data\\FinalOutput_container.xlsx', index=False)
    return(print('Done'))


api_script()






