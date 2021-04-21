class Rect:
    def __init__(self, length=2.0, width=3.0):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)


if __name__ == '__main__':
    r = Rect(float(input("长:")), float(input("宽:")))
    print(r.get_area(), " ", r.get_perimeter())
    r2 = Rect(16.0, 6.0)
    print(r2.get_area(), " ", r2.get_perimeter())
