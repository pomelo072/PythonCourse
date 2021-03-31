if __name__ == '__main__':
    lst_staff = ["李梅", "张富", "付妍", "赵诺", "刘江"]
    dic_award = {"张富": 10000, "赵诺": 15000}
    for i in lst_staff:
        print("{} {}".format(i, dic_award.get(i, 5000)))
