if __name__ == '__main__':
    for i in range(1, 20):
        for j in range(int((100 - 5 * i) / 3)):
            m = 100 - i - j
            if m % 3 != 0:
                continue
            if (5 * i + 3 * j + m / 3 == 100) and (i != 0 and j != 0 and m != 0):
                print("公鸡有{}个, 母鸡有{}个, 小鸡有{}个".format(i, j, m))
