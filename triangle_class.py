class IncorrectTriangleSides(Exception):
    pass

class Triangle:
    def __init__(self, длина1, длина2, длина3):
        if длина1 <= 0 or длина2 <= 0 or длина3 <= 0 or длина1 + длина2 <= длина3 or длина1 + длина3 <= длина2 or длина2 + длина3 <= длина1:
            raise IncorrectTriangleSides("Неправильная длина сторон треугольника")

        self.длина1 = длина1
        self.длина2 = длина2
        self.длина3 = длина3

    def triangle_type(self):
        if self.длина1 == self.длина2 == self.длина3:
            return "equilateral"
        elif self.длина1 == self.длина2 or self.длина1 == self.длина3 or self.длина2 == self.длина3:
            return "isosceles"
        else:
            return "nonequilateral"

    def perimeter(self):
        return self.длина1 + self.длина2 + self.длина3