import random as rd


def redbag(total=100, num=15):
    bag = []
    for i in range(num):
        if i == num - 1:
            bag.append(round(total, 2))
            break
        money = round(rd.uniform(0.01, total/(num - i)), 2)
        bag.append(money)
        total -= money
    return bag


if __name__ == '__main__':
    bag = redbag(10, 3)
    for i in range(len(bag)):
        print("第{}人领了{}元".format(i+1, bag[i]))
    print()
    bag = redbag()
    for i in range(len(bag)):
        print("第{}人领了{}元".format(i + 1, bag[i]))