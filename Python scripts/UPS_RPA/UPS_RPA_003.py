#!/usr/bin/env python
# coding: utf-8

# In[ ]:




from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
import glob
import os.path, time
import datetime
from datetime import date
import numpy as np
import datetime
import os
import schedule
import re
from selenium.webdriver.common.keys import Keys


chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\General_Shipment_data\\Data\\"}
chromeOptions.add_experimental_option("prefs",prefs)
chromedriver = "C:/Processes/python_script/RPA_UPS/chromedriver.exe"
chromeOptions.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)
driver.maximize_window()

URL = "https://fgv.ups-scs.com/loginservicesfgv/logOn.nfdo"
driver.get (URL)
time.sleep(5)
driver.refresh()
login_xpath = "//*[@id='top']/div/div/div/ul/li[2]/a"
time.sleep(2)
driver.find_element_by_xpath(login_xpath).click()
time.sleep(2)

driver.find_element_by_id("signInName").send_keys("karak@hyper-pet.com")
time.sleep(2)
driver.find_element_by_id ("password").send_keys("Cosmicpet1315")
time.sleep(2)
driver.find_element_by_id("next").click()
time.sleep(5)

Data_xpath = "//*[@id='navigation']/ul/li[3]/a"
time.sleep(2)
driver.find_element_by_xpath(Data_xpath).click()
time.sleep(5)

ship_xpath = "//*[@id='reference']/div[1]"
time.sleep(2)
driver.find_element_by_xpath(ship_xpath).click()
time.sleep(5)



html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)

ship_xpath_3 = "/html/body/form/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div[4]/div/div/div[2]/div[3]"
time.sleep(2)
driver.find_element_by_xpath(ship_xpath_3).click()
time.sleep(5)

reference_xpath = "//*[@id='fReferenceValue']"
time.sleep(5)
driver.find_element_by_id ("fReferenceValue").send_keys("%")
time.sleep(5)

custom_xpath = "//*[@id='customizedOutput']"
time.sleep(2)
driver.find_element_by_xpath(custom_xpath).click()
time.sleep(5)
driver.refresh()

container_xpath = "//*[@id='myform']/div[2]/div/div/div[4]/div[1]/div[2]/div[2]/div[1]/div[1]/label/span"
time.sleep(2)
driver.find_element_by_xpath(container_xpath).click()
time.sleep(5)

html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)
track= "//*[@id='customSearchTrack']"
time.sleep(2)
driver.find_element_by_xpath(track).click()
time.sleep(5)

excel_1 = "//*[@id='myform']/div[3]/div[1]/div[2]/div[1]/div/span/img"
time.sleep(5)
driver.find_element_by_xpath(excel_1).click()
time.sleep(5)

excel_2 = "//*[@id='myform']/div[3]/div[1]/div[2]/div[2]/a[1]"
time.sleep(5)
driver.find_element_by_xpath(excel_2).click()
time.sleep(5)
driver.close()
driver.quit()
Current_Date = datetime.datetime.today().strftime ('%y-%m-%d')
os.rename(r'C:\Processes\python_script\RPA_UPS\UPS_data\General_Shipment_data\Data\SearchResult.xlsx',r'C:\Processes\python_script\RPA_UPS\UPS_data\General_Shipment_data\Data\General Shipment Data' + str(Current_Date) + '.xlsx')


# In[ ]:





# In[133]:


chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Shipment_milestone_data\\Data\\"}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_experimental_option("excludeSwitches", ["enable-logging"])
chromedriver = "C:/Processes/python_script/RPA_UPS/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)
driver.maximize_window()


# In[134]:


URL = "https://fgv.ups-scs.com/loginservicesfgv/logOn.nfdo"
driver.get (URL)
time.sleep(5)
driver.refresh()
login_xpath = "//*[@id='top']/div/div/div/ul/li[2]/a"
time.sleep(2)
driver.find_element_by_xpath(login_xpath).click()
time.sleep(2)

driver.find_element_by_id("signInName").send_keys("karak@hyper-pet.com")
time.sleep(2)
driver.find_element_by_id ("password").send_keys("Cosmicpet1315")
time.sleep(2)
driver.find_element_by_id("next").click()
time.sleep(5)

Data_xpath = "//*[@id='navigation']/ul/li[3]/a"
time.sleep(2)
driver.find_element_by_xpath(Data_xpath).click()
time.sleep(5)

ship_xpath = "//*[@id='reference']/div[1]"
time.sleep(2)
driver.find_element_by_xpath(ship_xpath).click()
time.sleep(5)



