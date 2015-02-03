class Population():
    from TSGenotype import TSGenotype
    from Gene import Gene
    from random import random, shuffle
    import Tools

    def __init__(self, fitness_measure, 
                 n_genotypes=8, n_genes=2, n_bases=5, 
                 always_best=False, 
                 mutation_chance=0.2, 
                 verbose=True):
        # Parameters
        self.verbose         = verbose
        self.fitness_measure = fitness_measure
        self.n_genotypes     = n_genotypes
        self.n_genes         = n_genes
        self.n_bases         = n_bases
        self.always_best     = always_best
        self.mutation_chance = mutation_chance
        # Counters etc
        self.generation      = 0
        self.fitness         = []
        self.fitness_pairs   = []
        self.orders          = []
        self.generate_population()
        self.eval()
        while (max(self.fitness) <= (1. / 1e12)):
            self.generate_population()
            self.eval()
        print "pop  : Seed found"

    def generate_population(self,shuffle=True):
        genotypes = []
        self.fitness         = []
        self.fitness_pairs   = []
        self.orders          = []
        for i in range(self.n_genotypes):
            if shuffle:
                seeds = []
                for i in range(len(self.fitness_measure.points)):
                    seeds.append(i)
                for i in range(len(self.fitness_measure.points),self.n_genes):
                    seeds.append(int(self.random()*len(self.fitness_measure.points)))
                self.shuffle(seeds)
                genes = []
                for s in seeds:
                    genes.append(self.Gene(code=('{0:0%ib}'%self.n_bases).format(int(s))))
                genotypes.append(self.TSGenotype(genes=genes, name="0.%i"%i))
                # print genotypes
                # assert False
            else:
                genotypes.append(self.TSGenotype(n_genes=self.n_genes, n_bases=self.n_bases, name="0.%i"%i))
            self.fitness.append(1./1e12)
            self.fitness_pairs.append(0)
            self.orders.append([])
        self.genotypes = genotypes
    
    def eval(self):
        for i in range(self.n_genotypes):
            self.fitness[i], self.orders[i] = self.fitness_measure.eval(self.genotypes[i].eval())
            self.fitness_pairs[i] = (self.fitness[i],i)

    def select_fittest(self):
        self.make_fitness_bins()

        if self.always_best:
            self.fitness_pairs.sort()
            # print self.fitness_pairs
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
        return genotypes[0].breed(genotypes[1], mutation_chance=self.mutation_chance)

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
            # to_return += "%s\n"%(repr(g))
            to_return += "%s, f: %.5f, %s\n"%(g.name, self.fitness[i], self.orders[i])
        return to_return[:-1]