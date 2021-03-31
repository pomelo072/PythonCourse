if __name__ == '__main__':
    dic_student = {}
    for i in range(5):
        print("请输入 学生:年龄")
        x = input().split(":")
        dic_student[x[0]] = x[1]
    for i in dic_student.items():
        print(i[0]+"\t"+i[1])