import Point
from random import random
from math import sqrt, fabs
import ast
import json

def FillBoard(width, height, n_points, min_distance=10):
    points = []

    while (len(points) < n_points):
        point = Point.Point(random()*width, random()*height)

        non_overlapping = True
        for c in points:
            if (fabs(point.x - c.x) < min_distance) and \
               (fabs(point.y - c.y) < min_distance):
                non_overlapping = False
                break

        if non_overlapping:
            points.append(point)

    return points

def WritePointsToCSV(points,file_name):
    lines = []
    lines.append("x,y")
    for i,c in enumerate(points):
        lines.append("%f,%f"%(c.x,c.y))

    output_file = open(file_name,"w")
    for l in lines:
        output_file.write(l+"\n")
    output_file.close()

def WritePathToFile(path,points,file_name):
    lines = []
    lines.append("x1,y1,x2,y2")
    for i in range(len(path)):
        if i == 0: continue
        this_from = points[path[i-1]]
        this_to   = points[path[i]]
        lines.append("%f,%f,%f,%f"%(this_from.x,this_from.y,this_to.x,this_to.y))
    output_file = open(file_name,"w")
    for l in lines:
        output_file.write(l+"\n")
    output_file.close()

def WriteScoresToFile(scores,file_name):
    lines = []
    lines.append("generation,score")
    for i,s in enumerate(scores):
        lines.append("%i,%f"%(i,s))
    output_file = open(file_name,"w")
    for l in lines:
        output_file.write(l+"\n")
    output_file.close()

def MinBases(n):
    i = 0
    while (True):
        if (2**i) >= n:
            return i
        i+=1

def WriteGenotypeToJSON(genotype, file_name, fitness=False):
    g_dict = {}
    g_dict["genes"] = []
    for gene in genotype.genes:
        g_dict["genes"].append({"code":gene.code,"number":int(gene.code, 2)})
    output_file = open(file_name,"w")
    output_file.write(json.dumps(g_dict)+"\n")
    output_file.close()

# def WriteParametersToFile(parameters,file_name):
#     lines = []
#     lines.append("parameter,value")
#     parameters = ast.literal_eval(parameters.__str__())
#     keys = parameters.keys()   
#     keys.sort()
#     for key in keys:
#         # print key, parameters[key]
#         lines.append("%s,%s"%(key,repr(parameters[key])))

#     output_file = open(file_name,"w")
#     for l in lines:
#         output_file.write(l+"\n")
#     output_file.close()

# def SolveBoard(board,points,verbose=False):
#     max_score = 0
#     best_circle = False
#     global_max_r = 0
#     for i in range(board.width):
#         for j in range(board.height):
#             if verbose: print "tools: %i x %i"%(i,j)
#             dx = min(i,board.width-i)
#             dy = min(j,board.height-j)
#             max_r = min(dx,dy)
#             for c in circles:
#                 di = abs(c.x - i)
#                 dj = abs(c.y - j)
#                 dr = (sqrt((di*di) + (dj*dj)) - c.r)
#                 max_r = min(max_r,dr)
#             if max_r > global_max_r:
#                 global_max_r = max_r
#                 best_circle = Circle.Circle(i, j, max_r,c="c")
#     assert(best_circle), "No valid solutions found!"
#     return best_circle
