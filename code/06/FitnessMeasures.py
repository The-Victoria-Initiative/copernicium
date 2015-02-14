class CanvasFitnessMeasure():

    def __init__(self,canvas,verbose=False):
        self.canvas = canvas
        self.canvas.find_filled_pixels()
        self.verbose = verbose

    def eval(self,canvas):
        return self.canvas.compare(canvas)
        # return self.canvas.numpy_compare(canvas)
               
    def __repr__(self):
        return "fit  : --- Canvas fitness measure"