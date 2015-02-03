###################
print "test : --- Testing Point"
import Point
###################
print "test : --- Test making point"
x = 10
y = 100
point = Point.Point(x,y)
print point
print "test : ---"
###################
print "test : --- Make a vector of unique points"
from random import random
width  = 400
height = 400

points = [point]
while (len(points) < 10):
    new_point = Point.Point(random()*width, random()*height)
    print new_point
    non_overlapping = True
    for c in points:
        if (new_point.x == c.x) or (new_point.y == c.y):
            non_overlapping = False
            print "test :     bad"
            break
    if non_overlapping:
        print "test :     good (%i)"%(len(points)+1)
        points.append(new_point)
for c in points: print c
print "test : ---"
###################
print "test : --- done\n"