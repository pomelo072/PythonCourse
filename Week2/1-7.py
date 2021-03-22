if __name__ == '__main__':
    people = [x for x in range(1, 42)]
    point = 0
    while len(people) >= 3:
        point = (3 - 1 + point) % len(people)
        people.pop(point)

    print(people)

