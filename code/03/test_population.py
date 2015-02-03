###################
print "test : --- Testing a population"
import Tools
import Point
import Population
import FitnessMeasures
###################
width  = 400
height = 400
n_points  = 5
print "test : Generating %i points"%n_points
points = Tools.FillBoard(width,height,n_points)
print points
fitness = FitnessMeasures.TSFitnessMeasure(points)
bases = Tools.MinBases(n_points)
print "test : points: %i, bases: %i (2^%i = %i)"%(n_points,bases,bases,2**bases)


print "test : --- Generate a population"
population = Population.Population(fitness,n_genotypes=20,n_genes=n_points*2,n_bases=bases)
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