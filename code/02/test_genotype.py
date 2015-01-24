###################
print "test : --- Testing genotype"

###################
print "test : --- Generate a generic genotype"
import Genotype
genotype = Genotype.Genotype()
print genotype
print "test : ---"
###################
print "test : --- Generate a circle genotype"
import CircleGenotype
circle_genotype = CircleGenotype.CircleGenotype()
print circle_genotype
print "test : ---"
###################
print "test : --- Evaluate a genotype"
value = circle_genotype.eval()
print value
print "test : ---"

###################
print "test : --- done\n"