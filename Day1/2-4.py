#!/usr/bin/env python
# coding=utf-8

if __name__ == "__main__":
    x = input("请输入要转换的币值及符号，以¥或$结束：")
    if x[-1] == "¥":
        s = eval(x[:-1]) * 0.1456
        print("{0}元人民币可以兑换{1:.2f}美元".format(x[0:-1], s))
    elif x[-1] == "$":
        s = eval(x[:-1]) * 6.868
        print("{0}美元可以兑换{1:.2f}元人民币".format(x[0:-1], s))
    else:
        print("输入错误，请以¥或$结束")
        
