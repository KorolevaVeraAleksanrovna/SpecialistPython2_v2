class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, p2):
        return ((p2.x - self.x) ** 2 + (p2.y - self.y) ** 2) ** 0.5


class Triangle:
    def __init__(self, p1, p2, p3):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3

    def perimeter(self):
        a = self.point1.dist_to(p2)
        b = self.point2.dist_to(p3)
        c = self.point3.dist_to(p1)
        return a + b + c

    def area(self):
        a = self.point1.dist_to(p2)
        b = self.point2.dist_to(p3)
        c = self.point3.dist_to(p1)
        hp = (a+b+c)/2
         
        return (hp*(hp - a)(hp - b)(hp - c))**0.5
        

p1 = Point(2, 4)
p2 = Point(10, 8)
p3 = Point(-2, 0)
triangle1 = Triangle(p1, p2, p3)
# Задание: найдите площадь и пеиметр треугольника, реализовав методы

print("Периметр треугольника = ", triangle1.perimeter())
print("Площадь треугольника = ", triangle1.area())
