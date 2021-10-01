#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import glob
import os
import schedule
import time
from datetime import date
def DSDC():
    files = glob.glob("C:\\Processes\\python_script\\DSDC_code_flow\\Mission_pet_data\\Mission_pet_info\\*.xlsx")
    for f in files:
        print(f)
        os.remove(f)
    files = glob.glob("C:\\Processes\\python_script\\DSDC_code_flow\\Bow&Arrow_data\\Bow&Arrow_info\\*.xlsx")
    for f in files:
        print(f)
        os.remove(f)
    files = glob.glob("C:\\Processes\\python_script\\DSDC_code_flow\\Trixie_pet_data\\TrixiePet_info\\*.xlsx")
    for f in files:
        print(f)
        os.remove(f)
    files = glob.glob("C:\\Processes\\python_script\\DSDC_code_flow\\Hatfield_data\\Hatfield_info\\*.xlsx")
    for f in files:
        print(f)
        os.remove(f)
    today = date.today()
    print("Today's date:", today)
    #####################################
    df = pd.read_excel("C:\\Processes\\python_script\\DSDC_code_flow\\Mission_pet_data\\Inventory_MissionPet.xlsx", sheet_name = 'Summary')
    df1 = pd.read_excel("C:\\Processes\\python_script\\DSDC_code_flow\\Mission_pet_data\\Inventory_MissionPet.xlsx", sheet_name = 'PO_info')
    df2 = pd.read_excel("C:\\Processes\\python_script\\DSDC_code_flow\\Mission_pet_data\\Inventory_MissionPet.xlsx", sheet_name = 'SO_details')



    Total_Charge = df['Charge'].sum()
    Total_shipment = df['CO_Shipment'].sum()

    df = df.append({'item': 'Total', 'CO_Shipment':Total_shipment, 'Rate': 0.12, 'Charge': Total_Charge}, ignore_index=True)



    writer = pd.ExcelWriter('C:\\Processes\\python_script\\DSDC_code_flow\\Mission_pet_data\\Mission_pet_info\\Inventory_MissionPet.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Summary', index = False)
    df1.to_excel(writer, sheet_name='PO_info', index = False)
    df2.to_excel(writer, sheet_name='SO_details', index = False)
    writer.save()
    #########################################
    
    df = pd.read_excel("C:\\Processes\\python_script\\DSDC_code_flow\\Bow&Arrow_data\\Inventory_Bow&Arrow.xlsx", sheet_name= 'Summary')
    df1 = pd.read_excel("C:\\Processes\\python_script\\DSDC_code_flow\\Bow&Arrow_data\\Inventory_Bow&Arrow.xlsx", sheet_name= 'PO_info')
    df2 = pd.read_excel("C:\\Processes\\python_script\\DSDC_code_flow\\Bow&Arrow_data\\Inventory_Bow&Arrow.xlsx", sheet_name= 'SO_details')



    Total_Charge = df['Charge'].sum()
    Total_shipment = df['CO_Shipment'].sum()

    df = df.append({'item': 'Total', 'CO_Shipment':Total_shipment, 'Rate': 0.12, 'Charge': Total_Charge}, ignore_index=True)


    writer = pd.ExcelWriter('C:\\Processes\\python_script\\DSDC_code_flow\\Bow&Arrow_data\\Bow&Arrow_info\\Inventory_Bow&Arrow.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Summary', index = False)
    df1.to_excel(writer, sheet_name='PO_info', index = False)
    df2.to_excel(writer, sheet_name='SO_details', index = False)
    writer.save()
    ###########################################
    
    df = pd.read_excel("C:\\Processes\\python_script\\DSDC_code_flow\\Trixie_pet_data\\Inventory_TrixiePet.xlsx",sheet_name='Summary')
    df1 = pd.read_excel("C:\\Processes\\python_script\\DSDC_code_flow\\Trixie_pet_data\\Inventory_TrixiePet.xlsx",sheet_name='PO_info')
    df2 = pd.read_excel("C:\\Processes\\python_script\\DSDC_code_flow\\Trixie_pet_data\\Inventory_TrixiePet.xlsx",sheet_name='SO_Details')



    Total_Charge = df['Charge'].sum()
    Total_shipment = df['CO_Shipment'].sum()

    df = df.append({'item': 'Total', 'CO_Shipment':Total_shipment, 'Rate': 0.12, 'Charge': Total_Charge}, ignore_index=True)

    writer = pd.ExcelWriter('C:\\Processes\\python_script\\DSDC_code_flow\\Trixie_pet_data\\TrixiePet_info\\Inventory_TrixiePet.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Summary', index= False)
    df1.to_excel(writer, sheet_name='PO_info', index = False)
    df2.to_excel(writer, sheet_name='SO_Details', index = False)
    writer.save()

    ###############################################

    df = pd.read_excel("C:\\Processes\\python_script\\DSDC_code_flow\\Hatfield_data\\Inventory_Hatfield.xlsx",sheet_name='Summary')
    df1 = pd.read_excel("C:\\Processes\\python_script\\DSDC_code_flow\\Hatfield_data\\Inventory_Hatfield.xlsx",sheet_name='PO_info')
    df2 = pd.read_excel("C:\\Processes\\python_script\\DSDC_code_flow\\Hatfield_data\\Inventory_Hatfield.xlsx",sheet_name='SO_details')



    Total_shipment = df['CO_Shipment'].sum()

    df = df.append({'item': 'Total', 'CO_Shipment':Total_shipment}, ignore_index=True)

    writer = pd.ExcelWriter('C:\Processes\\python_script\\DSDC_code_flow\\Hatfield_data\\Hatfield_info\\Inventory_Hatfield.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Summary',index= False)
    df1.to_excel(writer, sheet_name='PO_info', index = False)
    df2.to_excel(writer, sheet_name='SO_details', index= False)
    writer.save()
    ##################################################
 


# In[ ]:


# schedule.every().monday.at("05:45").do(DSDC)
# while True: 
#     schedule.run_pending() 
#     time.sleep(1)
DSDC()


# In[ ]:





# In[ ]:




