# -*- coding:gbk -*-

__author__ = 'lybc'
import excel
import sys
reload(sys)
sys.setdefaultencoding('gbk')

def cut():
    filename = raw_input("请输入要处理的文件路径(将文件直接拖到本窗口即可): ")
    branch_index = input("请输入需要按哪一列切分: ")
    branch_index = branch_index - 1
    ex = excel.excel()
    if filename:
        print("正在处理, 请等待....")
        ex.branch_index = branch_index
        print(ex.cut(filename))
    option = raw_input("处理完成, 是否继续? (Y/N)")
    if option == "n" or option == "N":
        exit()


def merge():
    filename = raw_input("请输入要处理的文件路径: ")
    ex = excel.excel()
    if filename:
        print("正在处理, 请等待....")
        print(ex.merge(filename))
    option = raw_input("处理完成, 是否继续? (Y/N)")
    if option == "n" or option == "N":
        exit()

if __name__ == "__main__":
    while(True):
        print(r"""
                       欢迎使用EXCEL处理小工具!

                               _oo0oo_
                              o8888888o
                              88" . "88
                              (| -_- |)
                              0\  =  /0
                            ___/`---'\___
                          .' \\|     |// '.
                         / \\|||  :  |||// \
                        / _||||| -:- |||||- \
                       |   | \\\  -  /// |   |
                       | \_|  ''\---/''  |_/ |
                       \  .-\__  '-'  ___/-. /
                     ___'. .'  /--.--\  `. .'___
                  ."" '<  `.___\_<|>_/___.' >' "".
                 | | :  `- \`.:`\ _ /`:.`/ - ` : | |
                 \  \ `_.   \_ __\ /__ _/   .-` /  /
             =====`-.____`.___ \_____/___.-`___.-'=====
                               `=---='


             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                       佛祖保佑         永无BUG

             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
             请选择你想要进行的操作:
             1. 根据某列分割文件
             2. 合并目录下的所有文件

        """)
        option = input("请选择要进行的操作: ")
        if option == 1:
            cut()
        elif option == 2:
            merge()