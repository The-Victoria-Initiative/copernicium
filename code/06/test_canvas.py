###################
print "test : --- Testing canvas"
import Canvas
###################
print "test : --- Test filling canvas"
width  = 400
height = 400
canvas = Canvas.Canvas(width,height,verbose=True)
print canvas
print "test : ---"
###################
print "test : --- Add a circle"
import Circle
circle = Circle.Circle(100,100,100,colour=(255,200,255))
canvas.add_circle(circle)
###################
# print "test : --- Find filled pixels"
# canvas.find_filled_pixels()
# print canvas.filled_pixels
# ###################
# print "test : --- Compare canvases"
# canvas_b = Canvas.Canvas(width,height,fill="steelblue", verbose=True)
# score = canvas.compare(canvas_b)
# print "test : comparison score: %i"%score
###################
print "test : --- Test saving canvas"
file_name = "/zinc/web/copernicium/04/images/test.bmp"
canvas.save(file_name)
print "test : ---"
###################
# print "test : --- Test saving cleared canvas"
# file_name = "/zinc/web/copernicium/04/images/ideal.bmp"
# canvas.clear()
# canvas.save(file_name)
# print "test : ---"
###################
print "test : --- done\n"