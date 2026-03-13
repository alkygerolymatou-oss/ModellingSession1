from point import Point



class ColourPoint(Point):
    """
    color point class inheriting from point class
    """
    def __int__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour

p1= ColourPoint(1, 2, "red")
