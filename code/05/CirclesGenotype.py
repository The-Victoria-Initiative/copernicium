from Genotype import Genotype
from Circle import Circle
import copy

class CirclesGenotype(Genotype):

    def __init__(self,n_genes=6,n_bases=False,genes=False,name="0.0",colour_scale=1):
        self.colour_scale = colour_scale
        Genotype.__init__(self,n_genes=n_genes,n_bases=n_bases,genes=genes,name=name)

    def breed(self,mate,mutation_chance=1.):
        genes = []
        assert len(self.genes) == len(mate.genes), "Mismatched number of genes, self: %i, mate: %i"%(len(self.genes),len(mate.genes))
        for i in range(len(self.genes)):
            if (self.random() < mutation_chance): genes.append(copy.copy(self.genes[i]))
            else:                     genes.append(copy.copy(mate.genes[i]))
        offspring = CirclesGenotype(genes=genes,colour_scale=self.colour_scale)
        offspring.numerical_mutate(mutation_chance=mutation_chance)
        return offspring

    def eval(self,rainbow=False):
        circles = []
        j = 0
        for i in range(0,len(self.genes),6):
            colour = "steelblue"
            colour = (int(self.genes[i+3].code, 2)*self.colour_scale,
                      int(self.genes[i+4].code, 2)*self.colour_scale,
                      int(self.genes[i+5].code, 2)*self.colour_scale)
            circles.append(Circle(int(self.genes[i+0].code, 2),
                                  int(self.genes[i+1].code, 2),
                                  int(self.genes[i+2].code, 2)/(4*self.colour_scale),
                                  name=self.name+".%i"%j,
                                  radius_limit = 32/self.colour_scale,
                                  colour=colour))
            j += 1
        return circles

    def to_string(self):
        to_return = ""
        for i in range(0,len(self.genes),4):
            to_return += "(x1: %i, y1: %i), (x2: %i, y2: %i)\n"%\
            (int(self.genes[0].code, 2),int(self.genes[1].code, 2),int(self.genes[2].code, 2),int(self.genes[3].code, 2))
        return to_return[:-1]
