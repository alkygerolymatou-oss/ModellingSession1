class Point:
    """
    simple class to represent a point in 2d space.
    """

    def __init__(self, x, y):
        """
        Constructor for Point class
        """
        self.x = x
        self.y = y
    def __str__(self):
        """
        string representation of point alass.
        :return string repsresation
        :return:
        """
        return f"P<{self.x}, {self.y}"
    def __repr__(self):
        return self.__str__()
    def distance_origin(self):
       """
       calculate the distance between poit and origin
       :return: floay, distance between
       """
       return (self.x**2 + self.y**2) ** 0.5
    def distance_to(self, point):
        """

        :param point:
        :return:
        """
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) **0.5
    def __it__(self, other):
        """

        :param other:
        :return:
        """
        return self.distance_origin() < other.distance_origin


if __name__ == "__main__":
p1= Point(1,3)
p2= Point(3, 4)

print(p1.x, p1.y)
print(p2.x, p2.y)
print(p1)
print(f"{p2}distance origin is {p2.distance_origin()}")
p3= Point(12, 5)
print(f"{p3}distance origin is {p3.distance_origin()}")
p1= Point(6, 10)
p2= Point(6, 15)
print(f"distance between {p1} and {p2} is {p1.distance_to(p2)}")
p4= Point(1,1)
points=[p1, p2, p3, p4, Point(15, 6)] #list of points
print(points)
points.sort()
print(points)