html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)

ship_xpath_3 = "/html/body/form/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div[4]/div/div/div[2]/div[3]"
time.sleep(2)
driver.find_element_by_xpath(ship_xpath_3).click()
time.sleep(5)

reference_xpath = "//*[@id='fReferenceValue']"
time.sleep(5)
driver.find_element_by_id ("fReferenceValue").send_keys("%")
time.sleep(5)

custom_xpath = "//*[@id='customizedOutput']"
time.sleep(2)
driver.find_element_by_xpath(custom_xpath).click()
time.sleep(5)
driver.refresh()


# In[135]:


milestone = "//*[@id='myform']/div[2]/div/div/div[4]/div[1]/div[2]/div[2]/div[2]/div[1]/label"
time.sleep(2)
driver.find_element_by_xpath(milestone).click()
time.sleep(5)
html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)
track= "//*[@id='customSearchTrack']"
time.sleep(2)
driver.find_element_by_xpath(track).click()
time.sleep(5)

excel_1 = "//*[@id='myform']/div[3]/div[1]/div[2]/div[1]/div/span/img"
time.sleep(5)
driver.find_element_by_xpath(excel_1).click()
time.sleep(5)

excel_2 = "//*[@id='myform']/div[3]/div[1]/div[2]/div[2]/a[1]"
time.sleep(5)
driver.find_element_by_xpath(excel_2).click()
time.sleep(5)
driver.close()
driver.quit()

# In[136]:


Current_Date = datetime.datetime.today().strftime ('%y-%m-%d')
os.rename(r'C:\Processes\python_script\RPA_UPS\UPS_data\Shipment_milestone_data\Data\SearchResult.xlsx',r'C:\Processes\python_script\RPA_UPS\UPS_data\Shipment_milestone_data\Data\Shipment Milestone Events' + str(Current_Date) + '.xlsx')


# In[137]:


chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Customer_references_data\\Data\\"}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_experimental_option("excludeSwitches", ["enable-logging"])
chromedriver = "C:/Processes/python_script/RPA_UPS/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)
driver.maximize_window()


# In[138]:


URL = "https://fgv.ups-scs.com/loginservicesfgv/logOn.nfdo"
driver.get (URL)
time.sleep(5)
driver.refresh()
login_xpath = "//*[@id='top']/div/div/div/ul/li[2]/a"
time.sleep(2)
driver.find_element_by_xpath(login_xpath).click()
time.sleep(2)

driver.find_element_by_id("signInName").send_keys("karak@hyper-pet.com")
time.sleep(2)
driver.find_element_by_id ("password").send_keys("Cosmicpet1315")
time.sleep(2)
driver.find_element_by_id("next").click()
time.sleep(5)

Data_xpath = "//*[@id='navigation']/ul/li[3]/a"
time.sleep(2)
driver.find_element_by_xpath(Data_xpath).click()
time.sleep(5)

ship_xpath = "//*[@id='reference']/div[1]"
time.sleep(2)
driver.find_element_by_xpath(ship_xpath).click()
time.sleep(5)



html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)

ship_xpath_3 = "/html/body/form/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div[4]/div/div/div[2]/div[3]"
time.sleep(2)
driver.find_element_by_xpath(ship_xpath_3).click()
time.sleep(5)

reference_xpath = "//*[@id='fReferenceValue']"
time.sleep(5)
driver.find_element_by_id ("fReferenceValue").send_keys("%")
time.sleep(5)

custom_xpath = "//*[@id='customizedOutput']"
time.sleep(2)
driver.find_element_by_xpath(custom_xpath).click()
time.sleep(5)
driver.refresh()


# In[139]:


cust_ref = "//*[@id='myform']/div[2]/div/div/div[4]/div[1]/div[2]/div[2]/div[3]/div[1]/label"
time.sleep(5)
driver.find_element_by_xpath(cust_ref).click()
time.sleep(5)
html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)
track= "//*[@id='customSearchTrack']"
time.sleep(5)
driver.find_element_by_xpath(track).click()
time.sleep(5)

excel_1 = "//*[@id='myform']/div[3]/div[1]/div[2]/div[1]/div/span/img"
time.sleep(5)
driver.find_element_by_xpath(excel_1).click()
time.sleep(5)

excel_2 = "//*[@id='myform']/div[3]/div[1]/div[2]/div[2]/a[1]"
time.sleep(5)
driver.find_element_by_xpath(excel_2).click()
time.sleep(5)
driver.close()
driver.quit()

