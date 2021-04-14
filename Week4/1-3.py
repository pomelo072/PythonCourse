import random as rd


def find_fox():
    hole = list(range(1, 6))
    fox = rd.choice(hole)
    find = 0
    while True:
        find = int(input("猜猜是哪个洞(1-5)?"))
        if find == fox:
            print("找到了, 小狐狸在{}洞".format(find))
            break
        hole_next = [hole[fox - 2], hole[fox]]
        fox = rd.choice(hole_next)


if __name__ == '__main__':
    find_fox()
