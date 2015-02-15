class Pixel():

    def __init__(self, colour, c="b",name="0.0"):
        self.c      = c 
        self.colour = colour
        self.name   = name

    def __repr__(self):
        return "pixl: %s: %s (%s)"%\
         (self.name, repr(self.colour), self.c)