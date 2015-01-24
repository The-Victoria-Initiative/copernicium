###################
print "test : --- Testing tools"
import Tools
import Board
import Circle
###################
print "test : --- Test filling a board with circles"
width  = 400
height = 400
board = Board.Board(width,height,verbose=True)
print board
n_circles  = 20
max_radius = 30
circles = Tools.FillBoard(board,n_circles,max_radius)
print circles
extra_circles = Tools.FillBoard(board,n_circles,max_radius,current_circles=circles)
print extra_circles
###################
print "test : --- Write circles to file"
file_name = "board_setup.csv"
for c in extra_circles:
    circles.append(Circle.Circle(c.x,c.y,c.r,c="a"))
Tools.WriteCirclesToCSV(circles,file_name)
###################
print "test : --- done\n"