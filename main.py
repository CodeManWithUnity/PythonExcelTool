import pandas as pd
import GlobalVariables as gv
from pathlib import Path
from start import init_print
import xml.etree.ElementTree as ET
from openpyxl import load_workbook
import colorama
from colorama import Fore, Back, Style
import convert
import os

excel_file_path = gv.excel_folder_name
excelfile_path_list= []


# 项目菜单函数
def start(user_input):
    colorama.init()
    if user_input.isdigit():
        if user_input == '1':
            convert.convert_xlsx_to_csv()
        elif user_input == '2':
            convert.convert_xlsx_to_json()
        elif user_input == '3':
            convert.convert_xlsx_to_xml()
            pass
        elif user_input == '4':
            pass
        elif user_input == '5':
            pass
        elif user_input == '6':
            os.system('cmd /c exit')
        else:
            print(Fore.RED + '请输入一个正确的数字' + Style.RESET_ALL)
            init_print()
    else:
        print(Fore.RED +'请输入一个数字'+ Style.RESET_ALL)
        init_print()

