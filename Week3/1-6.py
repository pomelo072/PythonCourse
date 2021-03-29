if __name__ == '__main__':
    kv = lambda x, t, i: t(x.split(":")[i])
    dic = lambda a: dict([(kv(x, str, 0), kv(x, int, 1)) for x in a.split(",")])
    d = dic("语文:80,数学:82,英语:90,物理:85,化学:88,美术:80")
    s = 0
    for v in d.values():
        s += v
    print("总分为{}, 平均分为{:.1f}".format(s, s / len(d)))
