import string


def rep(s):
    for i in string.punctuation:
        s = s.replace(i, "")
    return s


if __name__ == '__main__':
    book_lst = []
    with open("./hamlet.txt", "r") as data:
        for line in data:
            line = line.replace("\n", "").lower()
            new_line = rep(line)
            book_lst += new_line.split(" ")
    book_dic = {}
    excludes = {"the", "and", "of", "you", "a", "i", "my", "in", "to",
                "it", "that", "is", "not", "this", "but", "", "with", "for"}
    for word in book_lst:
        book_dic[word] = book_dic.get(word, 0) + 1
    for word in excludes:
        del book_dic[word]
    new_dic = sorted(book_dic.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    for i in range(10):
        print("{}: {}".format(new_dic[i][0], new_dic[i][1]))