# In[140]:


Current_Date = datetime.datetime.today().strftime ('%y-%m-%d')
os.rename(r'C:\Processes\python_script\RPA_UPS\UPS_data\Customer_references_data\Data\SearchResult.xlsx',r'C:\Processes\python_script\RPA_UPS\UPS_data\Customer_references_data\Data\Customer References' + str(Current_Date) + '.xlsx')


# In[141]:


chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Ocean_container_information_data\\Data\\"}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_experimental_option("excludeSwitches", ["enable-logging"])
chromedriver = "C:/Processes/python_script/RPA_UPS/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)
driver.maximize_window()


# In[142]:


URL = "https://fgv.ups-scs.com/loginservicesfgv/logOn.nfdo"
driver.get (URL)
time.sleep(5)
driver.refresh()
login_xpath = "//*[@id='top']/div/div/div/ul/li[2]/a"
time.sleep(2)
driver.find_element_by_xpath(login_xpath).click()
time.sleep(2)

driver.find_element_by_id("signInName").send_keys("karak@hyper-pet.com")
time.sleep(2)
driver.find_element_by_id ("password").send_keys("Cosmicpet1315")
time.sleep(2)
driver.find_element_by_id("next").click()
time.sleep(5)

Data_xpath = "//*[@id='navigation']/ul/li[3]/a"
time.sleep(2)
driver.find_element_by_xpath(Data_xpath).click()
time.sleep(5)

ship_xpath = "//*[@id='reference']/div[1]"
time.sleep(2)
driver.find_element_by_xpath(ship_xpath).click()
time.sleep(5)



html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)

ship_xpath_3 = "/html/body/form/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div[4]/div/div/div[2]/div[3]"
time.sleep(2)
driver.find_element_by_xpath(ship_xpath_3).click()
time.sleep(5)

reference_xpath = "//*[@id='fReferenceValue']"
time.sleep(5)
driver.find_element_by_id ("fReferenceValue").send_keys("%")
time.sleep(5)

custom_xpath = "//*[@id='customizedOutput']"
time.sleep(2)
driver.find_element_by_xpath(custom_xpath).click()
time.sleep(5)
driver.refresh()


# In[143]:


ocean_path = "//*[@id='myform']/div[2]/div/div/div[4]/div[1]/div[2]/div[2]/div[5]/div[1]/label"
time.sleep(5)
driver.find_element_by_xpath(ocean_path).click()
time.sleep(5)
html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)
track= "//*[@id='customSearchTrack']"
time.sleep(5)
driver.find_element_by_xpath(track).click()
time.sleep(5)

excel_1 = "//*[@id='myform']/div[3]/div[1]/div[2]/div[1]/div/span/img"
time.sleep(5)
driver.find_element_by_xpath(excel_1).click()
time.sleep(5)

excel_2 = "//*[@id='myform']/div[3]/div[1]/div[2]/div[2]/a[1]"
time.sleep(5)
driver.find_element_by_xpath(excel_2).click()
time.sleep(5)
driver.close()
driver.quit()

# In[144]:


Current_Date = datetime.datetime.today().strftime ('%y-%m-%d')
os.rename(r'C:\Processes\python_script\RPA_UPS\UPS_data\Ocean_container_information_data\Data\SearchResult.xlsx',r'C:\Processes\python_script\RPA_UPS\UPS_data\Ocean_container_information_data\Data\Ocean Container Information' + str(Current_Date) + '.xlsx')


# In[145]:


chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Party_infomation_data\\Data\\"}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_experimental_option("excludeSwitches", ["enable-logging"])
chromedriver = "C:/Processes/python_script/RPA_UPS/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)
driver.maximize_window()


# In[ ]:





# In[146]:


URL = "https://fgv.ups-scs.com/loginservicesfgv/logOn.nfdo"
driver.get (URL)
time.sleep(5)
driver.refresh()
login_xpath = "//*[@id='top']/div/div/div/ul/li[2]/a"
time.sleep(2)
driver.find_element_by_xpath(login_xpath).click()
time.sleep(2)

driver.find_element_by_id("signInName").send_keys("karak@hyper-pet.com")
time.sleep(2)
driver.find_element_by_id ("password").send_keys("Cosmicpet1315")
time.sleep(2)
driver.find_element_by_id("next").click()
time.sleep(5)

Data_xpath = "//*[@id='navigation']/ul/li[3]/a"
time.sleep(2)
driver.find_element_by_xpath(Data_xpath).click()
time.sleep(5)

