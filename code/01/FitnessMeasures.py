class NumericalFitnessMeasure():

    def __init__(self,target_value):
        self.target_value = target_value

    def eval(self,value):
        if value == self.target_value:
            return 1000.
        return (1. / abs(value - self.target_value))

    def __repr__(self):
        return "nfit : --- Numerical fitness measure, target value: %.1f"%self.target_value