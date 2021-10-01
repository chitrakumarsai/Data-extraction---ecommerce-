#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import rpa as r
import datetime
import os
import schedule
import time
import re
def UPS_bot():

    # begin session
    r.init(visual_automation = True)
    #navigate to ups website
    r.init()
    r.url('https://fgv.ups-scs.com/loginservicesfgv/logOn.nfdo')
    r.wait(0.35) # programatic pause to scrape ethically
    # go to login page
    r.init()
    r.click('//*[@id="top"]/div/div/div/ul/li[2]/a')
    r.wait(2.4)
    # Enter username
    r.init()
    r.type('//*[@id="signInName"]', 'karak@hyper-pet.com')
    r.wait(.23)
    # Enter Password
    r.init()
    r.type('//*[@id="password"]', 'Cosmicpet1315')
    r.wait(0.42)
    # Click on 'Sign in' button
    r.init()
    r.click('//*[@id="next"]')
    r.wait(1.8)
    # Navigate to Data tab
    r.init()
    r.click('//*[@id="navigation"]/ul/li[3]/a')
    r.wait(1.9)
    # Navigate to freight
    r.init()
    r.click('//*[@id="shipmentContent"]/div[2]/div/ul/li[1]/a')
    r.wait(0.5)
    # Date Range should be Estimated Delivery
    r.init()
    r.click('//*[@id="dateRange"]/div[1]')
    r.wait(.43)
    r.init()
    r.click('Estimated Delivery')
    r.wait(0.18)
    # From -13 weeks
    r.init()
    r.click('//*[@id="fromWeeks"]/div[1]')
    r.wait(0.12)
    r.init()
    r.click('-13 Weeks')
    r.wait(0.175)
    # To should be +13 weeks
    r.init()
    r.click('//*[@id="toWeeks"]/div[1]')
    r.wait(0.21)
    r.init()
    r.click('+13 Weeks')


    r.click('//*[@id="reference"]/div[1]')
    r.wait(0.21)
    r.init()
    r.click('Container Number')
    r.wait(0.21)
    r.init()
    r.click('//*[@id="fReferenceValue"]')
    r.wait(0.21)
    r.init()
    r.type('//*[@id="fReferenceValue"]', '%')
    r.wait(0.21)
    r.click('//*[@id="show"]/div[2]')
    r.wait(0.21)
    
    r.click('//*[@id="customizedOutput"]')
    
    r.wait(0.21)
    r.init()

    r.init()
    r.click('//*[@id="myform"]/div[2]/div/div/div[4]/div[1]/div[2]/div[2]/div[1]/div[1]/label/span')
    
    r.wait(0.21)
    r.init()
    r.click('Track')
    r.wait(0.35)
    r.init()
    r.click('//*[@id="myform"]/div[2]/div[1]/div[2]/div[1]/div/span/img')
    
    r.wait(0.21)
    r.init()
    r.click('Excel')
    r.wait(0.35)
    r.init()
    

    now = datetime.datetime.now().strftime("%y-%m-%d")
    time.sleep(15)
    general_shipment_df = pd.read_excel('SearchResult.xlsx')
    
    general_shipment_df = general_shipment_df.rename(columns=str.upper)
    general_shipment_df.columns = general_shipment_df.columns.str.replace(' ', '_')
    
    general_shipment_df.to_excel('C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\General_Shipment_data\\Data\\General Shipment Data{}.xlsx'.format(now),index= False)

    r.click('//*[@id="myform"]/div[1]/div/div/a/img')
    
    r.wait(0.35)
    r.init()
    r.click('//*[@id="myform"]/div[2]/div/div/div[4]/div[1]/div[2]/div[2]/div[2]/div[1]/label/span')
    
    r.wait(0.35)
    r.init()
    r.click('Track')
    r.wait(0.175)
    r.init()
    r.click('//*[@id="myform"]/div[2]/div[1]/div[2]/div[1]/div/span/img')
    
    r.wait(0.21)
    r.init()
    r.click('Excel')

    now = datetime.datetime.now().strftime("%y-%m-%d")
    time.sleep(15)
    general_shipment_df = pd.read_excel('SearchResult.xlsx')
    
    general_shipment_df = general_shipment_df.rename(columns=str.upper)
    general_shipment_df.columns = general_shipment_df.columns.str.replace(' ', '_')
    
    general_shipment_df.to_excel('C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Shipment_milestone_data\\Data\\Shipment Milestone Events{}.xlsx'.format(now),index= False)
    


    r.init()
    r.click('//*[@id="myform"]/div[1]/div/div/a/img')
    
    r.wait(0.21)
    r.init()
    r.click('//*[@id="myform"]/div[2]/div/div/div[4]/div[1]/div[2]/div[2]/div[3]/div[1]/label/span')
    
    r.wait(0.21)
    r.init()
    r.click('Track')
    r.wait(0.21)
    r.init()
    r.click('//*[@id="myform"]/div[2]/div[1]/div[2]/div[1]/div/span/img')
    
    r.wait(0.21)
    r.init()
    r.click('Excel')



    now = datetime.datetime.now().strftime("%y-%m-%d")
    time.sleep(15)
    general_shipment_df = pd.read_excel('SearchResult.xlsx')
    
    general_shipment_df = general_shipment_df.rename(columns=str.upper)
    general_shipment_df.columns = general_shipment_df.columns.str.replace(' ', '_')
    
    general_shipment_df.to_excel('C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Customer_references_data\\Data\\Customer References{}.xlsx'.format(now),index= False)
    



    r.init()
    r.click('//*[@id="myform"]/div[1]/div/div/a/img')
    
    r.wait(0.21)
    r.init()
    r.click('//*[@id="myform"]/div[2]/div/div/div[4]/div[1]/div[2]/div[2]/div[5]/div[1]/label/span')
    
    r.wait(0.21)
    r.init()
    r.click('Track')
    r.wait(0.21)
    r.init()
    r.click('//*[@id="myform"]/div[2]/div[1]/div[2]/div[1]/div/span/img')
    
    r.wait(0.21)
    r.init()
    r.click('Excel')


    now = datetime.datetime.now().strftime("%y-%m-%d")
    time.sleep(15)
    general_shipment_df = pd.read_excel('SearchResult.xlsx')
    
    general_shipment_df = general_shipment_df.rename(columns=str.upper)
    general_shipment_df.columns = general_shipment_df.columns.str.replace(' ', '_')
    
    general_shipment_df.to_excel('C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Ocean_container_information_data\\Data\\Ocean Container Information{}.xlsx'.format(now),index= False)

    r.init()
    r.click('//*[@id="myform"]/div[1]/div/div/a/img')
    
    r.wait(0.21)
    r.init()
    r.click('//*[@id="myform"]/div[2]/div/div/div[4]/div[1]/div[2]/div[2]/div[6]/div[1]/label/span')
    
    r.wait(0.21)
    r.init()
    r.click('Track')
    r.wait(0.21)
    r.init()
    r.click('//*[@id="myform"]/div[2]/div[1]/div[2]/div[1]/div/span/img')
    
    r.wait(0.21)
    r.init()
    r.click('Excel')



    now = datetime.datetime.now().strftime("%y-%m-%d")
    time.sleep(15)
    general_shipment_df = pd.read_excel('SearchResult.xlsx')
    
    general_shipment_df = general_shipment_df.rename(columns=str.upper)
    general_shipment_df.columns = general_shipment_df.columns.str.replace(' ', '_')
    
    general_shipment_df.to_excel('C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Container_tracking_event_data\\Data\\Container Tracking Events{}.xlsx'.format(now),index= False)
    
    r.init()
    r.click('//*[@id="myform"]/div[1]/div/div/a/img')
    
    r.wait(0.21)
    r.init()
    r.click('//*[@id="myform"]/div[2]/div/div/div[4]/div[1]/div[2]/div[2]/div[4]/div[1]/label/span')
    
    r.wait(0.21)
    r.init()
    r.click('Track')
    r.wait(0.21)
    time.sleep(200)
    r.init()
    r.click('//*[@id="myform"]/div[2]/div[1]/div[2]/div[1]/div/span/img')
    
    r.wait(0.21)
    r.init()
    r.click('Excel')



    now = datetime.datetime.now().strftime("%y-%m-%d")
    time.sleep(15)
    general_shipment_df = pd.read_excel('SearchResult.xlsx')
    
    general_shipment_df = general_shipment_df.rename(columns=str.upper)
    general_shipment_df.columns = general_shipment_df.columns.str.replace(' ', '_')
    
    general_shipment_df.to_excel('C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Party_infomation_data\\Data\\Party Information{}.xlsx'.format(now),index= False)
    
    r.close()




