import random as r

if __name__ == '__main__':
    lst_who = ["小马", "小羊", "小鹿"]
    lst_where = ["草地上", "电影院", "家里"]
    lst_what = ["看电影", "听故事", "吃晚饭"]
    print("{}在{}{}".format(lst_who[r.randint(0, 2)], lst_where[r.randint(0, 2)], lst_what[r.randint(0, 2)]))
