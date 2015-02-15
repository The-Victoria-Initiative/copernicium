from Genotype import Genotype
from Colour import Colour
import copy

class ColoursGenotype(Genotype):

    def __init__(self,n_genes=6,n_bases=False,genes=False,name="0.0"):
        Genotype.__init__(self,n_genes=n_genes,n_bases=n_bases,genes=genes,name=name)

    def breed(self,mate,mutation_chance=1.):
        genes = []
        assert len(self.genes) == len(mate.genes), "Mismatched number of genes, self: %i, mate: %i"%(len(self.genes),len(mate.genes))
        for i in range(len(self.genes)):
            if (self.random() < mutation_chance): 
              genes.append(copy.copy(self.genes[i]))
            else:                     
              genes.append(copy.copy(mate.genes[i]))
        offspring = ColoursGenotype(genes=genes)
        offspring.numerical_mutate(mutation_chance=mutation_chance)
        return offspring

    def eval(self):
        pixels = []
        j = 0
        for i in range(0,len(self.genes),3):
            colour = "steelblue"
            colour = (int(self.genes[i+0].code, 2),
                      int(self.genes[i+1].code, 2),
                      int(self.genes[i+2].code, 2))
            pixels.append(Colour(colour, name=self.name+".%i"%j))
            j += 1
        return pixels

    def to_string(self):
        to_return = ""
        for i in range(0,len(self.genes),3):
            to_return += "(%i,%i,%i)\n"%\
            (int(self.genes[0].code, 2),int(self.genes[1].code, 2),int(self.genes[2].code, 2))
        return to_return[:-1]
