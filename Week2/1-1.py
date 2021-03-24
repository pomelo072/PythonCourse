if __name__ == '__main__':
    foot = int(input("请输入脚数:"))
    head = int(input("请输入头数:"))
    x = (4 * head - foot) / 2
    if x.is_integer() and x >= 0 and (head - x) >= 0:
        print("鸡有{}只, 兔有{}只".format(int(x), int(head - x)))
    else:
        print("Data Error!")
