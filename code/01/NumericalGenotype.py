from Genotype import Genotype
import copy

gene_values = {}
gene_values["0000"] = "0"
gene_values["0001"] = "1"
gene_values["0010"] = "2"
gene_values["0011"] = "3"
gene_values["0100"] = "4"
gene_values["0101"] = "5"
gene_values["0110"] = "6"
gene_values["0111"] = "7"
gene_values["1000"] = "8"
gene_values["1001"] = "9"
gene_values["1010"] = "+"
gene_values["1011"] = "-"
gene_values["1100"] = "*"
gene_values["1101"] = "/"

class NumericalGenotype(Genotype):

    def __init__(self,genes=False,name="0.0"):
        Genotype.__init__(self,genes=genes,name=name)

    def eval(self,return_string=False):
        """
        evaluate our genotype as a numerical series

        This is done by stepping through the genes looking
        for a number, then an operator, then a number,
        then an operator etc, ignoring out of sequence genes
        and non-coding types.

        Finally the expression is evaluated and the result returned
        """
        self.value = None
        need_a_number = True
        current_operator = None
        as_string = ""
        for i,gene in enumerate(self.genes):
            string_value = self.decode_gene(gene)
            if self.verbose: print "ngeno: gene[%i]: %s"%(i,string_value)
            if need_a_number:
                if not self.is_a_number(string_value): continue
                need_a_number = False

                if self.value == None:
                    self.value = float(string_value)
                    as_string = "%1s"%string_value
                    if self.verbose: print "ngeno:     inital value: %.0f"%self.value
                else:
                    assert current_operator != None, "Tried to operate without an operator"
                    self.update_value(current_operator, int(string_value))
                    as_string += " %1s %1s"%(current_operator,string_value)
                    if self.verbose: print "ngeno:     %s %s = %.2f"%(current_operator, string_value, self.value)
                    current_operator = None
            else:
                if not self.is_an_operator(string_value): continue
                need_a_number = True
                current_operator = string_value
                if self.verbose: print "ngeno:     operator: %s"%current_operator
        if return_string:
            return as_string +" = %f"%self.value
        return self.value

    def decode_gene(self,gene):
        if gene.code in gene_values.keys():
            return gene_values[gene.code]
        else:
            return "None"

    def is_a_number(self,string_value):
        if string_value in ["0","1","2","3","4","5","6","7","8","9"]:
            return True
        return False

    def is_an_operator(self,string_value):
        if string_value in ["+","-","*","/"]:
            return True
        return False

    def update_value(self, operator, value):
        if   operator == "+": self.value = self.value + value
        elif operator == "-": self.value = self.value - value
        elif operator == "*": self.value = self.value * value
        elif operator == "/":
            if self.value != 0 and value != 0:
                self.value = self.value / value
        else:
            assert False, "Invalid operator: %s"%operator

    def breed(self,mate):
        genes = []
        assert len(self.genes) == len(mate.genes), "Mismatched number of genes, self: %i, mate: %i"%(len(self.genes),len(mate.genes))
        for i in range(len(self.genes)):
            if (self.random() < 0.5): genes.append(copy.copy(self.genes[i]))
            else:                     genes.append(copy.copy(mate.genes[i]))
        offspring = NumericalGenotype(genes=genes)
        offspring.mutate()
        return offspring

    def to_string(self):
        to_return = ""
        for i,gene in enumerate(self.genes):
            if gene.code in gene_values.keys():
                to_return += "%4s "%gene_values[gene.code]
            else:
                to_return += " n/a "
        return to_return[:-1]