UPS_bot()

def UPSInfo():
    now = datetime.datetime.now().strftime("%y-%m-%d")
    directory = "C:\\Users\\chitrav\\Desktop\\RPA_UPS\\Party Information\\Sandbox\\"
    result = pd.read_excel("C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Party_infomation_data\\Data\\Total Party Information.xlsx")
    for filename in os.listdir(directory):
        if re.search(now, filename, re.IGNORECASE):
            print(filename)
            path = "C:\\Users\\chitrav\\Desktop\\RPA_UPS\\Party Information\\Sandbox\\" + filename
            newfile = pd.read_excel(path)
            newfile.columns = newfile.columns.str.encode('ascii', 'ignore').str.decode('ascii')
            newfile = newfile.rename(columns=str.upper)
            newfile.columns = newfile.columns.str.replace(' ', '_',regex=True)
            newfile.columns = newfile.columns.str.replace("/", "_",regex=True)
            newfile.columns = newfile.columns.str.replace("-", "_",regex=True)
            newfile.columns = newfile.columns.str.replace("(", "",regex=True)
            newfile.columns = newfile.columns.str.replace(")", "",regex=True)
            newfile = newfile.rename(columns={"SHIPMENT___HOUSE_BILL": "SHIPMENT_OR_HOUSE_BILL"})
            newfile.columns = newfile.columns.str.replace(' ', '_',regex=True)
            result = result.append(newfile,ignore_index=True)
            result = result.drop_duplicates()
            result.to_csv('C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Party_infomation_data\\Data\\Total Party Information.csv',index= False)
        else:
            None

    now = datetime.datetime.now().strftime("%y-%m-%d")
    directory = "C:\\Users\\chitrav\\Desktop\\RPA_UPS\\Shipment Milestone Events\\Sandbox\\"
    result = pd.read_excel("C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Shipment_milestone_data\\Data\\Total Shipment Milestone Events.xlsx")
    for filename in os.listdir(directory):
        if re.search(now, filename, re.IGNORECASE):
            print(filename)
            path = "C:\\Users\\chitrav\\Desktop\\RPA_UPS\\Shipment Milestone Events\\Sandbox\\" + filename
            newfile = pd.read_excel(path)
            newfile.columns = newfile.columns.str.encode('ascii', 'ignore').str.decode('ascii')
            newfile = newfile.rename(columns=str.upper)
            newfile.columns = newfile.columns.str.replace(' ', '_', regex= True)
            newfile.columns = newfile.columns.str.replace("/", "_", regex = True)
            newfile.columns = newfile.columns.str.replace("-", "_", regex = True)
            newfile.columns = newfile.columns.str.replace("(", "", regex= True)
            newfile.columns = newfile.columns.str.replace(")", "", regex= True)
            newfile = newfile.rename(columns={"SHIPMENT___HOUSE_BILL": "SHIPMENT_OR_HOUSE_BILL"})
            newfile.columns = newfile.columns.str.replace(' ', '_', regex = True)
            result = result.append(newfile,ignore_index=True)
            result = result.drop_duplicates()
            result.to_csv('C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Shipment_milestone_data\\Data\\Total Shipment Milestone Events.csv',index= False)
        else:
            None
            
    now = datetime.datetime.now().strftime("%y-%m-%d")
    directory = "C:\\Users\\chitrav\\Desktop\\RPA_UPS\\Ocean Container Information\\Sandbox\\"
    result = pd.read_excel("C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Ocean_container_information_data\\Data\\Total Ocean Container Information.xlsx")
    for filename in os.listdir(directory):
        if re.search(now, filename, re.IGNORECASE):
            print(filename)
            path = "C:\\Users\\chitrav\\Desktop\\RPA_UPS\\Ocean Container Information\\Sandbox\\" + filename
            newfile = pd.read_excel(path)
            newfile.columns = newfile.columns.str.encode('ascii', 'ignore').str.decode('ascii')
            newfile = newfile.rename(columns=str.upper)
            newfile.columns = newfile.columns.str.replace(' ', '_', regex = True)
            newfile.columns = newfile.columns.str.replace("/", "_", regex = True)
            newfile.columns = newfile.columns.str.replace("-", "_", regex = True)
            newfile.columns = newfile.columns.str.replace("(", "", regex = True)
            newfile.columns = newfile.columns.str.replace(")", "", regex = True)
            newfile = newfile.rename(columns={"SHIPMENT___HOUSE_BILL": "SHIPMENT_OR_HOUSE_BILL"})
            newfile.columns = newfile.columns.str.replace(' ', '_', regex = True)
            result = result.append(newfile,ignore_index=True)
            result = result.drop_duplicates()
            result.to_csv('C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Ocean_container_information_data\\Data\\Total Ocean Container Information.csv',index= False)
        else:
            None
            
    now = datetime.datetime.now().strftime("%y-%m-%d")
    directory = "C:\\Users\\chitrav\\Desktop\\RPA_UPS\\General Shipment Data\\Sandbox\\"
    result = pd.read_excel("C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\General_Shipment_data\\Data\\Total General Shipment Data.xlsx")
    for filename in os.listdir(directory):
        if re.search(now, filename, re.IGNORECASE):
            print(filename)
            path = "C:\\Users\\chitrav\\Desktop\\RPA_UPS\\General Shipment Data\\Sandbox\\" + filename
            newfile = pd.read_excel(path)
            newfile.columns = newfile.columns.str.encode('ascii', 'ignore').str.decode('ascii')
            newfile = newfile.rename(columns=str.upper)
            newfile.columns = newfile.columns.str.replace(' ', '_', regex = True)
            newfile.columns = newfile.columns.str.replace("/", "_", regex = True)
            newfile.columns = newfile.columns.str.replace("-", "_", regex = True)
            newfile.columns = newfile.columns.str.replace("(", "", regex = True)
            newfile.columns = newfile.columns.str.replace(")", "", regex = True)
            newfile = newfile.rename(columns={"SHIPMENT___HOUSE_BILL": "SHIPMENT_OR_HOUSE_BILL"})
            newfile.columns = newfile.columns.str.replace(' ', '_', regex = True)
            result = result.append(newfile,ignore_index=True)
            result = result.drop_duplicates()
            result.to_csv('C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\General_Shipment_data\\Data\\Total General Shipment Data.csv',index= False)
        else:
            None
            
    now = datetime.datetime.now().strftime("%y-%m-%d")
    directory = "C:\\Users\\chitrav\\Desktop\\RPA_UPS\\Customer References\\Sandbox\\"
    result = pd.read_excel("C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Customer_references_data\\Data\\Total Customer References.xlsx")
    for filename in os.listdir(directory):
        if re.search(now, filename, re.IGNORECASE):
            print(filename)
            path = "C:\\Users\\chitrav\\Desktop\\RPA_UPS\\Customer References\\Sandbox\\" + filename
            newfile = pd.read_excel(path)
            newfile.columns = newfile.columns.str.encode('ascii', 'ignore').str.decode('ascii')
            newfile = newfile.rename(columns=str.upper)
            newfile.columns = newfile.columns.str.replace(' ', '_', regex = True)
            newfile.columns = newfile.columns.str.replace("/", "_", regex = True)
            newfile.columns = newfile.columns.str.replace("-", "_", regex = True)
            newfile.columns = newfile.columns.str.replace("(", "", regex = True)
            newfile.columns = newfile.columns.str.replace(")", "", regex = True)
            newfile = newfile.rename(columns={"SHIPMENT___HOUSE_BILL": "SHIPMENT_OR_HOUSE_BILL"})
            newfile.columns = newfile.columns.str.replace(' ', '_', regex = True)
            result = result.append(newfile,ignore_index=True)
            result = result.drop_duplicates()
            result.to_csv('C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Customer_references_data\\Data\\Total Customer References.csv',index= False)
        else:
            None
            
    now = datetime.datetime.now().strftime("%y-%m-%d")
    directory = "C:\\Users\\chitrav\\Desktop\\RPA_UPS\\Container Tracking Events\\Sandbox\\"
    result = pd.read_excel("C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Container_tracking_event_data\\Data\\Total Container Tracking Events.xlsx")
    for filename in os.listdir(directory):
        if re.search(now, filename, re.IGNORECASE):
            print(filename)
            path = "C:\\Users\\chitrav\\Desktop\\RPA_UPS\\Container Tracking Events\\Sandbox\\" + filename
            newfile = pd.read_excel(path)
            newfile.columns = newfile.columns.str.encode('ascii', 'ignore').str.decode('ascii')
            newfile = newfile.rename(columns=str.upper)
            newfile.columns = newfile.columns.str.replace(' ', '_', regex = True)
            newfile.columns = newfile.columns.str.replace("/", "_", regex = True)
            newfile.columns = newfile.columns.str.replace("-", "_", regex = True)
            newfile.columns = newfile.columns.str.replace("(", "", regex = True)
            newfile.columns = newfile.columns.str.replace(")", "", regex = True)
            newfile = newfile.rename(columns={"SHIPMENT___HOUSE_BILL": "SHIPMENT_OR_HOUSE_BILL"})
            newfile.columns = newfile.columns.str.replace(' ', '_', regex = True)
            result = result.append(newfile,ignore_index=True)
            result = result.drop_duplicates()
            result.to_csv('C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Container_tracking_event_data\\Data\\Total Container Tracking Events.csv',index= False)
            
        else:
            None




