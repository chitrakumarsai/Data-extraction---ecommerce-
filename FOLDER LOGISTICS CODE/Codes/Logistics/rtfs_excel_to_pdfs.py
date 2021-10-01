#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sys
import os,os.path
import comtypes.client
import glob
import os
import time
import re
import shutil
from re import search
import win32com.client as win32
import schedule
import datetime as dt
def rtfexcel():
    wdFormatPDF = 17
    try:
        pdfs = glob.glob("C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Data\\*.rtf")

        dest = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Data\\rtfs"
        for pdf_path in pdfs:
            if os.path.getmtime(input_dir+'\\'+ file) < time.time() - 7 * 24 * 60 * 60:
                continue
            else:
                shutil.copy(pdf_path, dest)

        input_dir = 'C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Data\\rtfs\\'
        output_dir = 'C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Data\\'

        for subdir, dirs, files in os.walk(input_dir):
            try:
                for file in files:
                    if os.path.getmtime(input_dir+'\\'+ file) < time.time() - 7 * 24 * 60 * 60:
                        continue
                    else:
                        in_file = os.path.join(subdir, file)
                        output_file = file.split('.')[0]
                        out_file = output_dir+output_file+'.pdf'
                        word = comtypes.client.CreateObject('Word.Application')

                        doc = word.Documents.Open(in_file)
                        try:
                            doc.SaveAs(out_file, FileFormat=wdFormatPDF)
                        except Exception as e:
                            print("Failed to convert")
                            print(str(e))
                        finally:
                            doc.Close()
                            word.Quit()
            except:
                print("File not found")
    except:
        print("No RTF files")


    xls = glob.glob("C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Data\\*.xls")
    for xlsx in xls:
        fname = xlsx
        excel = win32.gencache.EnsureDispatch('Excel.Application')
        wb = excel.Workbooks.Open(fname)

        wb.SaveAs(fname+"x", FileFormat = 51)    #FileFormat = 51 is for .xlsx extension
        wb.Close()                               #FileFormat = 56 is for .xls extension
        excel.Application.Quit()
        os.remove(xlsx)

    pdfs = glob.glob("C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Data\\*.xlsx")

    dest = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Data\\excel"
    for file in pdfs:
        if os.path.getmtime(file) < time.time() - 7 * 24 * 60 * 60:
            continue
        else:
            try:
                shutil.move(file, dest)
            except:
                print("File exists")

    input_dir = 'C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Data\\excel\\'
    output_dir = 'C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Data\\'

    for subdir, dirs, files in os.walk(input_dir):
        try:
            for file in files:
                if os.path.getmtime(input_dir+'\\'+ file) < time.time() - 7 * 24 * 60 * 60:
                    continue
                else:
                    in_file = os.path.join(subdir, file)
                    output_file = file.split('.')[0]
                    out_file = output_dir+output_file+"_"+'.pdf'
                    excel = comtypes.client.CreateObject('Excel.Application')

                    doc = excel.Workbooks.Open(in_file)
                    try:
                        doc.SaveAs(out_file, FileFormat=57)
                    except Exception as e:
                        print("Failed to convert")
                        print(str(e))
                    finally:
                        doc.Close()
                        excel.Quit()
        except:
            print("File not found")


        
        
# from win32com import client
# import win32api
# import pathlib

# ### pip install pypiwin32 if module not found

# excel_file = "pdf_me.xlsx"
# pdf_file = "pdf_me.pdf"
# excel_path = str(pathlib.Path.cwd() / excel_file)
# pdf_path = str(pathlib.Path.cwd() / pdf_file)

# excel = client.DispatchEx("Excel.Application")
# excel.Visible = 0

# wb = excel.Workbooks.Open(excel_path)
# ws = wb.Worksheets[1]

# try:
#     wb.SaveAs(pdf_path, FileFormat=57)
# except Exception as e:
#     print("Failed to convert")
#     print(str(e))
# finally:
#     wb.Close()
#     excel.Quit()






# import openpyxl
# import sys
# import os,os.path
# import comtypes.client
# import glob
# import os
# import time
# import shutil

# def wordfinder(searchString):
#     for i in range(1, ws.max_row + 1):
#         for j in range(1, ws.max_column + 1):
#             if searchString == ws.cell(i,j).value:
#                 return True   

