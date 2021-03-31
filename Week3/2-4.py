if __name__ == '__main__':
    dic_city = {"张三风": ["北京", "成都"], "李茉绸": ["上海", "广州", "兰州"], "慕容福": ["太原", "西安", "济南", "上海"]}
    sh_lst = []
    for i in dic_city.keys():
        print("{}去过{}个城市".format(i, len(dic_city[i])))
        if "上海" in dic_city[i]:
            sh_lst.append(i)
    print("去过上海的有{}人, 他们是".format(len(sh_lst)), end="")
    for x in sh_lst:
        print(x, end=",")
