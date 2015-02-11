###################
print "test : --- Testing a population"
import Canvas
import FitnessMeasures
import Line
from random import random
###################
print "test : generating an empty canvas"
width  = 400
height = 400
canvas = Canvas.Canvas(width,height,verbose=True)
print "test : Drawing a square on the board"
canvas.add_line(Line.Line(100,100, 300,100))
canvas.add_line(Line.Line(300,100, 300,300))
canvas.add_line(Line.Line(300,300, 100,300))
canvas.add_line(Line.Line(100,300, 100,100))
file_name = "/zinc/web/copernicium/04/images/ideal.bmp"
canvas.save(file_name)
print "test : Generating fitness measure"
fitness = FitnessMeasures.CanvasFitnessMeasure(canvas)
print "test : Make a test canvas with random lines"
canvas_b = Canvas.Canvas(width,height,verbose=True)
for i in range(4):
    canvas_b.add_line(Line.Line(random()*width,
                                random()*height,
                                random()*width,
                                random()*height))
score = fitness.eval(canvas_b)
print "test : Scored: %i"%score
file_name = "/zinc/web/copernicium/04/images/test.bmp"
canvas_b.save(file_name)
# ###################
print "test : --- done\n"