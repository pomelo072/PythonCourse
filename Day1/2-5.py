#!/usr/bin/env python
# coding=utf-8

if __name__ == "__main__":
    m = int(input("输入1-12的整数："))
    month = "JanFebMarAprMayJunJulAugSepOctNovDec"
    print(month[(m-1)*3:(m-1)*3+3])
