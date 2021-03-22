if __name__ == '__main__':
    foot = eval(input("请输入脚数:"))
    head = eval(input("请输入头数:"))
    x = (4 * head - foot) / 2
    if x.is_integer():
        print("鸡有{}只, 兔有{}只".format(int(x), int(head - x)))
    else:
        print("Data Error!")