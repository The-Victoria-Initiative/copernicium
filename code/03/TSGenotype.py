from Genotype import Genotype
import copy

class TSGenotype(Genotype):

    def __init__(self,n_genes=False,n_bases=False,genes=False,name="0.0"):
        Genotype.__init__(self,n_genes=n_genes,n_bases=n_bases,genes=genes,name=name)

    def breed(self,mate,mutation_chance=1.):
        genes = []
        assert len(self.genes) == len(mate.genes), "Mismatched number of genes, self: %i, mate: %i"%(len(self.genes),len(mate.genes))
        for i in range(len(self.genes)):
            if (self.random() < mutation_chance): genes.append(copy.copy(self.genes[i]))
            else:                     genes.append(copy.copy(mate.genes[i]))
        offspring = TSGenotype(genes=genes)
        offspring.mutate()
        return offspring

    def eval(self):
        points = []
        for gene in self.genes:
            points.append(int(gene.code, 2))
        return points

    def to_string(self):
        to_return = ""
        for i,gene in enumerate(self.genes):
            if gene.code in gene_values.keys():
                to_return += "%4s "%gene_values[gene.code]
            else:
                to_return += " n/a "
        return to_return[:-1]
