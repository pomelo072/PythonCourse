class ThreeDimensionalVector:
    def __init__(self, x=1, y=1, z=1):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+","+str(self.z)+")"

    def addition(self, b):
        return ThreeDimensionalVector(self.x + b.x, self.y + b.y, self.z + b.z)

    def subtraction(self, b):
        return ThreeDimensionalVector(self.x - b.x, self.y - b.y, self.z - b.z)

    def multiplication(self, num):
        return ThreeDimensionalVector(self.x * num, self.y * num, self.z * num)

    def division(self, num):
        return ThreeDimensionalVector(self.x / num, self.y / num, self.z / num)

    def cross_multiplication(self, b):
        return ThreeDimensionalVector(self.y * b.z - self.z * b.y, self.z * b.x - self.x * b.z, self.x * b.y - self.y * b.x)

    def dot_multiplication(self, b):
        return self.x * b.x + self.y * b.y + self.z * b.z


if __name__ == '__main__':
    v1 = ThreeDimensionalVector(1, 2, 3)
    v2 = ThreeDimensionalVector(4, 5, 6)
    print("向量a + 向量b = ", v1.addition(v2))
    print("向量a - 向量b = ", v1.subtraction(v2))
    print("向量a * 常数num = ", v1.multiplication(2))
    print("向量a / 常数num = ", v1.division(2))
    print("向量a .* 向量b = ", v1.dot_multiplication(v2))
    print("向量a * 向量b = ", v1.cross_multiplication(v2))
