#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os
import schedule
import time
from datetime import date
import IPython
## FILE TO SEND AND ITS PATH
def customer_revenue():
    today = date.today()
    filename = 'Customer Data.xlsx'
    SourcePathName  = 'C:/Processes/python_script/Customer_revenue_data/' + filename 

    msg = MIMEMultipart()
    msg['From'] = 'chitrav@cosmicpet.com'
    msg['To'] = 'chitrav@cosmicpet.com'
    msg['Subject'] = 'Customer Revenue Data'
    body = 'Hello, Please find the attached which is the customer data/Revenue report.'
    msg.attach(MIMEText(body, 'plain'))

    ## ATTACHMENT PART OF THE CODE IS HERE
    attachment = open(SourcePathName, 'rb')
    part = MIMEBase('application', "octet-stream")
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)

    server = smtplib.SMTP('smtp.office365.com', 587)  ### put your relevant SMTP here
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('chitrav@cosmicpet.com', 'Akuti19eza!')  ### if applicable
    server.send_message(msg)
    # server.stoptls()
    server.quit()

    #IPython.Application.instance().kernel.do_shutdown(True)


# In[ ]:


# schedule.every().day.at("07:45").do(customer_revenue)
# while True: 
#     schedule.run_pending()    
#     time.sleep(1)


# In[ ]:


customer_revenue()


# In[ ]:





# In[ ]:




