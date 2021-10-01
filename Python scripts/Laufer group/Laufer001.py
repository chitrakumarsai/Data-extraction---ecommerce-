#!/usr/bin/env python
# coding: utf-8

# In[26]:


from selenium import webdriver
import time
import pandas as pd
import glob
import os.path, time
import datetime
from datetime import date


# In[17]:



chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "C:\\Processes\\python_script\\Laufer group\\Data\\active_ocean_bookings\\"}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_experimental_option("excludeSwitches", ["enable-logging"])
chromedriver = "C:/Processes/python_script/Laufer group/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)
driver.maximize_window()


# In[18]:


URL = "https://peerplus.laufer.com/PeerPlus/login"
driver.get (URL)
time.sleep(5)


# In[19]:


driver.find_element_by_id("username").send_keys("chitrav@cosmicpet.com")
driver.find_element_by_id ("password").send_keys("Akuti19eza!")


# In[20]:


driver.find_element_by_id("loginSubmit").click()
time.sleep(5)


# In[21]:


dashboard_Xpath = "/html/body/app-root/div/div/div/div/div/div/bookings-dashboard/pp-dashboard/div/div/div/pp-widget-column[1]/pp-widget[3]/div/div[2]/div/div/div[2]/bookings-ocean/div[1]/div/pp-grid/div[1]/div[3]/div/button[2]"
driver.find_element_by_xpath(dashboard_Xpath).click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='bs']/li[1]/a").click()
driver.close()
driver.quit()

# In[22]:


chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "C:\\Processes\\python_script\\Laufer group\\Data\\container\\"}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_experimental_option("excludeSwitches", ["enable-logging"])
chromedriver = "C:/Processes/python_script/Laufer group/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)
driver.maximize_window()
URL = "https://peerplus.laufer.com/PeerPlus/login"
driver.get (URL)
time.sleep(5)
driver.find_element_by_id("username").send_keys("chitrav@cosmicpet.com")
driver.find_element_by_id ("password").send_keys("Akuti19eza!")
driver.find_element_by_id("loginSubmit").click()
time.sleep(5)
container_Xpath = "/html/body/app-root/div/div/div/div/div/div/bookings-dashboard/ul/li[3]/a"
driver.find_element_by_xpath(container_Xpath).click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/app-root/div/div/div/div/div/div/containers-dashboard/pp-dashboard/div/div/div/pp-widget-column[1]/pp-widget[2]/div/div[2]/div/div/div[2]/app-containers-locator/div/div/pp-grid/div[1]/div/div/button").click()
time.sleep(5)
driver.close()
driver.quit()

# In[23]:


chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "C:\\Processes\\python_script\\Laufer group\\Data\\shipment\\"}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_experimental_option("excludeSwitches", ["enable-logging"])
chromedriver = "C:/Processes/python_script/Laufer group/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)
driver.maximize_window()
URL = "https://peerplus.laufer.com/PeerPlus/login"
driver.get (URL)
time.sleep(5)
driver.find_element_by_id("username").send_keys("chitrav@cosmicpet.com")
driver.find_element_by_id ("password").send_keys("Akuti19eza!")
driver.find_element_by_id("loginSubmit").click()
time.sleep(5)
shipments_Xpath ="/html/body/app-root/div/div/div/div/div/div/bookings-dashboard/ul/li[2]/a"
driver.find_element_by_xpath(shipments_Xpath).click()
time.sleep(5)
# # Documents and customer entry
driver.find_element_by_xpath("/html/body/app-root/div/div/div/div/div/div/shipments-dashboard/pp-dashboard/div/div/div/pp-widget-column[1]/pp-widget/div/div[2]/div/div/div[2]/app-shipments-locator/div/div/pp-grid/div[1]/div/div/button").click()
time.sleep(5)
driver.close()
driver.quit()

# In[24]:


chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "C:\\Processes\\python_script\\Laufer group\\Data\\PO\\"}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_experimental_option("excludeSwitches", ["enable-logging"])
chromedriver = "C:/Processes/python_script/Laufer group/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)
driver.maximize_window()
URL = "https://peerplus.laufer.com/PeerPlus/login"
driver.get (URL)
time.sleep(5)
driver.find_element_by_id("username").send_keys("chitrav@cosmicpet.com")
driver.find_element_by_id ("password").send_keys("Akuti19eza!")
driver.find_element_by_id("loginSubmit").click()
time.sleep(5)

PO_xpath = "//*[@id='pow']/li[1]/a"
driver.find_element_by_xpath(PO_xpath).click()
time.sleep(5)
# # Documents and customer entry
driver.find_element_by_xpath("/html/body/app-root/div/div/div/div/div/div/app-posummary-header/pp-tab/div/div/posummary/div/div/pp-grid/div[1]/div/div/button").click()
time.sleep(5)
driver.close()
driver.quit()

# In[ ]:





# In[25]:


chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "C:\\Processes\\python_script\\Laufer group\\Data\\ISF_filing_summary\\"}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_experimental_option("excludeSwitches", ["enable-logging"])
chromedriver = "C:/Processes/python_script/Laufer group/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)
driver.maximize_window()
URL = "https://peerplus.laufer.com/PeerPlus/login"
driver.get (URL)
time.sleep(5)
driver.find_element_by_id("username").send_keys("chitrav@cosmicpet.com")
driver.find_element_by_id ("password").send_keys("Akuti19eza!")
driver.find_element_by_id("loginSubmit").click()
time.sleep(5)
EDI_PO_Xpath = "//*[@id='isf']/li/a"
driver.find_element_by_xpath(EDI_PO_Xpath).click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/app-root/div/div/div/div/div/div/isf-filing-summary/pp-tab/div/div/div/div[3]/pp-grid/div[1]/div[3]/div/button").click()
time.sleep(5)
driver.close()
driver.quit()

