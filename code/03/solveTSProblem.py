###################
print "run  : --- Solving a travelling salesman problem with a genetic algorithm"
###################
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-W", "--width",           help="width",                           action="store", type=int,   dest="width",           default=400)
parser.add_option("-H", "--height",          help="height",                          action="store", type=int,   dest="height",          default=400)
parser.add_option("-p", "--points",          help="points",                          action="store", type=int,   dest="points",          default=20)
parser.add_option("-g", "--genotypes",       help="the number of genotypes",         action="store", type=int,   dest="genotypes",       default=10)
parser.add_option("-i", "--iteration_limit", help="limit the number of generations", action="store", type=int,   dest="max_generations", default=1000)
parser.add_option("-m", "--mutation_chance", help="the mutation probability",        action="store", type=float, dest="mutation_chance", default=0.1)
parser.add_option("-a", "--always_best",     help="the fittest always survive",      action="store_true",        dest="always_best",     default=False)
parser.add_option("-v", "--verbose",         help="turn on verbose mode",            action="store_true",        dest="verbose",         default=False)
(options, args) = parser.parse_args()
if options.verbose:
    print "run  : --- Options"
    print "run  :     width:                    ",options.width 
    print "run  :     height:                   ",options.height
    print "run  :     points:                   ",options.points
    print "run  :     n genotypes:              ",options.genotypes
    print "run  :     maximum generations:      ",options.max_generations
    print "run  :     mutation probability:     ",options.mutation_chance
    print "run  :     fittest always survives:  ",options.always_best
    print "run  :     verbose:                  ",options.verbose
###################
import Population
import FitnessMeasures
import Tools
import Point
# from math import sqrt
import time
###################
print "run  : --- Make points"
points = Tools.FillBoard(options.width,options.height,options.points)
print "run  :     ",points
fitness = FitnessMeasures.TSFitnessMeasure(points)
bases = Tools.MinBases(options.points)
print "run  : points: %i, bases: %i (2^%i = %i)"%(options.points,bases,bases,2**bases)
population = \
Population.Population(fitness,
                      n_genotypes=options.genotypes,
                      n_genes=options.points*2,
                      n_bases=bases,
                      mutation_chance=options.mutation_chance,
                      always_best=options.always_best,
                      verbose=options.verbose)
generation = 0
evolution  = []
###################
print "run  : --- Running"
ga_start = time.time()
while(True):
    generation +=1
    if (options.max_generations != -1) and (generation > options.max_generations): break
    
    if options.verbose or (generation%100 == 0):
        print "run  :     generation[%i]"%generation
        best_result = max(population.fitness)
        print "run  :     best result: %f"%best_result
        print population

    if options.verbose: print "run  :     selecting fittest"
    fittest = population.select_fittest()
    evolution.append((fittest[0],
                     (1. / (max(population.fitness))),
                     fitness.eval((fittest[0].eval()),return_coding=True)))
    # if (best_result > threshold): break

    if options.verbose: print "run  :     breeding: %s and %s"%(fittest[0].name,fittest[1].name)
    population.breed_next_generation(fittest)
    population.eval()
    
ga_end = time.time()
print population
best_result = max(population.fitness)
fittest = population.select_fittest()
best_path   = fitness.eval((fittest[0].eval()))[1]
coding_used = fitness.eval((fittest[0].eval()),return_coding=True)
print "run  : final generation[%i], best result: %f"%(generation, 1. / best_result)
print "run  : solution: %s"%repr(fittest[0])
print "run  :           ",coding_used
print "run  :           ",best_path
print "run  : time taken: %.2f s"%(ga_end-ga_start)
# ###################
# print "run  : --- Brute force problem solving"
# brute_start = time.time()
# best_circle = Tools.SolveBoard(board,path,verbose=False)
# brute_end   = time.time()
# print "run  : solution: %s"%repr(best_circle)
# print "run  : time taken: %.2f s"%(brute_end-brute_start)
###################
print "test : --- Write points to file"
file_name = "board_setup.csv"
Tools.WritePointsToCSV(points,file_name)

print "run  : --- Write path to file"
file_name = "path.csv"
Tools.WritePathToFile(best_path,points,file_name)

print "run  : --- Write scores to file"
file_name = "evolution.json"
Tools.WriteEvolutionToJSON(evolution,points,fitness,file_name)

print "run  : --- Write genotype to file"
file_name = "genotype.json"
Tools.WriteGenotypeToJSON(fittest[0],file_name,coding=coding_used)

# print "run  : --- Write evolution of path to file"
# file_name = "evolution.csv"
# Tools.WriteCirclesToCSV(best_path,file_name,scores=scores)

# print "run  : --- Write parameters to file"
# file_name = "parameters.csv"
# Tools.WriteParametersToFile(options,file_name)

# print "run  : --- Write results to files"
# results = {
#     "GA result":repr(fittest[0].eval())[:-4],
#     "GA time"  :"%.2f s"%(ga_end-ga_start),
#     "GA score" :"%.2f"%sqrt(best_result),
#     "Brute force circle":repr(best_circle)[:-4],
#     "Brute force Time"       :"%.2f s"%(brute_end-brute_start),
#     "Brute force score" :"%.2f"%best_circle.r
# }
# file_name = "results.json"
# import json
# with open(file_name, 'wb') as fp: json.dump(results, fp)
###################
print "run  : --- done\n"