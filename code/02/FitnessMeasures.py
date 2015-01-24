class CircleFitnessMeasure():

    def __init__(self,board,circles,verbose=False):
        self.board   = board
        self.circles = circles
        self.verbose = verbose

    def eval(self,circle):
        base_value = circle.r**2
        # if off of the board or overlapping with another circle give it a harsh penalty term
        overlap = 0
        for c in self.circles:
            this_overlap = circle.overlap(c)
            if this_overlap < 0.: overlap = overlap + this_overlap

        containment = self.board.containment(circle)
        containment = min(containment,0)

        if self.verbose:
            print "cfit : base value from r of %i is: %i"%(circle.r,base_value)
            print "cfit : containment = %i"%containment
            print "cfit : overlap     = %i"%overlap

        # base_value -= overlap**4
        # base_value -= containment**4
        # base_value = max(0.0001,base_value)
        if overlap < 0:     base_value = 0.00001
        if containment < 0: base_value = 0.00001

        if self.verbose:
            print "cfit : final value: %i"%base_value
        return base_value
        
    def __repr__(self):
        return "nfit : --- Circle fitness measure"