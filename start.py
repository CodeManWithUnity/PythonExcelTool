import main

def init_print():
    print('你好啊,我是一个打表程序,正在开始打表')
    print('请输入你想要的功能')
    print('------1.excel转成csv文件---------------------')
    print('------2.excel转成json文件--------------------')
    print('------3.excel转成xml文件--------------------')
    print('------4.excel转成lua文件---------------------')
    print('------5.excel转成python文件---------------------')
    print('------6.excel转成C#文件---------------------')
    print('------7.excel转成protobuf文件---------------------')
    print('------8.excel转成bytes文件---------------------')
    print('------9.excel转成sql文件---------------------')
    print('------10.查看各个目录输出文件夹----------------')
    print('------0.退出打表工程-------------------------')
    print('------666.一键打表(都转一遍)-------------------')
    user_input = input('请输入你想要的功能:')
    main.start(user_input)

if __name__ == '__main__':
    init_print()





