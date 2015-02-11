###################
print "test : --- Testing genes"

###################
print "test : --- Generate a gene"
import Gene
gene = Gene.Gene(n_bases=100)
print gene
print "test : ---"
###################
print "test : --- Mutate a gene"
gene.mutate(mutation_chance=1.)
print gene
print "test : ---"
###################
print "test : --- Numerically Mutate a gene"
print gene, int(gene.code, 2)
gene.numerical_mutate(mutation_chance=1.)
print gene, int(gene.code, 2)
print "test : ---"
###################
print "test : --- done\n"