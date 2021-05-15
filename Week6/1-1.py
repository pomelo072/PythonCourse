if __name__ == '__main__':
    with open("./data.txt", "w") as in_data:
        data = ["201921099103", "李子夏", "男", "计算机科学学院"]
        for i in data:
            in_data.write(i+"\n")
    with open("./data.txt", "r") as out_data:
        for line in out_data:
            print(line)
