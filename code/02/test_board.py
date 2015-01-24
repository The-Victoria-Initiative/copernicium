###################
print "test : --- Testing board"
import Board
###################
print "test : --- Test filling board"
width  = 400
height = 400
board = Board.Board(width,height,verbose=True)
print board
print "test : ---"
###################
print "test : --- Test if a circle is on the board"
import Circle
circle = Circle.Circle(1,288,1)
print circle, board.contained(circle)
print "test : ---"
###################
print "test : --- Get containment"
import Circle
circle = Circle.Circle(-10,288,1)
print circle, board.containment(circle)
print "test : ---"
###################
print "test : --- done\n"