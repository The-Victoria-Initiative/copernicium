###################
print "test : --- Testing a population"
import Board
import FitnessMeasures
import Tools
import Circle
import Population
###################

width  = 400
height = 400
board = Board.Board(width,height,verbose=True)
print board
n_circles  = 20
max_radius = 30
circles = Tools.FillBoard(board,n_circles,max_radius)
print circles

fitness_measure = FitnessMeasures.CircleFitnessMeasure(board,circles,verbose=True)

print "test : --- Generate a population"
population = Population.Population(fitness_measure)
print population
print "test : ---"
###################
print "test : --- Select fittest"
fittest = population.select_fittest()
for f in fittest:
    print f, f.eval()
print "test : ---"
###################
print "test : --- Breed the an example of the next generation"
next_gen = population.breed(fittest)
print next_gen
print "test : ---"
###################
print "test : --- Breed the next generation"
population.breed_next_generation(fittest)
population.eval()
print population
print "test : ---"
# ###################
print "test : --- done\n"