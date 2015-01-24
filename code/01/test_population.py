###################
print "test : --- Testing a population"

###################
print "test : --- Generate a population"
import Population
population = Population.Population()
print population
print "test : ---"
###################
print "test : --- Test fitness"
target_value = 23.
import FitnessMeasures
fitness_measure = FitnessMeasures.NumericalFitnessMeasure(target_value)
print fitness_measure
population.eval(fitness_measure)
print population
print "test : ---"
###################
print "test : --- Select fittest"
fittest = population.select_fittest()
print fittest
print "test : ---"
###################
print "test : --- Breed the an example of the next generation"
next_gen = population.breed(fittest)
print next_gen
print "test : ---"
###################
print "test : --- Breed the next generation"
population.breed_next_generation(fittest)
population.eval(fitness_measure)
print population
print "test : ---"
###################
print "test : --- done\n"