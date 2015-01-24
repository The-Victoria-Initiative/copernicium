class Board():

    def __init__(self, width, height, verbose=False):
        self.verbose = verbose
        self.width   = width
        self.height  = height

    def contained(self, circle):
        return ((circle.x - circle.r) >= 0) and \
               ((circle.x + circle.r) <= self.width) and \
               ((circle.y - circle.r) >= 0) and \
               ((circle.y + circle.r) <= self.height)

    def containment(self, circle):
        distance_to_x_edge = min(circle.x, (self.width - circle.x))
        distance_to_y_edge = min(circle.y, (self.height - circle.y))
        distance_to_edge   = min(distance_to_x_edge, distance_to_y_edge)
        return distance_to_edge - circle.r 

    def __repr__(self):
        return "Board: [%i x %i]"%(self.width,self.height)
