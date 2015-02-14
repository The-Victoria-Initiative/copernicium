###################
print "run  : --- Match a pattern with a genetic algorithm"
###################
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-W", "--width",           help="width",                           action="store", type=int,   dest="width",           default=32)
parser.add_option("-H", "--height",          help="height",                          action="store", type=int,   dest="height",          default=32)
parser.add_option("-p", "--pattern",         help="pattern to draw",                 action="store", type=str,   dest="pattern",         default="square")
parser.add_option("-g", "--genotypes",       help="the number of genotypes",         action="store", type=int,   dest="genotypes",       default=10)
parser.add_option("-i", "--iteration_limit", help="limit the number of generations", action="store", type=int,   dest="max_generations", default=10)
parser.add_option("-m", "--mutation_chance", help="the mutation probability",        action="store", type=float, dest="mutation_chance", default=0.1)
parser.add_option("-a", "--always_best",     help="the fittest always breed",        action="store_true",        dest="always_best",     default=False)
parser.add_option("-l", "--parents_live",    help="the fittest always survive",      action="store_true",        dest="parents_live",    default=False)
parser.add_option("-v", "--verbose",         help="turn on verbose mode",            action="store_true",        dest="verbose",         default=False)
(options, args) = parser.parse_args()
if options.verbose:
    print "run  : --- Options"
    print "run  :     width:                    ",options.width 
    print "run  :     height:                   ",options.height
    print "run  :     pattern:                  ",options.pattern
    print "run  :     n genotypes:              ",options.genotypes
    print "run  :     maximum generations:      ",options.max_generations
    print "run  :     mutation probability:     ",options.mutation_chance
    print "run  :     fittest always survives:  ",options.always_best
    print "run  :     verbose:                  ",options.verbose
###################
import Canvas
import FitnessMeasures
import Line
import Population
import Tools
import time
###################
print "run  : generating an empty canvas"
canvas = Canvas.Canvas(options.width,options.height)
if options.pattern == "square":
  print "run  : Drawing a square on the board"
  canvas.add_line(Line.Line(10,10,                              options.width-10,10))
  canvas.add_line(Line.Line(options.width-10,10,                options.width-10,options.height-10))
  canvas.add_line(Line.Line(options.width-10,options.height-10, 10,options.height-10))
  canvas.add_line(Line.Line(10,options.height-10,               10,10))
  n_lines = 4
else:
  assert False, "Invalid pattern requested: %s"%options.pattern

file_name = "/zinc/web/copernicium/04/images/ideal.bmp"
canvas.save(file_name)
print "run  : Saved target canvas as: %s"%file_name
print "run  : Generating fitness measure"
fitness = FitnessMeasures.CanvasFitnessMeasure(canvas)

bases   = Tools.MinBases(max(options.width,options.height))
print "run  : max dimension: %i, bases: %i (2^%i = %i)"%(max(options.width,options.height),bases,bases,2**bases)
print "run  : --- Generate a population"
population = \
 Population.Population(fitness,
                       n_genotypes=options.genotypes,
                       n_genes=4*n_lines,
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
        best_result = max(population.fitness)
        print "run  :     generation[%i], best result: %.1f"%(generation,best_result)
        # print population

    if options.verbose: print "run  :     selecting fittest"
    fittest = population.select_fittest(force_always_best=True)[0]
    best_canvas = population.generate_canvas(fittest)
    # evolution.append((fittest,
    #                   max(population.fitness),
    #                   best_canvas,
    #                   fittest.genes))
    # if (best_result > threshold): break

    if options.verbose: print "run  :     fittest: %s"%(fittest.name)
    population.breed_next_generation()
    population.eval()
    
ga_end = time.time()
print population
best_result = max(population.fitness)
fittest = population.select_fittest(force_always_best=True)[0]
best_canvas = population.generate_canvas(fittest)
coding_used = fittest.genes
print "run  : final generation[%i], best result: %f"%(generation, best_result)
print "run  : solution: %s"%repr(fittest)
print "run  :           ",coding_used
print "run  :           ",best_canvas
print "run  : time taken: %.2f s"%(ga_end-ga_start)
# # ###################
# # print "run  : --- Brute force problem solving"
# # brute_start = time.time()
# # best_circle = Tools.SolveBoard(board,path,verbose=False)
# # brute_end   = time.time()
# # print "run  : solution: %s"%repr(best_circle)
# # print "run  : time taken: %.2f s"%(brute_end-brute_start)
###################
print "test : --- Best canvas to file"
file_name = "/zinc/web/copernicium/04/images/test.bmp"
best_canvas.save(file_name)

# print "run  : --- Write path to file"
# file_name = "path.csv"
# Tools.WritePathToFile(best_path,points,file_name)

# print "run  : --- Write scores to file"
# file_name = "evolution.json"
# Tools.WriteEvolutionToJSON(evolution,points,fitness,file_name)

# print "run  : --- Write genotype to file"
# file_name = "genotype.json"
# Tools.WriteGenotypeToJSON(fittest[0],file_name,coding=coding_used)

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