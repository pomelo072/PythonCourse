if __name__ == '__main__':
    students = []
    with open("./score.csv", "r") as data:
        for line in data:
            line = line.replace("\n", "")
            students.append(line.split(","))
    columns = students.pop(0)
    for i in range(5):
        s = 0
        for student in students:
            s += int(student[i+1])
        print("{}的平均分为:{:.2f}".format(columns[i+1], s/len(student)))
    students.sort(key=lambda k: k[-1])
    with open("./scoreSort.csv","w") as sort_data:
        sort_data.write(",".join(columns)+"\n")
        for sortStudent in students:
            sort_data.write(",".join(sortStudent)+"\n")
    print("最低分: {} {}".format(students[0][0], students[0][-1]))
    print("最高分: {} {}".format(students[-1][0], students[-1][-1]))

