import point, math

class Triangle:
    """
    Make a class to do some things with triangles.
    """
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3


    def is_triangle(self):
        """
        Says if it's a triangle or not.
        """
        x1 = self.point1.x
        x2 = self.point2.x
        x3 = self.point3.x
        y1 = self.point1.y
        y2 = self.point2.y
        y3 = self.point3.y
        exp = ((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)) / 2
        return exp != 0


    def perimeter(self):
        """
        Gives us perimeter of the triangle.
        """
        line1 = math.sqrt((self.point1.x - self.point2.x)**2 + (self.point1.y - self.point2.y)**2)
        line2 = math.sqrt((self.point2.x - self.point3.x)**2 + (self.point2.y - self.point3.y)**2)
        line3 = math.sqrt((self.point3.x - self.point1.x)**2 + (self.point3.y - self.point1.y)**2)

        return line1 + line2 + line3


    def area(self):
        """
        Gives us area of the triangle.
        """
        line1 = math.sqrt((self.point1.x - self.point2.x)**2 + (self.point1.y - self.point2.y)**2)
        line2 = math.sqrt((self.point2.x - self.point3.x)**2 + (self.point2.y - self.point3.y)**2)
        line3 = math.sqrt((self.point3.x - self.point1.x)**2 + (self.point3.y - self.point1.y)**2)
        p = (line1 + line2 + line3) / 2

        return math.sqrt(p * (p - line1) * (p - line2) * (p - line3))


if __name__ == "__main__":
    triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
    # print(triangle.is_triangle())
    # print(triangle.perimeter())
    # print(triangle.area())
