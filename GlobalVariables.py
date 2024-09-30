from pathlib import Path
import os
paths = {}
# 全局变量文件
# 指定Excel 文件夹路径
excel_folder_name = Path('xlsx')
# 指定csv 文件路径
csv_folder_name = Path('csv')
# 指定json 文件路径
json_folder_name = Path('json')
# 指定xml 文件路径
xml_folder_name = Path('xml')
# 指定lua文件夹路径
lua_folder_name = Path('lua')
# 指定bytes文件路径
bytes_folder_name = Path('bytes')

# 指定 日志文件路径

def get_all_paths():
    root = os.getcwd()
    paths['xlsx'] = os.path.join(root, excel_folder_name)
    paths['csv'] = os.path.join(root, csv_folder_name)
    paths['xml'] = os.path.join(root, xml_folder_name)
    paths['json'] = os.path.join(root, json_folder_name)
    paths['lua'] = os.path.join(root, lua_folder_name)
    paths['bytes'] = os.path.join(root, bytes_folder_name)
    return paths
