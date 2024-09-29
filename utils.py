import os

# 读取excel文件夹下的所有文件并添加到容器列表中
def get_file_path(path):
    excelfile_path_list= []
    for root,dirs,files in os.walk(path):
        for file in files:
            file_path = os.path.join(root,file)
            excelfile_path_list.append(file_path)
    return excelfile_path_list
# 剔除掉某个文件夹下包含某个字符的文件
def remove_file(list,str):
    for excel_file in list:
    # 检查文件名是否包含~$字符
        if str in excel_file:
            list.remove(excel_file)
    return list
