#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests, json, itertools
import numpy as np
import pandas as pd
import datetime as dt
from datetime import datetime,timedelta
from threading import Timer
import schedule
import time
from datetime import date
from pandas.io.json import json_normalize
import re


api_token = 'XXXXXXXXXXXXXXXXXXXXXXXX'
api_url_base = 'https://api.flexport.com/shipments?page=1&per=10'

headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}

# response = requests.get(api_url_base, headers=headers)
# shipping = response.json()
def shipments(shipping):
    shipping_info = shipping['data']
    shipping_info = shipping_info['data']

    df_shipping = pd.json_normalize(shipping_info, errors='ignore')



    df_shipping.drop(['_object', 'it_number','air_shipment','wants_freight_management_bco', 'wants_flexport_freight', 'shippers','consignees', 'buyers', 'sellers', 'importers_of_record','items',
           'departure_date', 'arrival_date', 'picked_up_in_full_date',
           'delivered_in_full_date', 'metadata.PO', 'metadata.SKU',
           'booking._object', 'booking.ref_type', 'booking.link', 'booking.id',
           'calculated_weight.value', 'calculated_weight.unit',
           'calculated_weight._object', 'calculated_volume.value',
           'calculated_volume.unit', 'calculated_volume._object',
           'ocean_shipment._object', 'ocean_shipment.is_lcl',
           'ocean_shipment.house_bill_number', 'ocean_shipment.master_bill_number',
           'ocean_shipment.carrier_booking_number',
           'ocean_shipment.containers._object',
           'ocean_shipment.containers.ref_type', 'ocean_shipment.containers.link',
           'dangerous_goods._object', 'dangerous_goods.review_status',
           'dangerous_goods.classifications', 'legs._object', 'legs.ref_type',
           'legs.link', 'customs_entries._object', 'customs_entries.ref_type',
           'customs_entries.link', 'commercial_invoices._object',
           'commercial_invoices.ref_type', 'commercial_invoices.link',
           'documents._object', 'documents.ref_type', 'documents.link', 'booking',
           'ocean_shipment', 'air_shipment._object',
           'air_shipment.house_airway_bill', 'air_shipment.master_airway_bill',
           'air_shipment.chargeable_weight.value',
           'air_shipment.chargeable_weight.unit',
           'air_shipment.chargeable_weight._object',
           'air_shipment.chargeable_volume.value',
           'air_shipment.chargeable_volume.unit',
           'air_shipment.chargeable_volume._object','name','target_delivery_date',
                    'booking' ], axis = 1, inplace=True, errors= 'ignore')

    df_shipping.columns



    df_items = pd.json_normalize(shipping_info,'items',['pieces'], errors='ignore')

    df_items.drop(['_object','product.product_properties', 'product.hs_codes',
           'product.classifications', 'product.suppliers','product._object','total_weight._object','total_volume._object'],axis = 1, inplace=True, errors='ignore')

    result = pd.merge(df_shipping, df_items, on='pieces')


    result.rename(columns = {'id_y':'ITEM_ID', 'total_units':'ITEM_TOTAL_UNITS', 
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
                                 'cargo_ready_date':'CARGO_READY_DATE',
                                'id_x':'SHIPMENT_ID',
                            'transportation_mode':'TRANSPORTATIONMODE',
                            'freight_type':'FREIGHTTYPE',
                            'incoterm':'INCOTERM',
                            'created_date':'SHIPMENT_CREATEDDATE',
                            'status':'SHIPMENT_STATUS',
                            'priority':'SHIPMENT_PRIORITY',
                            'updated_at':'SHIPMENT_UPDATEDAT',
                            'archived_at':'SHIPMENTARCHIVEDAT',
                            'estimated_departure_date':'SHIPMENT_ESTIMATED_DEPARTURE_DATE',
                            'estimated_arrival_date':'SHIPMENT_ESTIMATED_ARRIVAL_DATE',
                            'actual_arrival_date':'SHIPMENT_ACTUAL_ARRIVAL_DATE',
                            'estimated_picked_up_in_full_date':'SHIPMENT_ESTIMATED_PICKED_UP_IN_FULL_DATE',
                            'actual_picked_up_in_full_date':'SHIPMENT_ACTUAL_PICKED_UP_IN_FULL_DATE',
                            'estimated_delivered_in_full_date':'SHIPMENT_ESTIMATED_DELIVERED_IN_FULL_DATE',
                            'actual_delivered_in_full_date':'SHIPMENT_ACTUAL_DELIVERED_IN_FULL_DATE',
                            'cargo_ready_date':'CARGO_READY_DATE',
                            'wants_import_customs_service':'WANTS_IMPORT_CUSTOMS_SERVICE',
                            'wants_export_customs_service':'WANTS_EXPORT_CUSTOMS_SERVICE',
                            'pieces':'PIECES'}, inplace = True)

    def split_it(SKU):
        if SKU.startswith('PF') or len(SKU) == 0:
            SKU = SKU.split()[0]
        else: 
            SKU = None
        return SKU
    try:
        result['ITEM_PRODUCT_NAME'] = result['ITEM_PRODUCT_NAME'].str.strip()
        result['ITEM_PRODUCT_NAME2'] = result['ITEM_PRODUCT_NAME'].apply(lambda x: split_it(x))
        result.replace('',np.nan,regex=True, inplace=True)
        result['ITEM_PRODUCT_SKU'] = result['ITEM_PRODUCT_SKU'].fillna(result['ITEM_PRODUCT_NAME2'])
        result.drop(['ITEM_PRODUCT_NAME2'], axis = 1, inplace=True)
    except:
        print('ITEM_PRODUCT_NAME is not present')
    return (result)
#     result.to_excel('FinalOutput_2.xlsx', index=False)

#     result['ITEM_PRODUCT_SKU']


# In[8]:


def api_script():
    today = date.today()
    print("Today's date:", today)
    response = requests.get(api_url_base, headers=headers)
    shipping = response.json()
    result = pd.DataFrame()
    data_f = shipments(shipping)
    result = result.append(data_f,ignore_index=True)
    while shipping['data']['next'] is not None:
        print("Next page found, downloading", shipping['data']['next'])
        response = requests.get(shipping['data']['next'],headers=headers)
        shipping = response.json()
        data_f = shipments(shipping)
        result = result.append(data_f,ignore_index=True)
    result.to_excel('C:\\Processes\\python_script\\python_code_flexport_data\\Shipping_data\\Shipping_report.xlsx', index=False)


# In[ ]:


# schedule.every().day.at("08:30").do(api_script)
# while True: 
#     schedule.run_pending()    
#     time.sleep(1)
api_script()


# In[ ]:





# In[ ]:




