# Created on Pomelo.
import math


if __name__ == "__main__":
    x1 = input("请输入x1:")
    y1 = input("请输入y1:")
    x2 = input("请输入x2:")
    y2 = input("请输入y2:")
    z = math.sqrt((int(x1)-int(x2))**2+(int(y1)-int(y2))**2)
    print("两点间距离为：{0:.2f}".format(z))