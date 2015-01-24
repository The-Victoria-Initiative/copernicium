###################
print "run  : --- Solving a numerical problem with a genetic algorithm"
###################
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-i", "--iteration_limit", help="limit the number of generations", action="store", type=int, dest="max_generations", default=1000)
parser.add_option("-v", "--verbose",         help="turn on verbose mode",            action="store_true",      dest="verbose",         default=False)
(options, args) = parser.parse_args()
import Population
import FitnessMeasures

population = Population.Population(n_genotypes=10)
generation = 0

target_value = 124
threshold    = 2.
print "run  : Target value = %f"%target_value
fitness_measure = FitnessMeasures.NumericalFitnessMeasure(target_value)
while(True):
    if (options.max_generations != -1) and (generation > options.max_generations): break
    population.eval(fitness_measure)
    best_result = max(population.fitness)
    if options.verbose or (generation%1000 == 0):
        print population
        print "run  :     generation[%i], best result: %f"%(generation, best_result)

    fittest = population.select_fittest()
    if (best_result > threshold): break

    if options.verbose: print "run  :     breeding: %s and %s"%(fittest[0].name,fittest[1].name)
    population.breed_next_generation(fittest)
    generation +=1

print "run  : final generation[%i], best result: %f"%(generation, best_result)
print "run  : solution: %s"%repr(fittest[0])
print "run  :  %s"%fittest[0].to_string()
print "run  :  %s"%fittest[0].eval(return_string=True)
###################
print "run  : --- done\n"