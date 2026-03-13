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
p1= Point(1,3)
p2= Point(3, 4)

print(p1.x, p1.y)
print(p2.x, p2.y)
print(p1)