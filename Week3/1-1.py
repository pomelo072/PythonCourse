import random

if __name__ == '__main__':
    lst_suit = ["黑桃", "红桃", "梅花", "方块"]
    lst_face = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']
    lst = [x + y for x in lst_suit for y in lst_face]
    b_list = lst.copy()
    # print(lst)
    random.shuffle(lst)
    user = eval(input("抽牌(0-51):"))
    computer = random.randint(0, 51)
    print("你抽的牌是 {}".format(lst[user]))
    print("电脑抽的牌是 {}".format(lst[computer]))
    if b_list.index(lst[user]) > b_list.index(lst[computer]):
        print("恭喜, 你赢了")
    elif b_list.index(lst[user]) < b_list.index(lst[computer]):
        print("很遗憾,你输了")
    else:
        print("咱们平手了")
