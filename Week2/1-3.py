if __name__ == '__main__':
    score = eval(input("请输入成绩:"))
    if score < 0 or score > 100:
        print("请输入0—100之间的整数！")
    elif score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("E")
