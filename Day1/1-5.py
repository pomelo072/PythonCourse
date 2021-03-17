# Create on pomelo.
import math


if __name__ == "__main__":
    r = eval(input("请输入球的半径："))
    s = 4 * math.pi * r**2
    v = (4/3) * math.pi * r**3
    print(f"球的面积为：{s}\n球的体积为：{v}")