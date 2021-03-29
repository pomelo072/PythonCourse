if __name__ == '__main__':
    s = input("请输入一串字符:")
    s = s.lower()
    lst = []
    for i in s:
        if i in " ,.!?":
            continue
        if i in lst:
            continue
        lst.append(i)
    lst.sort()
    for x in lst:
        print(x, end=",")
