###################
print "test : --- Testing fitness"
import FitnessMeasures
import Tools
import Point
###################
print "test : --- Test fitness"
width  = 400
height = 400
n_points  = 5
max_radius = 30
points = Tools.FillBoard(width,height,n_points)
print points

fitness = FitnessMeasures.TSFitnessMeasure(points,verbose=True)
print fitness

path = [1,0,7,2,3,4]
print path
results, order = fitness.eval(path)
print "test : order: ",order
print "test : score: ",results
print "test : ---"
###################
print "test : --- done\n"