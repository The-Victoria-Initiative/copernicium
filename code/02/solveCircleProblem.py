###################
print "run  : --- Solving a circle problem with a genetic algorithm"
###################
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-W", "--width",           help="board width",                     action="store", type=int,   dest="board_width",     default=400)
parser.add_option("-H", "--height",          help="board height",                    action="store", type=int,   dest="board_height",    default=400)
parser.add_option("-C", "--circles",         help="board circles",                   action="store", type=int,   dest="circles",         default=20)
parser.add_option("-R", "--radius",          help="board radius",                    action="store", type=int,   dest="radius",          default=30)
parser.add_option("-G", "--genotypes",       help="the number of genotypes",         action="store", type=int,   dest="genotypes",       default=10)
parser.add_option("-i", "--iteration_limit", help="limit the number of generations", action="store", type=int,   dest="max_generations", default=1000)
parser.add_option("-m", "--mutation_chance", help="the mutation probability",        action="store", type=float, dest="mutation_chance", default=0.2)
parser.add_option("-w", "--mutation_width",  help="the mutation Gaussian width",     action="store", type=float, dest="mutation_width",  default=0.1)
parser.add_option("-r", "--relative_width",  help="make mutation width relative",    action="store_true",        dest="relative_width",  default=True)
parser.add_option("-a", "--always_best",     help="the fittest always survive",      action="store_true",        dest="always_best",     default=False)
parser.add_option("-v", "--verbose",         help="turn on verbose mode",            action="store_true",        dest="verbose",         default=False)
(options, args) = parser.parse_args()
if options.verbose:
    print "run  : --- Options"
    print "run  :     board width:              ",options.board_width 
    print "run  :     board height:             ",options.board_height
    print "run  :     board circles:            ",options.circles
    print "run  :     initial radius:           ",options.radius
    print "run  :     n genotypes:              ",options.genotypes
    print "run  :     maximum generations:      ",options.max_generations
    print "run  :     mutation probability:     ",options.mutation_chance
    print "run  :     mutation width:           ",options.mutation_width
    print "run  :     fittest always survives:  ",options.always_best
    print "run  :     verbose:                  ",options.verbose
###################
import Population
import FitnessMeasures
import Tools
import Board
import Circle
from math import sqrt
import time
###################
print "run  : --- Make board"
board = Board.Board(options.board_width,options.board_height,verbose=options.verbose)
print "run  :     ",board
circles = Tools.FillBoard(board,options.circles,options.radius)
print "run  :     ",circles
fitness_measure = FitnessMeasures.CircleFitnessMeasure(board,circles)
population = \
Population.Population(fitness_measure, options.genotypes, 
                      always_best=options.always_best, 
                      mutation_chance=options.mutation_chance, 
                      width=options.mutation_width, 
                      relative_width=options.relative_width, 
                      verbose=options.verbose)
generation = 0
best_circles = []
scores       = []
###################
print "run  : --- Running"
ga_start = time.time()
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
    scores.append(sqrt(max(population.fitness)))
    # if (best_result > threshold): break

    if options.verbose: print "run  :     breeding: %s and %s"%(fittest[0].name,fittest[1].name)
    population.breed_next_generation(fittest)
    population.eval()
    
ga_end = time.time()
best_result = max(population.fitness)
print "run  : final generation[%i], best result: %f"%(generation, best_result)
print "run  : solution: %s"%repr(fittest[0])
print "run  :           ",fittest[0].eval()
print "run  : time taken: %.2f s"%(ga_end-ga_start)
###################
print "run  : --- Brute force problem solving"
brute_start = time.time()
best_circle = Tools.SolveBoard(board,circles,verbose=False)
brute_end   = time.time()
print "run  : solution: %s"%repr(best_circle)
print "run  : time taken: %.2f s"%(brute_end-brute_start)
###################
print "run  : --- Write circles to file"
file_name = "board_setup.csv"
circles.append(fittest[0].eval())
circles.append(best_circle)
Tools.WriteCirclesToCSV(circles,file_name)

print "run  : --- Write evolution of circles to file"
file_name = "evolution.csv"
Tools.WriteCirclesToCSV(best_circles,file_name,scores=scores)

print "run  : --- Write parameters to file"
file_name = "parameters.csv"
Tools.WriteParametersToFile(options,file_name)

print "run  : --- Write results to files"
results = {
    "GA result":repr(fittest[0].eval())[:-4],
    "GA time"  :"%.2f s"%(ga_end-ga_start),
    "GA score" :"%.2f"%sqrt(best_result),
    "Brute force circle":repr(best_circle)[:-4],
    "Brute force Time"       :"%.2f s"%(brute_end-brute_start),
    "Brute force score" :"%.2f"%best_circle.r
}
file_name = "results.json"
import json
with open(file_name, 'wb') as fp: json.dump(results, fp)
###################
print "run  : --- done\n"