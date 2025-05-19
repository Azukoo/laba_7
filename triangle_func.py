#Функция определяет тип треугольника по длинам его сторон.
class IncorrectTriangleSides(Exception):
    pass

def get_triangle_type(длина1, длина2, длина3):

    if длина1 <= 0 or длина2 <= 0 or длина3 <= 0 or длина1 + длина2 <= длина3 or длина1 + длина3 <= длина2 or длина2 + длина3 <= длина1:
        raise IncorrectTriangleSides("Неправильная длина сторон треугольника")

    if длина1 == длина2 == длина3:
        return "equilateral" #равносторонний
    elif длина1 == длина2 or длина1 == длина2 or длина2 == длина3:
        return "isosceles" #равнобедренный
    else:
        return "nonequilateral" #разносторонний

print(get_triangle_type(3, 3, 3))  
print(get_triangle_type(3, 3, 5))  
print(get_triangle_type(3, 4, 5)) 