# In[92]:


all_data = pd.read_csv("C:\\Processes\\python_script\\Laufer group\\Data\\active_ocean_bookings\\combined_data\\Total_active_ocean_bookings.csv")
for f in glob.glob("C:\\Processes\\python_script\\Laufer group\\Data\\active_ocean_bookings\\*.xlsx"):
    created = os.path.getctime(f)
    year,month,day,hour,minute,second=time.localtime(created)[:-3]
    file_creation_date = "%d-%02d-%02d "%(year,month,day)
    if file_creation_date != date.today():
        continue
    else:
        df = pd.read_excel(f, skiprows =3,delimiter=',')
        df.dropna(axis=1, how = "all", inplace = True)
        df.drop(['Unnamed: 35'], axis=1, inplace = True)
        all_data = all_data.append(df,ignore_index=True)
all_data = all_data.drop_duplicates()
all_data.to_csv("C:\\Processes\\python_script\\Laufer group\\Data\\active_ocean_bookings\\combined_data\\Total_active_ocean_bookings.csv",index=False)  


# In[73]:


all_data = pd.read_csv("C:\\Processes\\python_script\\Laufer group\\Data\\container\\combined_data\\Total_containers.csv")
for f in glob.glob("C:\\Processes\\python_script\\Laufer group\\Data\\container\\*.xlsx"):
    created = os.path.getctime(f)
    year,month,day,hour,minute,second=time.localtime(created)[:-3]
    file_creation_date = "%d-%02d-%02d "%(year,month,day)
    if file_creation_date != date.today():
        continue
    else:
        df = pd.read_excel(f, skiprows =3,delimiter=',')
        df.dropna(axis=1, how = "all" , inplace = True)
        df.drop(['Unnamed: 6','Unnamed: 38'], axis=1, inplace = True)
    #     df.rename(columns={"Unnamed: 35": "PO Numbers"}, inplace = True)
        all_data = all_data.append(df,ignore_index=True)
all_data = all_data.drop_duplicates()
all_data.to_csv("C:\\Processes\\python_script\\Laufer group\\Data\\container\\combined_data\\Total_containers.csv",index=False)  


# In[82]:


all_data = pd.read_csv("C:\\Processes\\python_script\\Laufer group\\Data\\ISF_filing_summary\\combined_data\\Total_ISF_summary.csv")
for f in glob.glob("C:\\Processes\\python_script\\Laufer group\\Data\\ISF_filing_summary\\*.xlsx"):
    created = os.path.getctime(f)
    year,month,day,hour,minute,second=time.localtime(created)[:-3]
    file_creation_date = "%d-%02d-%02d "%(year,month,day)
    if file_creation_date != date.today():
        continue
    else:
        df = pd.read_excel(f, skiprows =3,delimiter=',')
        df.dropna(axis=1, how = "all", inplace = True)
    #     df.drop(['Unnamed: 6','Unnamed: 38'], axis=1, inplace = True)
    #     df.rename(columns={"Unnamed: 35": "PO Numbers"}, inplace = True)
        all_data = all_data.append(df,ignore_index=True)
all_data = all_data.drop_duplicates()
all_data.to_csv("C:\\Processes\\python_script\\Laufer group\\Data\\ISF_filing_summary\\combined_data\\Total_ISF_summary.csv",index=False)  


# In[83]:


# In[86]:


all_data = pd.read_csv("C:\\Processes\\python_script\\Laufer group\\Data\PO\\combined_data\\Total_PO.csv")
for f in glob.glob("C:\\Processes\\python_script\\Laufer group\\Data\\PO\\*.xlsx"):
    created = os.path.getctime(f)
    year,month,day,hour,minute,second=time.localtime(created)[:-3]
    file_creation_date = "%d-%02d-%02d "%(year,month,day)
    if file_creation_date != date.today():
        continue
    else:
        df = pd.read_excel(f, skiprows =3,delimiter=',')
        df.dropna(axis=1, how = "all", inplace = True)
        df.drop(['Unnamed: 25','Unnamed: 26'], axis=1, inplace = True)
    #     df.rename(columns={"Unnamed: 35": "PO Numbers"}, inplace = True)
        all_data = all_data.append(df,ignore_index=True)
all_data = all_data.drop_duplicates()
all_data.to_csv("C:\\Processes\\python_script\\Laufer group\\Data\PO\\combined_data\\Total_PO.csv",index=False)  


# In[89]:


all_data = pd.read_csv("C:\\Processes\\python_script\\Laufer group\\Data\shipment\\combined_data\\Total_Shipment.csv")
for f in glob.glob("C:\\Processes\\python_script\\Laufer group\\Data\\shipment\\*.xlsx"):
    created = os.path.getctime(f)
    year,month,day,hour,minute,second=time.localtime(created)[:-3]
    file_creation_date = "%d-%02d-%02d "%(year,month,day)
    if file_creation_date != date.today():
        continue
    else:
        df = pd.read_excel(f, skiprows =3,delimiter=',')
        df.dropna(axis=1, how = "all", inplace = True)
        df.drop(['Unnamed: 3','Unnamed: 36'], axis=1, inplace = True)
    #     df.rename(columns={"Unnamed: 35": "PO Numbers"}, inplace = True)
        all_data = all_data.append(df,ignore_index=True)
all_data = all_data.drop_duplicates()
all_data.to_csv("C:\\Processes\\python_script\\Laufer group\\Data\shipment\\combined_data\\Total_Shipment.csv",index=False)  


# In[ ]:





# In[ ]:





# In[ ]:




