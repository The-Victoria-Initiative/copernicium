class Population():
    from NumericalGenotype import NumericalGenotype
    from random import random

    def __init__(self, n_genotypes=8, verbose=True):
        self.verbose = verbose
        self.n_genotypes = n_genotypes
        self.generation = 0
        self.fitness = []
        self.values = []
        self.generate_population()
        self.eval_population()

    def generate_population(self):
        genotypes = []
        for i in range(self.n_genotypes):
            genotypes.append(self.NumericalGenotype(name="0.%i"%i))
            self.fitness.append(0)
            self.values.append(0)
        self.genotypes = genotypes

    def eval_population(self):
        for i,g in enumerate(self.genotypes):
            self.values[i] = g.eval()

    def eval(self,fitness_measure):
        for i in range(self.n_genotypes):
            self.fitness[i] = fitness_measure.eval(self.values[i])

    def select_fittest(self):
        self.make_fitness_bins()
        # select first candidate
        first_candidate = self.pick_candidate()
        assert first_candidate is not False, "No first candidate was selected"
        
        second_candidate = first_candidate
        while (second_candidate == first_candidate):
            second_candidate = self.pick_candidate()
        assert second_candidate is not False, "No second candidate was selected"

        return self.genotypes[first_candidate], self.genotypes[second_candidate]

    def pick_candidate(self):
        score = self.random()*self.fitness_bins[-1]
        candidate = False
        for i in range(len(self.fitness_bins)-1):
            if (score > self.fitness_bins[i]) and (score <= self.fitness_bins[i+1]):
                candidate = i
                break
        return candidate

    def make_fitness_bins(self):
        bins = [0]
        for f in self.fitness:
            bin_edge = bins[-1]+(f*f)
            bins.append(bin_edge)
        self.fitness_bins = bins

    def breed(self, genotypes):
        return genotypes[0].breed(genotypes[1])

    def breed_next_generation(self,genotypes):
        next_generation = []
        self.generation += 1
        for i in range(self.n_genotypes):
            next_generation.append(self.breed(genotypes))
            next_generation[i].name = "%i.%i"%(self.generation,i)
            # print next_generation[i]
        # print next_generation
        # print self.genotypes
        self.genotypes = next_generation
        # print self.genotypes
        self.eval_population()

    def __repr__(self):
        to_return = "pop  : %i genotypes\n"%self.n_genotypes
        for i,g in enumerate(self.genotypes):
            to_return += "%s, s: %.2f, f: %.5f\n"%(repr(g),self.values[i], self.fitness[i])
        return to_return[:-1]