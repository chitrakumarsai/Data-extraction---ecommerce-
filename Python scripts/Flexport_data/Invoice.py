#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests, json, itertools
import pandas as pd
import datetime as dt
from datetime import datetime,timedelta
from threading import Timer
import schedule
import datetime
from datetime import date
import time
api_token = 'XXXXXXXXXXXXXXXXXXXXXXXX'
api_url_base = 'https://api.flexport.com/invoices'

headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}


# In[2]:


def flexport_invoice_item(invoice):
    invoice_info = invoice['data']
    invoice_data = invoice_info['data']
    lst_InvoiceName = []
    lst_invoice_issueDate = []
    lst_total_amount = []
    lst_item_data = []
    lst_item_name = []
    lst_item_slug = []
    lst_itemcategory = []
    lst_money = []
    lst_item_rate_value = []
    lst_item_qualifier = []
    lst_item_quantity_value = []
    lst_item_quantity_qualifier = []
    
    for i in range(len(invoice_data)):
        data = invoice_data[i]
        ID = data['id']
        for i in range(len(data['items'])):
            name = data['name']
            lst_InvoiceName.append(name)
            total_amount = str(data['total']['amount']) +' ' + str(data['total']['currency_code'])
            lst_total_amount.append(total_amount)
            item_data = data['items'][i]
            item_name = item_data['name']
            lst_item_name.append(item_name)
            invoice_issueDate = data['issued_at']
            chop = len(invoice_issueDate.split()[-1]) -10
            end_date = invoice_issueDate[:-chop]
            lst_invoice_issueDate.append(end_date)
            item_slug = item_data['slug']
            lst_item_slug.append(item_slug)
            item_category = item_data['category']
            lst_itemcategory.append(item_category)
            item_money = str(item_data['amount']['amount']) + ' ' + item_data['amount']['currency_code']
            lst_money.append(item_money)
            if item_data['rate'] != None:
                item_rate_value = item_data['rate']['value']
                lst_item_rate_value.append(item_rate_value)
                item_rate_qualifier = item_data['rate']['qualifier']
                lst_item_qualifier.append(item_rate_qualifier)
            else:
                lst_item_rate_value.append(None)
                lst_item_qualifier.append(None)
            if item_data['quantity'] != None:
                item_quantity_value = item_data['quantity']['value']
                lst_item_quantity_value.append(item_quantity_value)
                item_quantity_qualifier = item_data['quantity']['qualifier']
                lst_item_quantity_qualifier.append(item_quantity_qualifier)
            else:
                lst_item_quantity_value.append(None)
                lst_item_quantity_qualifier.append(None)
                
            
    df_invoice = pd.DataFrame(list(zip(lst_InvoiceName,lst_item_name,lst_invoice_issueDate,lst_item_slug,lst_itemcategory,lst_money,lst_item_rate_value,lst_item_quantity_qualifier,lst_item_quantity_value,lst_item_quantity_qualifier,lst_total_amount)),columns=['Invoice Number','Item name','Invoice issue date','Item slug','Item category','Amount','Rate Value','Rate Quantifier', 'Quantity Value','Quantity Qualifier','Total Amount'])
    return(df_invoice)



# In[3]:


def api_script():
    response = requests.get(api_url_base, headers=headers)
    invoice = response.json()
    result = pd.DataFrame()
    data_f = flexport_invoice_item(invoice)
    result = result.append(data_f,ignore_index=True)
    while invoice['data']['next'] is not None:
        print("Next page found, downloading", invoice['data']['next'])
        response = requests.get(invoice['data']['next'],headers=headers)
        invoice = response.json()
        data_f = flexport_invoice_item(invoice)
        result = result.append(data_f,ignore_index=True)
    result.to_excel('C:\\Processes\\python_script\\python_code_flexport_data\\Invoice_data\\Invoice_data.xlsx', index= False)
    today = date.today()
    print("Today's date:", today)


# In[4]:


# schedule.every().day.at("08:30").do(api_script)
api_script()


# In[ ]:


# while True: 
#     schedule.run_pending() 
#     time.sleep(1)


# In[ ]:




