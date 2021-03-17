# Create on pomelo.

import math
import sys


if __name__ == "__main__":
    a = eval(input("请输入三角形的第1条边长："))
    b = eval(input("请输入三角形的第2条边长："))
    c = eval(input("请输入三角形的第3条边长："))
    if (a+b < c) or (a+c < b) or (b+c < a):
        print("边长不组成三角形")
        sys.exit(-1)
    p = (a + b + c) / 2
    s = p * (p - a) * (p - b) * (p - c)
    print(f"该三角形的面积为：{math.sqrt(s)}")