class Line():

    def __init__(self, x1, y1, x2, y2, width=1, colour="steelblue", c="b",name="0.0"):
        self.x1     = x1
        self.y1     = y1
        self.x2     = x2
        self.y2     = y2
        self.width  = width
        self.c      = c 
        self.colour = colour
        self.name   = name

    def __repr__(self):
        return "Line: %s: (%i, %i) -> (%i, %i), w: %i (%s)"%\
         (self.name, self.x1, self.y1, self.x2, self.y2, self.width, self.c)