UPSInfo()


def UPS_Col():
    df1 = pd.read_csv("C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Ocean_container_information_data\\Data\\Total Ocean Container Information.csv",low_memory=False)
    df1['LATEST_STATUS_DATE'] = pd.to_datetime(df1['LATEST_STATUS_DATE'],errors = 'coerce')
    df1['CONFIRMED_DEPARTURE'] = pd.to_datetime(df1['CONFIRMED_DEPARTURE'],errors = 'coerce')
    df1['SHIPMENT_BOOKED'] = pd.to_datetime(df1['SHIPMENT_BOOKED'],errors = 'coerce')
    df1['DELIVERED'] = pd.to_datetime(df1['DELIVERED'],errors = 'coerce')
    df1['LATEST_CONTAINER_STATUS_DATE_TIME'] = pd.to_datetime(df1['LATEST_CONTAINER_STATUS_DATE_TIME'],errors = 'coerce')
    df1['CONTAINER_DATA_LAST_UPDATED'] = pd.to_datetime(df1['CONTAINER_DATA_LAST_UPDATED'],errors = 'coerce')

    df1['CONTAINER_ORIGIN_OUT_GATE_DATE_TIME'] = pd.to_datetime(df1['CONTAINER_ORIGIN_OUT_GATE_DATE_TIME'],errors = 'coerce')
    df1['CONTAINER_ORIGIN_IN_GATE_DATE_TIME'] = pd.to_datetime(df1['CONTAINER_ORIGIN_IN_GATE_DATE_TIME'],errors = 'coerce')
    df1['CONTAINER_ETD_FROM_PORT_OF_LOAD_DATE_TIME'] = pd.to_datetime(df1['CONTAINER_ETD_FROM_PORT_OF_LOAD_DATE_TIME'],errors = 'coerce')
    df1['CONTAINER_LOADED_ON_VESSEL_DATE_TIME'] = pd.to_datetime(df1['CONTAINER_LOADED_ON_VESSEL_DATE_TIME'],errors = 'coerce')
    df1['VESSEL_DEPARTURE_DATE_TIME'] = pd.to_datetime(df1['VESSEL_DEPARTURE_DATE_TIME'],errors = 'coerce')
    df1['CONTAINER_ETA_AT_PLACE_OF_DELIVERY_DATE_TIME'] = pd.to_datetime(df1['CONTAINER_ETA_AT_PLACE_OF_DELIVERY_DATE_TIME'],errors = 'coerce')
    df1['VESSEL_ARRIVED_DATE_TIME'] = pd.to_datetime(df1['VESSEL_ARRIVED_DATE_TIME'],errors = 'coerce')
    df1['CONTAINER_LOADED_ON_RAIL_DATE_TIME'] = pd.to_datetime(df1['CONTAINER_LOADED_ON_RAIL_DATE_TIME'],errors = 'coerce')
    df1['CONTAINER_RAIL_ARVL_DEST_INTERMODAL_RAMP_DATE_TIME'] = pd.to_datetime(df1['CONTAINER_RAIL_ARVL_DEST_INTERMODAL_RAMP_DATE_TIME'],errors = 'coerce')
    df1['CONTAINER_DESTINATION_OUT_GATE_DATE_TIME'] = pd.to_datetime(df1['CONTAINER_DESTINATION_OUT_GATE_DATE_TIME'],errors = 'coerce')
    df1['RETURN_CONTAINER_DATE_TIME'] = pd.to_datetime(df1['RETURN_CONTAINER_DATE_TIME'],errors = 'coerce')


    df1.to_csv('C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Ocean_container_information_data\\Total Ocean Container Information.csv',index= False)

    df2 = pd.read_csv("C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Container_tracking_event_data\\Data\\Total Container Tracking Events.csv", low_memory=False)
    df2.head()

    df2['LATEST_STATUS_DATE'] = pd.to_datetime(df2['LATEST_STATUS_DATE'],errors = 'coerce')
    df2['CONFIRMED_DEPARTURE'] = pd.to_datetime(df2['CONFIRMED_DEPARTURE'],errors = 'coerce')
    df2['SHIPMENT_BOOKED'] = pd.to_datetime(df2['SHIPMENT_BOOKED'],errors = 'coerce')
    df2['DELIVERED'] = pd.to_datetime(df2['DELIVERED'],errors = 'coerce')
    df2['CONTAINER_TRACKING_EVENT_DATE_TIME_LOCAL'] = pd.to_datetime(df2['CONTAINER_TRACKING_EVENT_DATE_TIME_LOCAL'],errors = 'coerce')
    df2['DELIVERED'] = pd.to_datetime(df2['DELIVERED'],errors = 'coerce')



    df2.to_csv('C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Container_tracking_event_data\\Total Container Tracking Events.csv',index= False)

    df3 = pd.read_csv("C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Customer_references_data\\Data\\Total Customer References.csv", low_memory=False)

    df3['LATEST_STATUS_DATE'] = pd.to_datetime(df3['LATEST_STATUS_DATE'],errors = 'coerce')
    df3['CONFIRMED_DEPARTURE'] = pd.to_datetime(df3['CONFIRMED_DEPARTURE'],errors = 'coerce')
    df3['SHIPMENT_BOOKED'] = pd.to_datetime(df3['SHIPMENT_BOOKED'],errors = 'coerce')
    
    df3['DELIVERED'] = pd.to_datetime(df3['DELIVERED'],errors = 'coerce')



    df3.to_csv("C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Customer_references_data\\Total Customer References.csv", index = False)

    df4 = pd.read_csv("C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\General_Shipment_data\\Data\\Total General Shipment Data.csv", low_memory=False)


    df4['LATEST_STATUS_DATE'] = pd.to_datetime(df4['LATEST_STATUS_DATE'],errors = 'coerce')
    df4['CONFIRMED_DEPARTURE'] = pd.to_datetime(df4['CONFIRMED_DEPARTURE'],errors = 'coerce')
    df4['SHIPMENT_BOOKED'] = pd.to_datetime(df4['SHIPMENT_BOOKED'],errors = 'coerce')
    df4['DELIVERED'] = pd.to_datetime(df4['DELIVERED'],errors = 'coerce')
    df4['SHIPMENT_DATA_LAST_UPDATED'] = pd.to_datetime(df4['SHIPMENT_DATA_LAST_UPDATED'],errors = 'coerce')

    df4.to_csv("C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\General_Shipment_data\\Total General Shipment Data.csv", index=False)

    df5 = pd.read_csv("C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Party_infomation_data\\Data\\Total Party Information.csv", low_memory=False)

    df5['LATEST_STATUS_DATE'] = pd.to_datetime(df5['LATEST_STATUS_DATE'],errors = 'coerce')
    df5['CONFIRMED_DEPARTURE'] = pd.to_datetime(df5['CONFIRMED_DEPARTURE'],errors = 'coerce')
    df5['SHIPMENT_BOOKED'] = pd.to_datetime(df5['SHIPMENT_BOOKED'],errors = 'coerce')
    df5['DELIVERED'] = pd.to_datetime(df5['DELIVERED'])
    
    df5.to_csv("C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Party_infomation_data\\Total Party Information.csv", index=False)

    df6 = pd.read_csv("C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Shipment_milestone_data\\Data\\Total Shipment Milestone Events.csv", low_memory=False)
    df6['LATEST_STATUS_DATE'] = pd.to_datetime(df6['LATEST_STATUS_DATE'],errors = 'coerce')
    df6['CONFIRMED_DEPARTURE'] = pd.to_datetime(df6['CONFIRMED_DEPARTURE'],errors = 'coerce')
    df6['SHIPMENT_BOOKED'] = pd.to_datetime(df6['SHIPMENT_BOOKED'],errors = 'coerce')
    df6['DELIVERED'] = pd.to_datetime(df6['DELIVERED'],errors = 'coerce')
    df6['PLANNED_PICKUP_DATE'] = pd.to_datetime(df6['PLANNED_PICKUP_DATE'],errors = 'coerce')
    df6['BOOKING_RECEIVED_FROM_CUSTOMER'] = pd.to_datetime(df6['BOOKING_RECEIVED_FROM_CUSTOMER'],errors = 'coerce')
    df6['RECEIVED_INTO_UPS_POSSESSION_PICKED_UP'] = pd.to_datetime(df6['RECEIVED_INTO_UPS_POSSESSION_PICKED_UP'],errors = 'coerce')
    df6['DATE_AVAILABLE_TO_SHIP'] = pd.to_datetime(df6['DATE_AVAILABLE_TO_SHIP'],errors = 'coerce')
    df6['DOCUMENTS_RECEIVED_FROM_SHIPPER'] = pd.to_datetime(df6['DOCUMENTS_RECEIVED_FROM_SHIPPER'],errors = 'coerce')
    df6['DATE_OF_EXPORT'] = pd.to_datetime(df6['DATE_OF_EXPORT'],errors = 'coerce')
    df6['ETD_FROM_PORT_OF_LOAD'] = pd.to_datetime(df6['ETD_FROM_PORT_OF_LOAD'],errors = 'coerce')
    df6['ESTIMATED_DEPARTUREED'] = pd.to_datetime(df6['ESTIMATED_DEPARTUREED'],errors = 'coerce')
    df6['ETD_FROM_PORT_OF_LOAD'] = pd.to_datetime(df6['ETD_FROM_PORT_OF_LOAD'],errors = 'coerce')
    df6['ETA_AT_PORT_OF_DISCHARGE'] = pd.to_datetime(df6['ETA_AT_PORT_OF_DISCHARGE'],errors = 'coerce')
    df6['ETD_FROM_PORT_OF_LOAD'] = pd.to_datetime(df6['ETD_FROM_PORT_OF_LOAD'],errors = 'coerce')
    df6[['LATEST_ESTIMATED_ARRIVAL_ETA','CONFIRMED_ARRIVAL','ARRIVED_AT_DESTINATION_COUNTRY_OR_TERRITORY','CONFIRMED_ARRIVAL_AT_FINAL_CARRIER_B_L_POINT','ON_HAND_AT_DESTINATION','DOCUMENTS_TURNED_OVER_TO_UPS_OUTSIDE_BROKER_','CLEARED_CUSTOMS','CARRIER_AND_CUSTOMS_RELEASED','DELIVERY_ORDER_ISSUED','ORIGINAL_ESTIMATED_DELIVERY_DATE','REVISED_ESTIMATED_DELIVERY_DATE','OUT_FOR_DELIVERY','US_ISF_ACCEPTED','US_ISF_ACCEPTED_WITH_WARNING','US_ISF_MATCHED_TO_AMS_BILL_ON_FILE','US_ISF_CUT_OFF_DATE','LAST_EVENT_OCCURRED_DATE','SOLAS_TRANSMITTED_DATE']] = df6[['LATEST_ESTIMATED_ARRIVAL_ETA','CONFIRMED_ARRIVAL','ARRIVED_AT_DESTINATION_COUNTRY_OR_TERRITORY','CONFIRMED_ARRIVAL_AT_FINAL_CARRIER_B_L_POINT','ON_HAND_AT_DESTINATION','DOCUMENTS_TURNED_OVER_TO_UPS_OUTSIDE_BROKER_','CLEARED_CUSTOMS','CARRIER_AND_CUSTOMS_RELEASED','DELIVERY_ORDER_ISSUED','ORIGINAL_ESTIMATED_DELIVERY_DATE','REVISED_ESTIMATED_DELIVERY_DATE','OUT_FOR_DELIVERY','US_ISF_ACCEPTED','US_ISF_ACCEPTED_WITH_WARNING','US_ISF_MATCHED_TO_AMS_BILL_ON_FILE','US_ISF_CUT_OFF_DATE','LAST_EVENT_OCCURRED_DATE','SOLAS_TRANSMITTED_DATE']].apply(pd.to_datetime,errors = 'coerce')

    df6.to_csv("C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Shipment_milestone_data\\Total Shipment Milestone Events.csv", index=False)

UPS_Col()









