from Genotype import Genotype
from Circle import Circle
import copy

class CircleGenotype(Genotype):

    def __init__(self,genes=False,name="0.0"):
        Genotype.__init__(self,genes=genes,name=name)
        self.name = name

    def eval(self):
        """
        evaluate our genotype as circle

        """
        x_code = self.genes[0].code
        y_code = self.genes[1].code
        r_code = self.genes[2].code
        return Circle(int(x_code, 2), int(y_code, 2), int(r_code, 2),name=self.name,c="a")

    def breed(self,mate):
        genes = []
        assert len(self.genes) == len(mate.genes), "Mismatched number of genes, self: %i, mate: %i"%(len(self.genes),len(mate.genes))
        for i in range(len(self.genes)):
            if (self.random() < 0.5): genes.append(copy.copy(self.genes[i]))
            else:                     genes.append(copy.copy(mate.genes[i]))
        offspring = CircleGenotype(genes=genes)
        offspring.numerical_mutate()
        return offspring
