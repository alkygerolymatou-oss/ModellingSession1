from color_point import ColourPoint

class AdvancedPoint(ColourPoint):
    #class variables
    COLORS = ["red", "green", "blue", "yellow", "black", "white"]
    def __init__(self, x, y, color):
        #check color
        if color not in self.COLORS:
            raise ValueError(f"Invalid colour: you need to be one of the {self.COLORS}")
        self._x= x
        self._y= y
        self._color= color

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value): #this is a setter
        if value not in self.COLORS:
            raise ValueError(f"invalid colour: yu need to be one of the {self.COLORS}")
        self._color= value

    @classmethod
    def add_color(cls, color):
        #add a ne offical color to the list
        cls.COLORS.append(color)

    @staticmethod
    def distance_2_point(p1, p2):
        return ((p1.x- p2.x)**2 +(p1.y- p2.v)**2)**5



    @staticmethod
    def from_dict(d): # factory allos to creat from a dictionary
        x= d["x"]
        y= d["y"]
        color= d["color"]
        return AdvancedPoint(x, y, color)

p0= AdvancedPoint.from_dict({"x": 1, "y":2, "color": "red" })
p1=AdvancedPoint(1, 2, "blue")
print(p1)
p2= AdvancedPoint(3, 4, "red")
print(p2)
# p1.x= 7 #problem , dont want to change like this
print(p1)
print(p1.x)
#ypu call class methods via the class name instead of the instance name
AdvancedPoint.add_color("coral")
p3= AdvancedPoint(1, 2, "coral")
print(p3)