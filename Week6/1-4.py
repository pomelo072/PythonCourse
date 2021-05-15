import random


if __name__ == '__main__':
    miyus = []
    with open("./7_4儿童谜语集.csv", "r", encoding="utf8") as data:
        for line in data:
            line = line.replace("\n", "")
            miyus.append(line.split(","))
    columns = miyus.pop(0)
    print(columns)
    print(miyus)
    for i in range(5):
        with open("./试卷_"+str(i+1)+".txt", "w") as temp_data:
            with open("./答卷_"+str(i+1)+".txt", "w") as temp_data_w:
                for x in range(10):
                    miti = miyus[random.randint(0, len(miyus)-1)]
                    temp_data.write(miti[0] + "\n")
                    temp_data_w.write(",".join(miti)+"\n")
