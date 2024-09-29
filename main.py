import pandas as pd
import GlobalVariables as gv
from pathlib import Path
from start import init_print
import colorama
from colorama import Fore, Back, Style
import os

excel_file_path = gv.excel_folder_name
excelfile_path_list= []



def start(user_input):
    colorama.init()
    if user_input.isdigit():
        if user_input == '1':

            pass
        elif user_input == '2':
            pass
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





#读取excel文件夹下的所有文件并添加到容器列表中
def get_file_path():
    for root,dirs,files in os.walk(excel_file_path):
        for file in files:
            file_path = os.path.join(root,file)
            excelfile_path_list.append(file_path)
    for path in excelfile_path_list:
        print(path)