# xlsx = glob.glob("C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Data\\*.xlsx")
# for file in xlsx:
#     wb = openpyxl.load_workbook(file)
#     ws = wb.active
# #     if wordfinder("Nanjing Colorinpet Trading Company"):
# #         dest = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\NANJING COLORINPET TRANDING COMPANY"
# #         shutil.copy(file, dest)
# #     if wordfinder("FUZHOU SUNLIGHT CAMPING PRODUCTS CO.,LTD."):
# #         dest = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\FUZHOU SUNLIGHT CAMPING PRODUCTS"
# #         shutil.copy(file, dest)
# #     elif wordfinder("SUNCAMP INTERNATIONAL LTD."):
# #         dest = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\SUN CAMP INTERNATIONAL"
# #         shutil.copy(file, dest)       
#     if wordfinder("SHANGHAI TS TOYS CO.,LTD"):
#         dest = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\SHANGHAI TS TOYS"
#         shutil.copy(file, dest)    
#     elif wordfinder("Activity by Destination Report - Laufer Group International"):
#         dest = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\LAUFER GROUP INTERNATIONAL"
#         shutil.copy(file, dest)  
#     elif wordfinder("HICHANCE INDUSTRIES LIMITED"):
#         dest = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\HICHANCE INDUSTRIES LIMITED"
#         shutil.copy(file, dest) 
# #     elif wordfinder("Worldfa Exports"):
# #         dest = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\WORLDFA EXPORTS PRIVATE LIMITED"
# #         shutil.copy(file, dest) 
# #     elif wordfinder("Bral Taiwan Corporation"):
# #         dest = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\BRAL TAIWAN CORPORATION"
# #         shutil.copy(file, dest)
# #     elif wordfinder("HOTON PET SUPPLIER"):
# #         dest = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\HOTON PET SUPPLIER CO., LTD"
# #         shutil.copy(file, dest)
# #     elif wordfinder("GLOBAL EMINENCE"):
# #         dest = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\GLOBAL EMINENCE"
# #         shutil.copy(file, dest)
# #     elif wordfinder("WEIHAI BESFASHION"):
# #         dest = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\WEIHAI BESFASHION CO.,LTD"
# #         shutil.copy(file, dest)
# #     elif wordfinder("Liaocheng Triton Diving Equipment"):
# #         dest = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\TRITON DRIVING EQUIPMENT"
# #         shutil.copy(file, dest)
# #     elif wordfinder("Dongyang Sopop Enamel Decoration"):
# #         dest = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\DONGYANG SOPOP ENAMEL DECORATION MATERIAL CO., LTD"
# #         shutil.copy(file, dest)
# #     elif wordfinder("Royal International Industrial"):
# #         dest = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\ROYAL INTERNATION INDUSTRY"
# #         shutil.copy(file, dest)
# #     elif wordfinder("HANGZHOU BOYI PET"):
# #         dest = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\HANZHOU BOY! PET PRODUCTS"
# #         shutil.copy(file, dest)
# #     elif wordfinder("SUZHOU HENGRUNDA IMPORT & EXPORT"):
# #         dest = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\SUZHOU HENGRUNDA IMPORT & EXPORT CO., LTD"
# #         shutil.copy(file, dest)
# #     elif wordfinder("Xiamen Velland Garments"):
# #         dest = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\XIAMEN VELLAND GARMENTS CO., LTD"
# #         shutil.copy(file, dest)
# #     elif wordfinder("ELDY PET FASHION"):
# #         dest = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\ELDY PET FASHION"
# #         shutil.copy(file, dest)
# #     elif wordfinder("BEST-RUN TECHNOLOGY"):
# #         dest = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\BEST-RUN TECHNOLOGY"
# #         shutil.copy(file, dest)
# #     elif wordfinder("TIANJIN DIBEI INTERNATIONAL"):
# #         dest = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\TIANJIN DIBEI INTERNATIONAL TRADE CO., LTD"
# #         shutil.copy(file, dest)
# #     elif wordfinder("Changshu Huamao International"):
# #         dest = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\CHANGSHU HUAMAO INTERNATIONAL TRADE"
# #         shutil.copy(file, dest)
# #     elif wordfinder("Shanghai Jinwang Luggage"):
# #         dest = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\SHANGHAI JINWANG LUGGAGE TRAVEL PRODUCTS CO., LTD"
# #         shutil.copy(file, dest)
# #     elif wordfinder("Shanghai Jinwang Luggage"):
# #         dest = "C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Factories\\SHANGHAI JINWANG LUGGAGE TRAVEL PRODUCTS CO., LTD"
# #         shutil.copy(file, dest)
        
   
# input_dir = 'C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Data\\excel\\'
# output_dir = 'C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Data\\'

# for subdir, dirs, files in os.walk(input_dir):
#     for file in files:
#         in_file = os.path.join(subdir, file)
#         output_file = file.split('.')[0]
#         out_file = output_dir+output_file+'.pdf'
#         excel = comtypes.client.CreateObject('Excel.Application')

#         doc = excel.Workbooks.Open(in_file)
#         doc.SaveAs(out_file, FileFormat=57)
#         doc.Close()
#         excel.Quit()


# In[5]:


rtfexcel()
#schedule.every().day.at("08:27").do(rtfexcel)


# In[ ]:


# while True: 
#     schedule.run_pending() 
#     time.sleep(1)


# In[3]:


input_dir = 'C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Data\\excel\\'
output_dir = 'C:\\Users\\ChitraVenkata\\Dropbox (Cosmic Pet-Business)\\Cosmic - Reporting\\Processes\\Chitra_Working\\Logistics\\Data\\'

for subdir, dirs, files in os.walk(input_dir):
    for file in files:
        if os.path.getmtime(input_dir+'\\'+ file) < time.time() - 7 * 24 * 60 * 60:
            print(file)
            continue
        else:
            print(file)
#             in_file = os.path.join(subdir, file)
#             output_file = file.split('.')[0]
#             out_file = output_dir+output_file+'.pdf'
#             excel = comtypes.client.CreateObject('Excel.Application')
#             doc = excel.Workbooks.Open(in_file)
#             try:
#                 doc.SaveAs(out_file, FileFormat=57)
#             except Exception as e:
#                 print("Failed to convert")
#                 print(str(e))
#             finally:
#                 doc.Close()
#                 excel.Quit()


# In[ ]:




