class Circle():
    from math import sqrt

    def __init__(self, x, y, r, colour="steelblue", c="b",name="0.0",radius_limit=False):
        self.x = x
        self.y = y
        if radius_limit:
            self.r = min(radius_limit,r)
        else:
            self.r = r

        self.c = c 
        self.colour = colour
        self.name = name

    def overlap(self,circle):
        dx = self.x-circle.x
        dy = self.y-circle.y
        dr = self.sqrt( (dx*dx) + (dy*dy) )
        sum_r = self.r + circle.r
        return dr - sum_r

    def __repr__(self):
        return "Circle: %s: [%.2f x %.2f], r = %.2f (%s)"%(self.name, self.x, self.y, self.r, self.c)