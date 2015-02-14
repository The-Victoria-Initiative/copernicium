###################
print "run  : --- Match a pattern with a genetic algorithm"
###################
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-p", "--pattern",         help="pattern to draw",                 action="store", type=str,   dest="pattern",         default="jess_128")
parser.add_option("-s", "--suffix",          help="save suffix",                     action="store", type=str,   dest="suffix",          default="default")
parser.add_option("-g", "--genotypes",       help="the number of genotypes",         action="store", type=int,   dest="genotypes",       default=10)
parser.add_option("-c", "--circles",         help="the number of circles",           action="store", type=int,   dest="circles",         default=10)
parser.add_option("-i", "--iteration_limit", help="limit the number of generations", action="store", type=int,   dest="max_generations", default=10)
parser.add_option("-t", "--time_limit",      help="time limit in seconds",           action="store", type=int,   dest="time_limit",      default=False)
parser.add_option("-m", "--mutation_chance", help="the mutation probability",        action="store", type=float, dest="mutation_chance", default=0.1)
parser.add_option("-a", "--always_best",     help="the fittest always breed",        action="store_true",        dest="always_best",     default=False)
parser.add_option("-l", "--parents_live",    help="the fittest always survive",      action="store_true",        dest="parents_live",    default=False)
parser.add_option("-v", "--verbose",         help="turn on verbose mode",            action="store_true",        dest="verbose",         default=False)
(options, args) = parser.parse_args()
if options.verbose:
    print "run  : --- Options"
    print "run  :     pattern:                  ",options.pattern
    print "run  :     n genotypes:              ",options.genotypes
    print "run  :     n circles:                ",options.circles
    print "run  :     time limit [s]:           ",options.time_limit
    print "run  :     maximum generations:      ",options.max_generations
    print "run  :     mutation probability:     ",options.mutation_chance
    print "run  :     fittest always survives:  ",options.always_best
    print "run  :     suffix:                   ",options.suffix
    print "run  :     verbose:                  ",options.verbose
###################
import Canvas
import FitnessMeasures
import Circle
import Population
import Tools
import time
###################
if options.pattern == "jess":
  print "run  : Drawing a 256 Jess on the board"
  options.width  = 256
  options.height = 256
  canvas = Canvas.Canvas(options.width,options.height,image="Image.bmp")
  colour_scale   = 1
elif options.pattern == "jess_128":
  print "run  : Drawing a 128 Jess on the board"
  options.width  = 128
  options.height = 128
  canvas = Canvas.Canvas(options.width,options.height,image="Image_128.bmp")
  colour_scale   = 2
else:
  assert False, "Invalid pattern requested: %s"%options.pattern

print "run  : Generating fitness measure"
fitness = FitnessMeasures.CanvasFitnessMeasure(canvas)

bases   = Tools.MinBases(options.width)
print "run  : max dimension: %i, bases: %i (2^%i = %i)"%(max(options.width,options.height),bases,bases,2**bases)
print "run  : --- Generate a population"
population = \
 Population.Population(fitness,
                       n_genotypes=options.genotypes,
                       n_genes=6*options.circles,
                       n_bases=bases,
                       mutation_chance=options.mutation_chance,
                       always_best=options.always_best,
                       colour_scale=colour_scale,
                       verbose=options.verbose)
generation = 0
evolution  = []
###################
print "run  : --- Running"
ga_start = time.time()
while(True):
    generation +=1
    dt = time.time() - ga_start
    if ((options.max_generations != -1) and (generation > options.max_generations)) or\
       (options.time_limit and (dt > options.time_limit)): break
    
    if options.verbose or (generation%10 == 0):
        best_result = max(population.fitness)
        print "run  :     generation[%i], best result: %.1f, time: %.1f s"%(generation,best_result,dt)
        # print population

    if options.verbose: print "run  :     selecting fittest"
    fittest = population.select_fittest(force_always_best=True)[0]
    best_canvas = population.generate_canvas(fittest)
    #evolution.append((fittest,
    #                  max(population.fitness),
    #                  best_canvas,
    #                  fittest.genes))
    # if (best_result > threshold): break

    if options.verbose: print "run  :     fittest: %s"%(fittest.name)
    population.breed_next_generation()
    population.eval()
    
ga_end = time.time()
# print population
best_result = max(population.fitness)
fittest = population.select_fittest(force_always_best=True)[0]
best_canvas = population.generate_canvas(fittest)
coding_used = fittest.genes
print "run  : final generation[%i], best result: %.1f"%(generation, best_result)
# print "run  : solution: %s"%repr(fittest)
# print "run  :           ",coding_used
# print "run  :           ",best_canvas
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
file_name = "/zinc/web/copernicium/05/images/test_%s.bmp"%options.suffix
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
