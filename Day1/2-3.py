#!/usr/bin/env python
# coding=utf-8
if __name__ == "__main__":
    x = input("请输入要兑换的人民币币值，以¥结束：")
    a = eval(x[:-1]) * 0.1456
    print("{0}元人民币可以兑换{1:.2f}".format(x, a))
