import Circle
from random import random
from math import sqrt
import ast

def FillBoard(board,n_circles,max_radius,min_radius=5,current_circles=[]):
    circles = []

    while (len(circles) < n_circles):
        circle = Circle.Circle(random()*board.width, random()*board.height, (random()*(max_radius-min_radius)+min_radius))
        if not board.contained(circle): continue

        non_overlapping = True
        for c in circles:
            if circle.overlap(c) < 0:
                non_overlapping = False
                break
        for c in current_circles:
            if circle.overlap(c) < 0:
                non_overlapping = False
                break
        if non_overlapping:
            circles.append(circle)

    return circles

def WriteCirclesToCSV(circles,file_name,scores=False):
    lines = []
    
    if scores:  lines.append("generation,x,y,r,c,score")
    else:       lines.append("x,y,r,c")

    for i,c in enumerate(circles):
        if scores:  lines.append("%i,%f,%f,%f,%s,%f"%(i,c.x,c.y,c.r,c.c,scores[i]))
        else:       lines.append("%f,%f,%f,%s"%(c.x,c.y,c.r,c.c))

    output_file = open(file_name,"w")
    for l in lines:
        output_file.write(l+"\n")
    output_file.close()

def WriteParametersToFile(parameters,file_name):
    lines = []
    lines.append("parameter,value")
    parameters = ast.literal_eval(parameters.__str__())
    keys = parameters.keys()   
    keys.sort()
    for key in keys:
        # print key, parameters[key]
        lines.append("%s,%s"%(key,repr(parameters[key])))

    output_file = open(file_name,"w")
    for l in lines:
        output_file.write(l+"\n")
    output_file.close()

def SolveBoard(board,circles,verbose=False):
    max_score = 0
    best_circle = False
    global_max_r = 0
    for i in range(board.width):
        for j in range(board.height):
            if verbose: print "tools: %i x %i"%(i,j)
            dx = min(i,board.width-i)
            dy = min(j,board.height-j)
            max_r = min(dx,dy)
            for c in circles:
                di = abs(c.x - i)
                dj = abs(c.y - j)
                dr = (sqrt((di*di) + (dj*dj)) - c.r)
                max_r = min(max_r,dr)
            if max_r > global_max_r:
                global_max_r = max_r
                best_circle = Circle.Circle(i, j, max_r,c="c")
    assert(best_circle), "No valid solutions found!"
    return best_circle
