class Gene():
    from random import random, gauss

    def __init__(self, n_bases=9, code=False, verbose=True):
        self.verbose = verbose
        self.n_bases = n_bases
        if not code:
            self.generate_gene()
        else:
            self.code = code
            self.n_bases = len(code)

    def generate_gene(self):
        code = ""
        for i in range(self.n_bases):
            if self.random() < 0.5: code = code + "0"
            else:                   code = code + "1"
        self.code = code

    def mutate(self,mutation_chance=0.1):
        for i in range(self.n_bases):
            r = self.random()
            if r > mutation_chance: continue
            # print "mutation on base %i"%i
            if self.code[i] == "0":
                tmp = self.code[:i]+"1"+self.code[i+1:]
            else:
                tmp = self.code[:i]+"0"+self.code[i+1:]
            self.code = tmp

    def numerical_mutate(self,mutation_chance=0.1,width=0.1,relative_width=True):
        if self.random() > mutation_chance: return
        this_as_int = int(self.code, 2)
        if relative_width: width = this_as_int*relative_width
        mutated = max(0,int(self.gauss(this_as_int,width)))
        self.code = ('{0:0%ib}'%self.n_bases).format(mutated)

    def __repr__(self):
        return self.code
