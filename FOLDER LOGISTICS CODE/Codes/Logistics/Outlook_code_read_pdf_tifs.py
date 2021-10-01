#!/usr/bin/env python
# coding: utf-8

# In[1]:


import multiprocessing
from multiprocessing import Pool
import pytesseract
from pdf2image import convert_from_path
import glob
import os
import time
import re
import shutil
from re import search


# In[2]:


# import pytesseract
# from pdf2image import convert_from_path
# import glob

# path = 'C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Sandbox\\'
# pdfs = glob.glob("C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Data\\*.pdf")
# for pdf_path in pdfs:
#     try:
#         pages = convert_from_path(pdf_path, 500,poppler_path = r"C:\Users\ChitraVenkata\Desktop\poppler-0.68.0\bin")
#     except:
#         continue
#     for pageNum,imgBlob in enumerate(pages):
#         pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\ChitraVenkata\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'
#         text = pytesseract.image_to_string(imgBlob,lang='eng')
#         filename = f'{pdf_path[:-4]}_page{pageNum}'
#         print(filename[112:])
#         filename = filename[112:]
# #         pdf_path = path + filename
# # #         pdf_path = path + pdf_path[112:]
#         with open(f'{path + filename }.txt', 'w') as the_file:
#             the_file.write(text)


# In[ ]:





# In[6]:


