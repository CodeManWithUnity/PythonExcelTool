import pandas as pd
import GlobalVariables as gv
from pathlib import Path
from start import init_print
import xml.etree.ElementTree as ET
from openpyxl import load_workbook
import glob
import colorama
from colorama import Fore, Back, Style
import utils
import os

excel_file_path = gv.excel_folder_name
excelfile_path_list= []


# 项目菜单函数
def start(user_input):
    colorama.init()
    if user_input.isdigit():
        if user_input == '1':
            convert_xlsx_to_csv()
        elif user_input == '2':
            convert_xlsx_to_json()
        elif user_input == '3':
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


# 获取当前目录下的所有excel文件
def get_all_excel_files():
    excelfile_path_list = glob.glob(f'{excel_file_path}/*.xlsx')
    excelfile_path_list = utils.remove_file(excelfile_path_list,'~$')
    return excelfile_path_list

# 转成csv文件
def convert_xlsx_to_csv():
    excelfile_path_list = get_all_excel_files()
    for filename in excelfile_path_list:
        xls = pd.ExcelFile(filename)
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name)
            csv_filename = os.path.splitext(os.path.basename(filename))[0]
            csv_filename = f"{csv_filename}_{sheet_name}.csv"
            csv_path = os.path.join(gv.csv_folder_name, csv_filename)
            df.to_csv(csv_path, index=False)
            print(Fore.GREEN + f"{csv_filename} 转换csv完成！" + Style.RESET_ALL)
# 转成json文件
def convert_xlsx_to_json():
    excelfile_path_list = get_all_excel_files()
    for filename in excelfile_path_list:
        xls = pd.ExcelFile(filename)
        combined_df = pd.DataFrame()
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name)
            combined_df = pd.concat([combined_df, df], ignore_index=True)
        json_data = combined_df.to_json(orient='records', force_ascii=False, lines=False)
        json_filename =f"{os.path.splitext(os.path.basename(filename))[0]}.json"
        json_path = os.path.join(gv.json_folder_name, json_filename)
        # 保存为JSON文件
        with open(json_path, 'w', encoding='utf-8') as json_file:
            json_file.write(json_data)
# 转成xml文件


