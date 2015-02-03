class Gene():
    from random import random, gauss

    def __init__(self, n_base=9, code=False, verbose=True):
        self.verbose = verbose
        self.n_base = n_base
        if not code:
            self.generate_gene()
        else:
            self.code = code

    def generate_gene(self):
        """
        A gene is a sequence of 4 binary bits which represent
        a number 0 - 9 or a simple mathematical operator: + ,
        -, /, *.
        """
        code = ""
        for i in range(self.n_base):
            if self.random() < 0.5: code = code + "0"
            else:                   code = code + "1"
        self.code = code

    def mutate(self,mutation_chance=0.1):
        for i in range(self.n_base):
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
        self.code = ('{0:0%ib}'%self.n_base).format(mutated)

    def __repr__(self):
        return self.code