pdfs = glob.glob("C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Data\\*.pdf")
source_folder = pdfs
dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\MASH INTERNATIONAL"
path = 'C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Sandbox\\'
for pdf_path in pdfs:
    if os.path.getmtime(pdf_path) < time.time() - 1 * 24 * 60 * 60:  # 24h ago
        continue
    else:
        try:
            pages = convert_from_path(pdf_path, 500,poppler_path = r"C:\Users\ChitraVenkata\Desktop\poppler-0.68.0\bin")
        except:
            continue
        for pageNum,imgBlob in enumerate(pages):
            pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\ChitraVenkata\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'
            text = pytesseract.image_to_string(imgBlob,lang='eng')
            print(text)
            if search('MASH INTERNATIONAL', text.upper() , re.IGNORECASE) or search('208001', text.upper() , re.IGNORECASE) or search('208 001', text.upper() , re.IGNORECASE):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\MASH INTERNATIONAL"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('NANJING ORIENT ENTERPRISE LTD', text.upper() , re.IGNORECASE):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\NANJING ORIENT ENTERPRISE LTD"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
    #         elif search('UPS ASIA GROUP', text , re.IGNORECASE):
    #             dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\UPS ASIA GROUP"
    #             try:
    #                 shutil.move(pdf_path, dest_folder)
    #             except:
    #                 print('File exists')

            elif search('Nanjing Colorinpet ', text.upper() , re.IGNORECASE):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\NANJING COLORINPET TRANDING COMPANY"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('FUZHOU SUNLIGHT CAMPING PRODUCTS', text.upper() , re.IGNORECASE):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\FUZHOU SUNLIGHT CAMPING PRODUCTS"
                try:
                    shutil.copy(pdf_path, dest_folder)  
                except:
                    print('File exists')
            elif search('B&B MOLDED PRODUCTS', text.upper() , re.IGNORECASE):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\B&B MOLDED PRODUCTS"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('WEIHAI BESFASHION ', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\WEIHAI BESFASHION CO.,LTD"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('SHANGHAI TS TOYS', text.upper(), re.IGNORECASE )or  search('201109', text.upper(), re.IGNORECASE ) or search('TSTOYS', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\SHANGHAI TS TOYS"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('SHANGHAI CHONGXIN PET', text.upper(), re.IGNORECASE ) or search('SHANGHAI! CHONGXIN PET INDUSTRY', text.upper(), re.IGNORECASE ) or search('HUAXIN', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\SHANGHAI CHONGXIN PET"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('S & R MANUFACTURING', text.upper(), re.IGNORECASE ) or search('S&R MANUFACTURING', text.upper(), re.IGNORECASE):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\S&R MANUFACTURING"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('LIAOCHENG TRITON DIVING EQUIPMENT ', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\LIAOCHENG  TRITON DIVING EQUIPMENT CORP"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('KINCHLA', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\KINCHLA"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('HICHANCE', text.upper(), re.IGNORECASE ) or search('MONGKOK', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\HICHANCE INDUSTRIES LIMITED"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('HANZHOU BOY! PET ', text.upper(), re.IGNORECASE ) or search('HAGNZHOU BOY! ', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\HANZHOU BOY! PET PRODUCTS"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('ELDY PET FASHION', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\ELDY PET FASHION"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('CHANGSHU HUAMAO INTERNATIONAL ', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\CHANGSHU HUAMAO INTERNATIONAL TRADE COMPANY LTD"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('ALLANA', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\ALLANA"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')

    #             filename = f'{pdf_path[:-4]}_page{pageNum}'

            elif search('Y.K.INDUSTRIES', text.upper(), re.IGNORECASE ) or search('YK Industries',text.upper(), re.IGNORECASE )or search('KANPUR',text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\Y K INDUSTRIES"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('XIAMEN VELLAND GARMENTS', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\XIAMEN VELLAND GARMENTS CO., LTD"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('HUANGSHAN ROAD', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\TRITON DRIVING EQUIPMENT"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('TIGER POINT TRADING CORPORATION', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\TIGER POINT TRADING CORPORATION"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('TIANJIN DIBEI INTERNATIONAL TRADE', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\TIANJIN DIBEI INTERNATIONAL TRADE CO., LTD"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('TAN TIN DUC' , text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\TAN TIN DUC CO., LTD"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('SUZHOU HENGRUNDA', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\SUZHOU HENGRUNDA IMPORT & EXPORT CO., LTD"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('SHENZHEN MALL VANGUARD PAPER', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\SHENZHEN MALL VANGUARD PAPER"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('SHANGHAI GRAVIM INDUSTRIAL', text.upper(), re.IGNORECASE ) or search('SHANGHAT GRAVIM INDUSTRIAL', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\SHANGHAI GRAVIM INDUSTRIAL CO.,LTD"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('SHANGHAI JINWANG LUGGAGE TRAVEL PRODUCTS', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\SHANGHAI JINWANG LUGGAGE TRAVEL PRODUCTS CO., LTD"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')

            elif search('SANDU INDUSTRIAL AREA', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\SANDU INDUSTRIAL AREA"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('ROHEER INTERNATIONAL', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\ROHEER INTERNATIONAL"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('PET KRAFT', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\PET KRAFT"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('NINGBO GOODO TOOLS CO., LTD', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\NINGBO GOODO TOOLS CO., LTD"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('MARK & NUMBERS', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\MARK & NUMBERS"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('LIAOCHENG  TRITON DIVING EQUIPMENT', text.upper(), re.IGNORECASE ) or search('LIAOQCHENG TRITON DIVING EQUIPMENT', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\LIAOCHENG  TRITON DIVING EQUIPMENT CORP"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('LAUFER GROUP INTERNATIONAL', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\LAUFER GROUP INTERNATIONAL"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('JIANGSU HOLLY EVER-PRIME INTERNATIONAL', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\JIANGSU HOLLY EVER-PRIME INTERNATIONAL LTD"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('HIGH HOPE ZHONGTIAN CORPORATION', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\HIGH HOPE ZHONGTIAN CORPORATION"
                try:
                    shutil.move(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('GLOBAL EMINENCE', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\GLOBAL EMINENCE"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('FORTUNATE', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\FORTUNATE"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('AGRO FOOD INDUSTRIES', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\AGRO FOOD INDUSTRIES"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('BDP INTERNATIONAL', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\BDP INTERNATIONAL LTD"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('BEST-RUN TECHNOLOGY', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\BEST-RUN TECHNOLOGY"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('CHANGSHU HUAMAO INTERNATIONAL', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\CHANGSHU HUAMAO INTERNATIONAL TRADE"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('DONGYANG SOPOP ENAMEL DECORATION', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\DONGYANG SOPOP ENAMEL DECORATION MATERIAL CO., LTD"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('BRAL TAIWAN', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\BRAL TAIWAN CORPORATION"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('WHOLELUCKS INDUSTRIAL LIMITED', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\WHOLELUCKS INDUSTRIAL LIMITED"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('MEIJER DISTRIBUTION', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\MEIJER DISTRIBUTION"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('PORT ERIE PLASTICS', text.upper(), re.IGNORECASE ) or search('Troupe', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\PORT ERIE PLASTICS"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('WORLDFA EXPORTS PRIVATE LIMITED', text.upper(), re.IGNORECASE ) or search('449-450 ', text.upper(), re.IGNORECASE ) or search('131020',text.upper(), re.IGNORECASE):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\WORLDFA EXPORTS PRIVATE LIMITED"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('ROYAL INTERNATION INDUSTRY', text.upper(), re.IGNORECASE ) or search ('1555',text.upper(), re.IGNORECASE):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\ROYAL INTERNATION INDUSTRY"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
            elif search('ANHUI AIPET IMPORT', text.upper(), re.IGNORECASE ):
                dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\ANHUI AIPET IMPORT AND EXPORT"
                try:
                    shutil.copy(pdf_path, dest_folder)
                except:
                    print('File exists')
    #             print(filename[112:])
    #             filename = filename[112:]
    #             with open(f'{path + filename }.txt', 'w') as the_file:
    #                 the_file.write(text)


# In[7]:


# import pytesseract
# from pdf2image import convert_from_path
# import glob

# path = 'C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Sandbox\\'
# pdfs = glob.glob("C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Data\\*.tif")
# for pdf_path in pdfs:
#     for pageNum in enumerate(pdf_path):
#         pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\ChitraVenkata\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'
#         text = pytesseract.image_to_string(pdf_path,lang='eng')
#         filename = f'{pdf_path[:-4]}_page{pageNum}'
#         print(filename[112:])
#         filename = filename[112:]
# #         pdf_path = path + filename
# # #         pdf_path = path + pdf_path[112:]
# #         with open(f'{path + filename }.txt', 'w') as the_file:
# #             the_file.write(text)


# In[8]:


#tifs
path = 'C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Sandbox\\'
pdfs = glob.glob("C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Data\\*.tif")
for pdf_path in pdfs:
    if os.path.getmtime(pdf_path) < time.time() - 7 * 24 * 60 * 60:  # 24h ago
        continue
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\ChitraVenkata\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'
    text = pytesseract.image_to_string(pdf_path,lang='eng')
    print(text)
    if search('MASH INTERNATIONAL', text.upper() , re.IGNORECASE) or search('208001', text.upper() , re.IGNORECASE) or search('208 001', text.upper() , re.IGNORECASE):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\MASH INTERNATIONAL"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('NANJING ORIENT ENTERPRISE LTD', text.upper() , re.IGNORECASE):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\NANJING ORIENT ENTERPRISE LTD"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    #         elif search('UPS ASIA GROUP', text , re.IGNORECASE):
    #             dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\UPS ASIA GROUP"
    #             try:
    #                 shutil.move(pdf_path, dest_folder)
    #             except:
    #                 print('File exists')

    elif search('Nanjing Colorinpet ', text.upper() , re.IGNORECASE):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\NANJING COLORINPET TRANDING COMPANY"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('FUZHOU SUNLIGHT CAMPING PRODUCTS', text.upper() , re.IGNORECASE):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\FUZHOU SUNLIGHT CAMPING PRODUCTS"
        try:
            shutil.copy(pdf_path, dest_folder)  
        except:
            print('File exists')
    elif search('B&B MOLDED PRODUCTS', text.upper() , re.IGNORECASE):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\B&B MOLDED PRODUCTS"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('WEIHAI BESFASHION ', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\WEIHAI BESFASHION CO.,LTD"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('SHANGHAI TS TOYS', text.upper(), re.IGNORECASE )or  search('201109', text.upper(), re.IGNORECASE ) or search('TSTOYS', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\SHANGHAI TS TOYS"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('SHANGHAI CHONGXIN PET', text.upper(), re.IGNORECASE ) or search('SHANGHAI! CHONGXIN PET INDUSTRY', text.upper(), re.IGNORECASE ) or search('HUAXIN', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\SHANGHAI CHONGXIN PET"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('S & R MANUFACTURING', text.upper(), re.IGNORECASE ) or search('S&R MANUFACTURING', text.upper(), re.IGNORECASE):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\S&R MANUFACTURING"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('LIAOCHENG TRITON DIVING EQUIPMENT ', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\LIAOCHENG  TRITON DIVING EQUIPMENT CORP"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('KINCHLA', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\KINCHLA"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('HICHANCE', text.upper(), re.IGNORECASE ) or search('MONGKOK', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\HICHANCE INDUSTRIES LIMITED"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('HANZHOU BOY! PET ', text.upper(), re.IGNORECASE ) or search('HAGNZHOU BOY! ', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\HANZHOU BOY! PET PRODUCTS"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('ELDY PET FASHION', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\ELDY PET FASHION"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('CHANGSHU HUAMAO INTERNATIONAL ', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\CHANGSHU HUAMAO INTERNATIONAL TRADE COMPANY LTD"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('ALLANA', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\ALLANA"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')

    #             filename = f'{pdf_path[:-4]}_page{pageNum}'

    elif search('Y.K.INDUSTRIES', text.upper(), re.IGNORECASE ) or search('YK Industries',text.upper(), re.IGNORECASE )or search('KANPUR',text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\Y K INDUSTRIES"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('XIAMEN VELLAND GARMENTS', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\XIAMEN VELLAND GARMENTS CO., LTD"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('HUANGSHAN ROAD', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\TRITON DRIVING EQUIPMENT"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('TIGER POINT TRADING CORPORATION', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\TIGER POINT TRADING CORPORATION"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('TIANJIN DIBEI INTERNATIONAL TRADE', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\TIANJIN DIBEI INTERNATIONAL TRADE CO., LTD"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('TAN TIN DUC' , text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\TAN TIN DUC CO., LTD"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('SUZHOU HENGRUNDA', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\SUZHOU HENGRUNDA IMPORT & EXPORT CO., LTD"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('SHENZHEN MALL VANGUARD PAPER', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\SHENZHEN MALL VANGUARD PAPER"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('SHANGHAI GRAVIM INDUSTRIAL', text.upper(), re.IGNORECASE ) or search('SHANGHAT GRAVIM INDUSTRIAL', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\SHANGHAI GRAVIM INDUSTRIAL CO.,LTD"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('SHANGHAI JINWANG LUGGAGE TRAVEL PRODUCTS', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\SHANGHAI JINWANG LUGGAGE TRAVEL PRODUCTS CO., LTD"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')

    elif search('SANDU INDUSTRIAL AREA', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\SANDU INDUSTRIAL AREA"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('ROHEER INTERNATIONAL', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\ROHEER INTERNATIONAL"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('PET KRAFT', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\PET KRAFT"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('NINGBO GOODO TOOLS CO., LTD', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\NINGBO GOODO TOOLS CO., LTD"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('MARK & NUMBERS', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\MARK & NUMBERS"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('LIAOCHENG  TRITON DIVING EQUIPMENT', text.upper(), re.IGNORECASE ) or search('LIAOQCHENG TRITON DIVING EQUIPMENT', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\LIAOCHENG  TRITON DIVING EQUIPMENT CORP"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('LAUFER GROUP INTERNATIONAL', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\LAUFER GROUP INTERNATIONAL"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('JIANGSU HOLLY EVER-PRIME INTERNATIONAL', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\JIANGSU HOLLY EVER-PRIME INTERNATIONAL LTD"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('HIGH HOPE ZHONGTIAN CORPORATION', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\HIGH HOPE ZHONGTIAN CORPORATION"
        try:
            shutil.move(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('GLOBAL EMINENCE', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\GLOBAL EMINENCE"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('FORTUNATE', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\FORTUNATE"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('AGRO FOOD INDUSTRIES', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\AGRO FOOD INDUSTRIES"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('BDP INTERNATIONAL', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\BDP INTERNATIONAL LTD"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('BEST-RUN TECHNOLOGY', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\BEST-RUN TECHNOLOGY"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('CHANGSHU HUAMAO INTERNATIONAL', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\CHANGSHU HUAMAO INTERNATIONAL TRADE"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('DONGYANG SOPOP ENAMEL DECORATION', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\DONGYANG SOPOP ENAMEL DECORATION MATERIAL CO., LTD"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('BRAL TAIWAN', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\BRAL TAIWAN CORPORATION"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('WHOLELUCKS INDUSTRIAL LIMITED', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\WHOLELUCKS INDUSTRIAL LIMITED"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('MEIJER DISTRIBUTION', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\MEIJER DISTRIBUTION"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('PORT ERIE PLASTICS', text.upper(), re.IGNORECASE ) or search('Troupe', text.upper(), re.IGNORECASE ):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\PORT ERIE PLASTICS"
        try:
                    shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('WORLDFA EXPORTS PRIVATE LIMITED', text.upper(), re.IGNORECASE ) or search('449-450 ', text.upper(), re.IGNORECASE ) or search('131020',text.upper(), re.IGNORECASE):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\WORLDFA EXPORTS PRIVATE LIMITED"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
    elif search('ROYAL INTERNATION INDUSTRY', text.upper(), re.IGNORECASE ) or search ('1555',text.upper(), re.IGNORECASE):
        dest_folder = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\ROYAL INTERNATION INDUSTRY"
        try:
            shutil.copy(pdf_path, dest_folder)
        except:
            print('File exists')
#     filename = f'{file[:-4]}'
# #     print(filename[112:])
#     filename = filename[112:]
# # #         pdf_path = path + pdf_path[112:]
#     with open(f'{path + filename }.txt', 'w') as the_file:
#         the_file.write(text)


# In[ ]:





# In[ ]:




