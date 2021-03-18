#!/usr/bin/env python
# coding=utf-8
if __name__ == "__main__":
    s = input("please input your ID number:")
    if len(s) == 18:
        print("出生日期:{0}年{1}月{2}日".format(s[6:10], s[10:12], s[12:14]))
    else:
        print("length Error!")
