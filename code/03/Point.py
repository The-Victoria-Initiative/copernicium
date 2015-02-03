class Point():
    from math import sqrt

    def __init__(self, x, y, c="b",name="0.0"):
        self.x = x
        self.y = y
        self.c = c 
        self.name = name

    def __repr__(self):
        return "Point: %s: [%.2f x %.2f], (%s)"%(self.name, self.x, self.y, self.c)