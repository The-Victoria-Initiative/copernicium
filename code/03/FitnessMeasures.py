class TSFitnessMeasure():
    from math import fabs, sqrt

    def __init__(self,points,verbose=False):
        self.points = points
        self.verbose = verbose

    def eval(self,path):
        # print path
        path_length = 0
        visited     = []
        for i in range(len(path)):
            if path[i] >= len(self.points):
                continue
            if len(visited) ==0:
                visited.append(path[i])
            
            if path[i] in visited:
                continue
            
            this_from = self.points[visited[-1]]
            this_to   = self.points[path[i]]
            dx = self.fabs(this_from.x - this_to.x)
            dy = self.fabs(this_from.y - this_to.y)
            dr = self.sqrt((dx*dx) + (dy*dy))
            path_length += dr
            visited.append(path[i])
            if self.verbose: 
                print "fit  :     [%i - %i], (%i,%i) - (%i,%i) = %.2f, path length: %.2f"%\
                 (visited[-2],visited[-1],this_from.x,this_from.y,this_to.x,this_to.y,dr,path_length)
        if self.verbose:
            print "fit  : visited: %s"%repr(visited)
        if len(visited) != len(self.points): return (1. / 1e12), visited
        return (1. / path_length), visited
            
        
    def __repr__(self):
        return "fit  : --- TS fitness measure"