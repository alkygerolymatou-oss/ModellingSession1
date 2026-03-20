from point import Point

class ColourPoint(Point):
    """
    color point class inheriting from point class
    """
    def __int__(self, x, y, colour):
        #check if x and y are number
        if not isinstance(x, (int, float)):
            raise TypeError("x must be an number")
        if not isinstance(y,(int, float)):
            raise TypeError("y, misy be an number")
        self.x = x
        self.y = y
        self.colour = colour

if __name__ == "__main__":
    color_point = ColourPoint()
    print(color_point)
    p1= ColourPoint(1, 2, "red")
    p2 = ColourPoint(1, 1, "blue")
    p3= ColourPoint(5, 6, "blue")
    p4= ColourPoint(-2, -3, "yellow")
    color_points =[p1, p2, p3, p4]
    print(p1.color)
    print(p1)
    print(color_points)
    color_points.sort()
    print(color_point)
    #p5=ColourPoint("bob", "james", "red")



