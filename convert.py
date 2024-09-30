import utils
import pandas as pd
import xlrd
import os
from colorama import Fore, Back, Style
import GlobalVariables as gv
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import json
import start as st
# 转成csv文件
def convert_xlsx_to_csv(isall = False):
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
    if not isall:
        st.init_print()
# 转成json
def convert_xlsx_to_json(isall = False):
    excelfile_path_list = utils.get_all_excel_files()
    for filename in excelfile_path_list:
        xls = pd.ExcelFile(filename)
        
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name)
            
            # 将DataFrame转换为Python对象(字典列表)
            data = df.to_dict(orient='records')
            
            # 使用json.dumps()将Python对象转换为格式化的JSON字符串
            json_data = json.dumps(data, ensure_ascii=False, indent=4)
            
            json_filename = f"{os.path.splitext(os.path.basename(filename))[0]}_{sheet_name}.json"
            json_path = os.path.join(gv.json_folder_name, json_filename)
            
            # 将格式化后的JSON字符串写入文件
            with open(json_path, 'w', encoding='utf-8') as json_file:
                json_file.write(json_data)
            
            print(Fore.GREEN + f"{json_path} 转换json完成!" + Style.RESET_ALL)
    if not isall:
        st.init_print()
# 转成xml
def convert_xlsx_to_xml(isall = False):
    excelfile_path_list = utils.get_all_excel_files()
    for filename in excelfile_path_list:
        xls = pd.ExcelFile(filename)
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name)
            root = ET.Element(sheet_name)
            for _, row in df.iterrows():
                item = ET.SubElement(root, 'item')
                for col in df.columns:
                    cell = ET.SubElement(item, col)
                    cell_value = str(row[col])
                    cell_value = cell_value.replace('\n', '<br/>')
                    cell.text = cell_value
            xml_filename = f"{os.path.splitext(os.path.basename(filename))[0]}_{sheet_name}.xml"
            xml_path = os.path.join(gv.xml_folder_name, xml_filename)
            
            # 使用 toprettyxml 格式化 XML 输出
            rough_string = ET.tostring(root, 'utf-8')
            reparsed = minidom.parseString(rough_string)
            pretty_xml = reparsed.toprettyxml(indent="  ")
            
            with open(xml_path, "w", encoding="utf-8") as xml_file:
                xml_file.write(pretty_xml)
            
            print(Fore.GREEN + f"{xml_path} 转换xml完成！" + Style.RESET_ALL)
    if not isall:
        st.init_print()
# 转成lua
def convert_xlsx_to_lua(isall = False):
    excelfile_path_list = utils.get_all_excel_files()
    for filename in excelfile_path_list:
        workbook = xlrd.open_workbook(filename)
        for sheet_name in workbook.sheet_names():
            sheet = workbook.sheet_by_name(sheet_name)
            
            lua_filename = f"{os.path.splitext(os.path.basename(filename))[0]}_{sheet_name}.lua"
            lua_path = os.path.join(gv.lua_folder_name, lua_filename)
            
            with open(lua_path, 'w', encoding='utf-8') as lua_file:
                lua_file.write(f"-- {sheet_name}\nlocal {sheet_name} = {{\n")
                
                for row_index in range(1, sheet.nrows):  # 从第二行开始,跳过表头
                    lua_file.write("  {\n")
                    for col_index in range(sheet.ncols):
                        cell_value = sheet.cell_value(row_index, col_index)
                        
                        # 获取表头名称
                        header_name = sheet.cell_value(0, col_index)
                        
                        lua_file.write(f'    {header_name} = ')
                        
                        if isinstance(cell_value, str):
                            cell_value = cell_value.replace('\n', '\\n')
                            lua_file.write(f'"{cell_value}"')
                        elif isinstance(cell_value, float):
                            # 如果是浮点数,根据常识判断是否需要保留小数
                            if header_name.lower() in ["id", "age", "level", "amount"]:
                                # 对于这些字段,转换为整数
                                lua_file.write(str(int(cell_value)))
                            else:
                                # 其他字段保留浮点数
                                lua_file.write(str(cell_value))
                        elif isinstance(cell_value, int):
                            lua_file.write(str(cell_value))
                        elif isinstance(cell_value, bool):
                            # 布尔类型转换为字符串
                            lua_file.write(str(cell_value).lower())
                        else:
                            # 其他类型,转换为字符串
                            lua_file.write(f'"{str(cell_value)}"')
                        
                        lua_file.write(',\n')
                    
                    lua_file.write("  },\n")
                
                lua_file.write("}\n")
                lua_file.write(f"return {sheet_name}\n")
            
            print(Fore.GREEN + f"{lua_path} 转换lua完成！" + Style.RESET_ALL)
    if not isall:
        st.init_print()

# 转成python
def convert_xlsx_to_python(isall = False):
    pass

# 转成C#文件
def convert_xlsx_to_csharp(isall = False):
    pass

# 转成protobuf
def convert_xlsx_to_protobuf(isall = False):
    pass
# 转成bytes
def convert_xlsx_to_bytes(isall = False):
    excelfile_path_list = utils.get_all_excel_files()
    for filename in excelfile_path_list:
        xls = pd.ExcelFile(filename)
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name)
            # 将DataFrame转换为二进制数据
            bytes_data = df.to_csv(index=False).encode('utf-8') 
            bytes_filename = f"{os.path.splitext(os.path.basename(filename))[0]}_{sheet_name}.bytes"
            bytes_path = os.path.join(gv.bytes_folder_name, bytes_filename)
            # 将二进制数据写入文件
            with open(bytes_path, 'wb') as bytes_file:
                bytes_file.write(bytes_data)
            print(Fore.GREEN + f"{bytes_path} 转换bytes完成!" + Style.RESET_ALL)
    if not isall:
        st.init_print()

# 转成sql
def convert_xlsx_to_sql(isall = False):
    pass




# 转全部
def convert_xlsx_to_all():
    convert_xlsx_to_csv(True)
    convert_xlsx_to_json(True)
    convert_xlsx_to_xml(True)
    convert_xlsx_to_lua(True)
    convert_xlsx_to_python(True)
    convert_xlsx_to_csharp(True)
    convert_xlsx_to_protobuf(True)
    convert_xlsx_to_bytes(True)
    convert_xlsx_to_sql(True)
    

# 打印所有的输出文件夹路径
def debug_log_all_folder():
    paths = gv.get_all_paths()
    print(Fore.YELLOW + f"---------所有输出数据的文件夹详情如下---------" + Style.RESET_ALL)
    for key, value in paths.items():
        str = key + "文件夹的目录是" + ':'+ value
        print(Fore.YELLOW + f"{str}" + Style.RESET_ALL)
    print(Fore.YELLOW + f"---------------------------------------------" + Style.RESET_ALL)
    st.init_print()