ship_xpath = "//*[@id='reference']/div[1]"
time.sleep(2)
driver.find_element_by_xpath(ship_xpath).click()
time.sleep(5)



html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)

ship_xpath_3 = "/html/body/form/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div[4]/div/div/div[2]/div[3]"
time.sleep(2)
driver.find_element_by_xpath(ship_xpath_3).click()
time.sleep(5)

reference_xpath = "//*[@id='fReferenceValue']"
time.sleep(5)
driver.find_element_by_id ("fReferenceValue").send_keys("%")
time.sleep(5)

custom_xpath = "//*[@id='customizedOutput']"
time.sleep(2)
driver.find_element_by_xpath(custom_xpath).click()
time.sleep(5)
driver.refresh()


# In[147]:


party = "//*[@id='myform']/div[2]/div/div/div[4]/div[1]/div[2]/div[2]/div[4]/div[1]/label"
time.sleep(5)
driver.find_element_by_xpath(party).click()
time.sleep(5)
html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)
track= "//*[@id='customSearchTrack']"
time.sleep(5)
driver.find_element_by_xpath(track).click()
time.sleep(12)

excel_1 = "//*[@id='myform']/div[3]/div[1]/div[2]/div[1]/div/span/img"
time.sleep(5)
driver.find_element_by_xpath(excel_1).click()
time.sleep(5)

excel_2 = "//*[@id='myform']/div[3]/div[1]/div[2]/div[2]/a[1]"
time.sleep(5)
driver.find_element_by_xpath(excel_2).click()
time.sleep(5)
driver.close()
driver.quit()

# In[148]:


Current_Date = datetime.datetime.today().strftime ('%y-%m-%d')
os.rename(r'C:\Processes\python_script\RPA_UPS\UPS_data\Party_infomation_data\Data\SearchResult.xlsx',r'C:\Processes\python_script\RPA_UPS\UPS_data\Party_infomation_data\Data\Party Information' + str(Current_Date) + '.xlsx')


# In[149]:


# In[ ]:



chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Container_tracking_event_data\\Data\\"}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_experimental_option("excludeSwitches", ["enable-logging"])
chromedriver = "C:/Processes/python_script/RPA_UPS/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)
driver.maximize_window()


# In[150]:


URL = "https://fgv.ups-scs.com/loginservicesfgv/logOn.nfdo"
driver.get (URL)
time.sleep(5)
driver.refresh()
login_xpath = "//*[@id='top']/div/div/div/ul/li[2]/a"
time.sleep(2)
driver.find_element_by_xpath(login_xpath).click()
time.sleep(2)

driver.find_element_by_id("signInName").send_keys("karak@hyper-pet.com")
time.sleep(2)
driver.find_element_by_id ("password").send_keys("Cosmicpet1315")
time.sleep(2)
driver.find_element_by_id("next").click()
time.sleep(5)
driver.refresh()
time.sleep(5)
Data_xpath = "//*[@id='navigation']/ul/li[3]/a"
time.sleep(2)
driver.find_element_by_xpath(Data_xpath).click()
time.sleep(5)

ship_xpath = "//*[@id='reference']/div[1]"
time.sleep(2)
driver.find_element_by_xpath(ship_xpath).click()
time.sleep(5)



html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)

# ship_xpath_3 = "/html/body/form/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div[4]/div/div/div[2]/div[3]"
# time.sleep(2)
# driver.find_element_by_xpath(ship_xpath_3).click()
# time.sleep(5)

reference_xpath = "//*[@id='fReferenceValue']"
time.sleep(5)
driver.find_element_by_id ("fReferenceValue").send_keys("%")
time.sleep(5)

custom_xpath = "//*[@id='customizedOutput']"
time.sleep(2)
driver.find_element_by_xpath(custom_xpath).click()
time.sleep(5)
driver.refresh()


# In[151]:


con_track = "//*[@id='myform']/div[2]/div/div/div[4]/div[1]/div[2]/div[2]/div[6]/div[1]/label"
time.sleep(5)
driver.find_element_by_xpath(party).click()
time.sleep(5)
html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)
track= "//*[@id='customSearchTrack']"
time.sleep(5)
driver.find_element_by_xpath(track).click()
time.sleep(12)

excel_1 = "//*[@id='myform']/div[3]/div[1]/div[2]/div[1]/div/span/img"
time.sleep(5)
driver.find_element_by_xpath(excel_1).click()
time.sleep(5)

