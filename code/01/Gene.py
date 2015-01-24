class Gene():
    from random import random

    def __init__(self, n_base=4, verbose=False):
        self.verbose = verbose
        self.n_base = n_base
        self.generate_gene()

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

    def __repr__(self):
        return self.code
