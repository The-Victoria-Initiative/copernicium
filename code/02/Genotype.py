class Genotype():
    from Gene import Gene
    from random import random

    def __init__(self, name="0.0", n_genes=3, genes=False, verbose=False):
        self.verbose = verbose
        self.n_genes = n_genes
        self.name = name
        if genes:
            self.genes = genes
        else:
            self.generate_genotype()

    def generate_genotype(self):
        """
        A genotype consists of a string of n_genes
        """
        genes = []
        for i in range(self.n_genes):
            genes.append(self.Gene())
        self.genes = genes

    def mutate(self,mutation_chance=0.01):
        for i in range(len(self.genes)):
            # print i
            self.genes[i].mutate(mutation_chance=mutation_chance)

    def numerical_mutate(self,mutation_chance=0.2,width=0.1,relative_width=True):
        for i in range(len(self.genes)):
            # print i
            self.genes[i].numerical_mutate(mutation_chance=mutation_chance,width=width,relative_width=relative_width)

    def __repr__(self):
        return "genot: %s, %i genes: %s"%(self.name,self.n_genes,repr(self.genes))