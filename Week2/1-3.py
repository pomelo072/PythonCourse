if __name__ == '__main__':
    while True:
        score = input("请输入成绩(直接回车结束):")
        if score == "":
            break
        dig_score = eval(score)
        if dig_score < 0 or dig_score > 100:
            print("请输入0—100之间的整数！")
        elif dig_score >= 90:
            print("A")
        elif dig_score >= 80:
            print("B")
        elif dig_score >= 70:
            print("C")
        elif dig_score >= 60:
            print("D")
        else:
            print("E")
