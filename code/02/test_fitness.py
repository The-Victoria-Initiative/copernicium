###################
print "test : --- Testing fitness"
import Board
import FitnessMeasures
import Tools
import Circle
###################
print "test : --- Test fitness"
width  = 400
height = 400
board = Board.Board(width,height,verbose=True)
print board
n_circles  = 20
max_radius = 30
circles = Tools.FillBoard(board,n_circles,max_radius)
circles = [Circle.Circle(30,100,11),Circle.Circle(1,100,2)]
print circles

fitness = FitnessMeasures.CircleFitnessMeasure(board,circles,verbose=True)
print fitness

x = 10
y = 100
r = 10
circle = Circle.Circle(x,y,r)
print circle
print "fitness: ",fitness.eval(circle)
print "test : ---"
###################
print "test : --- done\n"