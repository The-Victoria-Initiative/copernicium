import Circle
from random import random

def FillBoard(board,n_circles,max_radius,current_circles=[]):
    circles = []

    while (len(circles) < n_circles):
        circle = Circle.Circle(random()*board.width, random()*board.height, random()*max_radius)
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