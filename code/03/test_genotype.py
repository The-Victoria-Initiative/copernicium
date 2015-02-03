###################
print "test : --- Testing genotype"

###################
print "test : --- Generate a generic genotype"
import Genotype
genotype = Genotype.Genotype()
print genotype
print "test : ---"
###################
print "test : --- Generate a TS genotype"
import TSGenotype
ts_genotype = TSGenotype.TSGenotype(n_bases=4,n_genes=2)
print ts_genotype
print "test : ---"
###################
print "test : --- Evaluate a genotype"
value = ts_genotype.eval()
print value
print "test : ---"
###################
print "test : --- done\n"