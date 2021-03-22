if __name__ == '__main__':
    for i in range(3, 101):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, end=" ")
