if __name__ == '__main__':
    x = eval(input("x = "))
    if x >= 20:
        print(0)
    elif x >= 10:
        print(0.5 * x - 2)
    elif x >= 5:
        print(3 * x - 5)
    elif x >= 0:
        print(x)
    else:
        print(0)
