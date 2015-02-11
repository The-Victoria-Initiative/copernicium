from Genotype import Genotype
from Line import Line
import copy

class LinesGenotype(Genotype):

    def __init__(self,n_genes=4,n_bases=False,genes=False,name="0.0"):
        Genotype.__init__(self,n_genes=n_genes,n_bases=n_bases,genes=genes,name=name)

    def breed(self,mate,mutation_chance=1.):
        genes = []
        assert len(self.genes) == len(mate.genes), "Mismatched number of genes, self: %i, mate: %i"%(len(self.genes),len(mate.genes))
        for i in range(len(self.genes)):
            if (self.random() < mutation_chance): genes.append(copy.copy(self.genes[i]))
            else:                     genes.append(copy.copy(mate.genes[i]))
        offspring = LinesGenotype(genes=genes)
        offspring.mutate()
        return offspring

    def eval(self,rainbow=False):
        lines = []
        j = 0
        colours = ["red","green","blue","yellow"]
        for i in range(0,len(self.genes),4):
            colour = "steelblue"
            if rainbow: colour = colours[i/4]
            lines.append(Line(int(self.genes[i+0].code, 2),
                              int(self.genes[i+1].code, 2),
                              int(self.genes[i+2].code, 2),
                              int(self.genes[i+3].code, 2),
                              name=self.name+".%i"%j,
                              colour=colour))
            j += 1
        return lines

    def to_string(self):
        to_return = ""
        for i in range(0,len(self.genes),4):
            to_return += "(x1: %i, y1: %i), (x2: %i, y2: %i)\n"%\
            (int(self.genes[0].code, 2),int(self.genes[1].code, 2),int(self.genes[2].code, 2),int(self.genes[3].code, 2))
        return to_return[:-1]
