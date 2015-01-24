###################
print "test : --- Testing genes"

###################
print "test : --- Generate a gene"
import Gene
gene = Gene.Gene()
print gene
print "test : ---"
###################
print "test : --- Mutate a gene"
gene.mutate(mutation_chance=1.)
print gene
print "test : ---"
###################
print "test : --- done\n"