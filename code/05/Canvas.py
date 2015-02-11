class Canvas():
    from PIL import Image, ImageDraw, ImageColor
    from Line import Line
    from math import fabs
    import numpy as np

    def __init__(self, width, height, image=False, fill="white", verbose=False):
        self.verbose = verbose
        self.width   = width
        self.height  = height
        self.fill    = fill
        self.image   = image
        self.background = self.ImageColor.getcolor(self.fill,"RGB")
        self.clear()


    def clear(self):
        if self.image:
            self.img = self.Image.open(self.image)
            self.width
        else:
            self.img     = self.Image.new( 'RGB', (self.width,self.height), self.fill) # create a new black image
        self.pixels  = self.img.load()
        self.draw    = self.ImageDraw.Draw(self.img)
        self.bands   = self.img.getbands()

    def add_line(self,line):
        self.draw.line((line.x1,line.y1, line.x2,line.y2), fill=line.colour, width=line.width)

    def add_circle(self,circle):
        x1 = circle.x - circle.r
        y1 = circle.y - circle.r
        x2 = circle.x + circle.r
        y2 = circle.y + circle.r
        self.draw.ellipse((x1,y1, x2,y2), fill=circle.colour)

    def save(self, file_name):
        if self.verbose: print "cnvs : Saving canvas as: %s"%file_name
        self.img.save(file_name)

    def compare(self, canvas):
        if self.verbose: print "cnvs : Comparing canvases"
        if self.img.size != canvas.img.size:
            print "cnvs : Cannot compare canvases of different size"
            print "cnvs :  this:  ",self.img.size
            print "cnvs :  other: ",canvas.img.size
            assert False
        score = 0
        # for i,j in self.filled_pixels:    # for every filled pixel:
        for i in range(self.img.size[0]):
            for j in range(self.img.size[1]):
                this_pixel =   self.pixels[i,j]
                that_pixel = canvas.pixels[i,j]
                # compare in colour space
                diff = self.fabs(this_pixel[0]-that_pixel[0]) + \
                       self.fabs(this_pixel[1]-that_pixel[1]) + \
                       self.fabs(this_pixel[2]-that_pixel[2])
                if diff == 0: score += 2
                else:         score += 1. / diff

        return score

    def numpy_compare(self, canvas):
        if self.verbose: print "cnvs : Comparing canvases numpy style"
        score = 0
        for band_index, band in enumerate(self.bands):
            m1 = self.np.array([p[band_index] for p in   self.img.getdata()]).reshape(*  self.img.size)
            m2 = self.np.array([p[band_index] for p in canvas.img.getdata()]).reshape(*canvas.img.size)
            diff = self.np.sum(self.np.abs(m1-m2))
            if diff == 0: score += 2
            else:         score += 1. / diff
        return score

    def find_filled_pixels(self):
        self.filled_pixels = []
        for i in range(self.img.size[0]):
            for j in range(self.img.size[1]):
                if self.pixels[i,j] == self.background: continue
                self.filled_pixels.append((i,j))

    def __repr__(self):
        return "Canvas: [%i x %i]"%(self.width,self.height)