excel_2 = "//*[@id='myform']/div[3]/div[1]/div[2]/div[2]/a[1]"
time.sleep(5)
driver.find_element_by_xpath(excel_2).click()
time.sleep(5)
driver.close()
driver.quit()

# In[152]:
Current_Date = datetime.datetime.today().strftime ('%y-%m-%d')
os.rename(r'C:\Processes\python_script\RPA_UPS\UPS_data\Container_tracking_event_data\Data\SearchResult.xlsx',r'C:\Processes\python_script\RPA_UPS\UPS_data\Container_tracking_event_data\Data\Container Tracking Events' + str(Current_Date) + '.xlsx')


# In[4]:






result = pd.read_csv("C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Container_tracking_event_data\\Data\\Total Container Tracking Events.csv", dtype='unicode')
for f in glob.glob("C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Container_tracking_event_data\\Data\\*.xlsx"):
    created = os.path.getctime(f)
    year,month,day,hour,minute,second=time.localtime(created)[:-3]
    file_creation_date = "%d-%02d-%02d "%(year,month,day)
    if file_creation_date != date.today():
        continue
    else:
        newfile = pd.read_excel(f,dtype=object)
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
result.to_csv('C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Container_tracking_event_data\\Data\\Total Container Tracking Events.csv',index= False) 


# In[7]:


result = pd.read_csv("C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\General_Shipment_data\\Data\\Total General Shipment Data.csv", dtype='unicode')
for f in glob.glob("C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\General_Shipment_data\\Data\\*.xlsx"):
    created = os.path.getctime(f)
    year,month,day,hour,minute,second=time.localtime(created)[:-3]
    file_creation_date = "%d-%02d-%02d "%(year,month,day)
    if file_creation_date != date.today():
        continue
    else:
        newfile = pd.read_excel(f,dtype=object)
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
result.to_csv('C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\General_Shipment_data\\Data\\Total General Shipment Data.csv',index= False) 


# In[8]:


result = pd.read_csv("C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Customer_references_data\Data\\Total Customer References.csv", dtype='unicode')
for f in glob.glob("C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Customer_references_data\\Data\\*.xlsx"):
    created = os.path.getctime(f)
    year,month,day,hour,minute,second=time.localtime(created)[:-3]
    file_creation_date = "%d-%02d-%02d "%(year,month,day)
    if file_creation_date != date.today():
        continue
    else:
        newfile = pd.read_excel(f,dtype=object)
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
result.to_csv('C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Customer_references_data\\Data\\Total Customer References.csv',index= False) 


# In[9]:


result = pd.read_csv("C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Ocean_container_information_data\Data\\Total Ocean Container Information.csv", dtype='unicode')
for f in glob.glob("C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Ocean_container_information_data\\Data\\*.xlsx"):
    created = os.path.getctime(f)
    year,month,day,hour,minute,second=time.localtime(created)[:-3]
    file_creation_date = "%d-%02d-%02d "%(year,month,day)
    if file_creation_date != date.today():
        continue
    else:
        newfile = pd.read_excel(f,dtype=object)
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
result.to_csv('C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Ocean_container_information_data\\Data\\Total Ocean Container Information.csv',index= False) 


# In[10]:


result = pd.read_csv("C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Party_infomation_data\Data\\Total Party Information.csv", dtype='unicode')
for f in glob.glob("C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Party_infomation_data\\Data\\*.xlsx"):
    created = os.path.getctime(f)
    year,month,day,hour,minute,second=time.localtime(created)[:-3]
    file_creation_date = "%d-%02d-%02d "%(year,month,day)
    if file_creation_date != date.today():
        continue
    else:
        newfile = pd.read_excel(f,dtype=object)
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


# In[11]:


result = pd.read_csv("C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Shipment_milestone_data\Data\\Total Shipment Milestone Events.csv", dtype='unicode')
for f in glob.glob("C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Shipment_milestone_data\\Data\\*.xlsx"):
    created = os.path.getctime(f)
    year,month,day,hour,minute,second=time.localtime(created)[:-3]
    file_creation_date = "%d-%02d-%02d "%(year,month,day)
    if file_creation_date != date.today():
        continue
    else:
        newfile = pd.read_excel(f,dtype=object)
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
result.to_csv('C:\\Processes\\python_script\\RPA_UPS\\UPS_data\\Shipment_milestone_data\\Data\\Total Shipment Milestone Events.csv',index= False) 


# In[13]:





# In[14]:




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















# In[15]:





# In[ ]:




