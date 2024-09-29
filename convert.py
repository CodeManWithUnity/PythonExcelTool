import utils
import pandas as pd
import os
from colorama import Fore, Back, Style
import GlobalVariables as gv
# 转成csv文件
def convert_xlsx_to_csv():
    excelfile_path_list = utils.get_all_excel_files()
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
    excelfile_path_list = utils.get_all_excel_files()
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
def convert_xlsx_to_xml():
    pass


