###################
print "test : --- Testing Circle"
import Circle
###################
print "test : --- Test making circle"
x = 10
y = 100
r = 15
circle = Circle.Circle(x,y,r)
print circle
print "test : ---"
###################
print "test : --- Test for overlapping"
circle_b = Circle.Circle(10,100,1)
print circle, circle_b
print circle.overlap(circle_b)
print "test : ---"
###################
print "test : --- Make a vector of non-overlapping circles"
from random import random
width  = 400
height = 400
max_r  = 100

circles = [circle]
while (len(circles) < 10):
    new_circle = Circle.Circle(random()*width, random()*height, random()*max_r)
    print new_circle
    non_overlapping = True
    for c in circles:
        if new_circle.overlap(c) < 0:
            non_overlapping = False
            print "test :     bad"
            break
    if non_overlapping:
        print "test :     good (%i)"%(len(circles)+1)
        circles.append(new_circle)
for c in circles: print c
print "test : ---"
###################
print "test : --- done\n"