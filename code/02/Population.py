class Population():
    from CircleGenotype import CircleGenotype
    from Gene import Gene
    from random import random
    import Tools

    def __init__(self, fitness_measure, n_genotypes=8, verbose=True):
        self.verbose     = verbose
        self.fitness_measure = fitness_measure
        self.n_genotypes = n_genotypes
        self.generation  = 0
        self.fitness     = []
        self.fitness_pairs = []
        self.generate_population()
        self.eval()
        while (max(self.fitness) < 1):
            self.generate_population()
            self.eval()

    def generate_population(self):
        genotypes = []
        seed_circles = self.Tools.FillBoard(self.fitness_measure.board,self.n_genotypes,30)

        for i in range(self.n_genotypes):
            genes = []
            genes.append(self.Gene(code='{0:09b}'.format(int(seed_circles[i].x))))
            genes.append(self.Gene(code='{0:09b}'.format(int(seed_circles[i].y))))
            genes.append(self.Gene(code='{0:09b}'.format(int(seed_circles[i].r))))

            genotypes.append(self.CircleGenotype(genes=genes, name="0.%i"%i))
            self.fitness.append(0)
            self.fitness_pairs.append(0)
        self.genotypes = genotypes

    
    def eval(self):
        for i in range(self.n_genotypes):
            self.fitness[i] = self.fitness_measure.eval(self.genotypes[i].eval())
            self.fitness_pairs[i] = (self.fitness[i],i)

    def select_fittest(self,always_best=True):
        self.make_fitness_bins()

        if always_best:
            self.fitness_pairs.sort()
            first_candidate = self.fitness_pairs[-1][1]
            # second_candidate = self.fitness_pairs[-2][1]
            second_candidate = self.pick_candidate()
        else:
            first_candidate = self.pick_candidate()
            assert first_candidate is not False, "No first candidate was selected"
            
            second_candidate = first_candidate
            # while (second_candidate == first_candidate):
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

    def make_fitness_bins(self, exclude=False):
        bins = [0]
        for f in self.fitness:
            bin_edge = bins[-1]+(f*f)
            bins.append(bin_edge)
        self.fitness_bins = bins

    def breed(self, genotypes):
        return genotypes[0].breed(genotypes[1])

    def breed_next_generation(self,genotypes,parents_live=True):
        # print genotypes
        next_generation = []
        offset = 0
        if parents_live:
            offset = 2
            next_generation.append(genotypes[0])
            next_generation.append(genotypes[1])

        self.generation += 1
        for i in range(self.n_genotypes-offset):
            next_generation.append(self.breed(genotypes))
            next_generation[i+offset].name = "%i.%i"%(self.generation,i+offset)
            # print next_generation[i]
        # print next_generation
        # print self.genotypes
        self.genotypes = next_generation
        # print self.genotypes
        self.eval()

    def __repr__(self):
        to_return = "pop  : %i genotypes\n"%self.n_genotypes
        for i,g in enumerate(self.genotypes):
            to_return += "%s, f: %.5f\n"%(g.eval(), self.fitness[i])
        return to_return[:-1]