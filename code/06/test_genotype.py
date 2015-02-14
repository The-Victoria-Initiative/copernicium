###################
print "test : --- Testing genotype"

###################
print "test : --- Generate a generic genotype"
import Genotype
genotype = Genotype.Genotype()
print genotype
print "test : ---"
###################
print "test : --- Generate a Lines genotype"
import LinesGenotype
lines_genotype = LinesGenotype.LinesGenotype(n_bases=4,n_genes=12)
print lines_genotype
print lines_genotype.to_string()
print "test : ---"
##################
print "test : --- Evaluate a genotype"
value = lines_genotype.eval()
print value
print "test : ---"
###################
print "test : --- done\n"