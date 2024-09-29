import main

def init_print():
    print('你好啊,我是一个打表程序,正在开始打表')
    print('请输入你想要的功能')
    print('------1.excel转成python文件------------------')
    print('------2.excel转成json文件--------------------')
    print('------3.excel转成lua文件---------------------')
    print('------4.excel转成xml文件---------------------')
    print('------4.查看各个目录输出文件夹----------------')
    print('------5.一键打表(都转一遍)-------------------')
    print('------6.退出打表工程-------------------------')
    user_input = input('请输入你想要的功能:')
    main.start(user_input)

if __name__ == '__main__':
    init_print()





