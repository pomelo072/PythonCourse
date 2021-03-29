if __name__ == '__main__':
    lst_score = [9, 10, 8, 9, 10, 7, 6, 8, 7, 8]
    lst_score.sort()
    lst_score.pop(0)
    lst_score.pop(-1)
    print("该选手最后得分为{}".format(sum(lst_score) / len(lst_score)))
