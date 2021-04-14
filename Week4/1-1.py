dicCategory = {"1": "面类", "2": "饭类", "3": "西餐类"}
dicMenu = {
    "面类": {"1": "四海鱼蛋面", "2": "湾仔三鲜面", "3": "意式肉酱面"},
    "饭类": {"1": "碎肉玉米饭", "2": "耗油牛肉饭", "3": "蒜蓉鸭翅饭"},
    "西餐类": {"1": "黑椒猪排", "2": "菲力牛排", "3": "西冷牛排"},
}


def show_category():
    print("欢迎光临")
    print("本饭店菜单分类如下:")
    for key, value in dicCategory.items():
        print("{} ---- {}".format(key, value))


def select_category():
    categoryNO = input("请输入编号(1,2,3)选择菜单分类:")
    return dicCategory[categoryNO]


def show_menu(category):
    print("{}菜单如下:".format(category))
    for key, value in dicMenu[category].items():
        print("{} ---- {}".format(key, value))


def select_menu(category):
    nameNO = input("请输入(1,2,3)选择菜单名:")
    return dicMenu[category][nameNO]


listMenu = []
while True:
    show_category()
    category = select_category()
    show_menu(category)
    menuName = select_menu(category)
    listMenu.append(menuName)

    goOn = input("是否继续点菜? 是请按y, 否请按n:")
    if goOn == "n":
        break
print("您点的菜为:{}".format(",".join(listMenu)))
