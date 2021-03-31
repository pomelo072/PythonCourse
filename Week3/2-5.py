if __name__ == '__main__':
    s = "When in the course of human events, it becomes necessary for one people to dissolve the political bands " \
        "which have connected them with another, and to assume among the powers of the earth, the separate and equal " \
        "station to which th Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of " \
        "mankind requires that they should declare the causes which impel them to the separation."
    dic = {}
    s = s.split(" ")
    for i in s:
        if i not in dic.keys():
            if i[-1] in ",.":
                i = i[:-1]
            dic[i] = 1
        else:
            dic[i] += 1
    print(dic)
    lst = []
    for x in range(5):
        v = max(dic.values())
        for i in dic.items():
            if i[1] == v:
                lst.append(i)
                dic.pop(i[0])
                break
    print("排名前五为:")
    for s in lst:
        print("{}: {}".format(s[0], s[1]))
