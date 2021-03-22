if __name__ == '__main__':
    for x in range(20):
        for y in range(33):
            for z in range(0, 100, 3):
                if (x + y + z == 100) and (5 * x + z // 3 + 3 * y) == 100 and (x != 0 and y != 0 and z != 0):
                    print('公鸡：%d 母鸡：%d 小鸡: %d' % (x, y, z))
