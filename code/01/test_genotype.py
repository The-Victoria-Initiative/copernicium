###################
print "test : --- Testing genotype"

###################
print "test : --- Generate a generic genotype"
import Genotype
genotype = Genotype.Genotype()
print genotype
print "test : ---"
###################
print "test : --- Generate a numerical genotype"
import NumericalGenotype
numerical_genotype = NumericalGenotype.NumericalGenotype()
print numerical_genotype
print "test : ---"
###################
print "test : --- Evaluate a genotype"
value = numerical_genotype.eval()
print value
print "test : ---"
###################
print "test : --- Test fitness"
target_value = 23.
import FitnessMeasures
fitness_measure = FitnessMeasures.NumericalFitnessMeasure(target_value)
print fitness_measure
score = fitness_measure.eval(value)
print "test : Genotype scored: %.2f"%score
print "test : ---"
###################
print "test : --- done\n"