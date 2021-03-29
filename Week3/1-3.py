if __name__ == '__main__':
    lst_fib = [1, 1]
    for i in range(28):
        x = lst_fib[i] + lst_fib[i + 1]
        lst_fib.append(x)
    print(lst_fib)
