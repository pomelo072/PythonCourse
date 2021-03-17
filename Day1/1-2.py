# Create on pomelo.
import math


if __name__ == "__main__":
    v = math.pi * 66 * 66 * 24.2
    s = math.pi * 66*66 *2 + 2 * math.pi * 66 * 24.2
    print("圆柱体的体积为{0:.2f}，表面积为{1:.2f}".format(v, s))
    s = (math.pi * 16.2**2) - (math.pi * 9.4**2)
    print(f"圆环面积为{s:.2f}")
    v = (4/3) * math.pi * 2.11**3
    print(f"圆球体积为{v:.2f}")