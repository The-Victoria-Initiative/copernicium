###################
print "run  : --- Solving a circle problem with a genetic algorithm"
###################
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-i", "--iteration_limit", help="limit the number of generations", action="store", type=int, dest="max_generations", default=1000)
parser.add_option("-v", "--verbose",         help="turn on verbose mode",            action="store_true",      dest="verbose",         default=False)
(options, args) = parser.parse_args()
###################
import Population
import FitnessMeasures
import Tools
import Board
import Circle
###################
print "run  : --- Make board"
width  = 400
height = 400
board = Board.Board(width,height,verbose=options.verbose)
print "run  :     ",board
n_circles  = 20
max_radius = 30
circles = Tools.FillBoard(board,n_circles,max_radius)
print "run  :     ",circles
fitness_measure = FitnessMeasures.CircleFitnessMeasure(board,circles)
population = Population.Population(fitness_measure, n_genotypes=20)
generation = 0
best_circles = []
scores       = []
###################
print "run  : --- Running"
while(True):
    generation +=1
    if (options.max_generations != -1) and (generation >= options.max_generations): break
    
    if options.verbose or (generation%1000 == 0):
        print "run  :     generation[%i]"%generation
        best_result = max(population.fitness)
        print "run  :     best result: %f"%best_result
        print population

    if options.verbose: print "run  :     selecting fittest"
    fittest = population.select_fittest()
    best_circles.append(fittest[0].eval())
    scores.append(max(population.fitness))
    # if (best_result > threshold): break

    if options.verbose: print "run  :     breeding: %s and %s"%(fittest[0].name,fittest[1].name)
    population.breed_next_generation(fittest)
    population.eval()
    

best_result = max(population.fitness)
print "run  : final generation[%i], best result: %f"%(generation, best_result)
print "run  : solution: %s"%repr(fittest[0]),fittest[0].eval()
###################
print "run  : --- Write circles to file"
file_name = "board_setup.csv"
circles.append(fittest[0].eval())
Tools.WriteCirclesToCSV(circles,file_name)

print "run  : --- Write evolution of circles to file"
file_name = "evolution.csv"
Tools.WriteCirclesToCSV(best_circles,file_name,scores=scores)
###################
print "run  : --- done\n"