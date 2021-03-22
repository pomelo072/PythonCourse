import random


if __name__ == '__main__':
    num = int(input("请输入要生成激活码的个数:"))
    for q in range(num):
        key = ""
        for x in range(29):
            if x in [5, 11, 17, 23]:
                key += "-"
            else:
                key += random.choice("BCEFGHJKMPQTVWXY2346789")
        print(key)
