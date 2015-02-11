class Canvas():
    from PIL import Image, ImageDraw, ImageColor
    from Line import Line

    def __init__(self, width, height, fill="white", verbose=False):
        self.verbose = verbose
        self.width   = width
        self.height  = height
        self.fill    = fill
        self.background = self.ImageColor.getcolor(self.fill,"RGB")
        self.clear()

    def clear(self):
        self.img     = self.Image.new( 'RGB', (self.width,self.height), self.fill) # create a new black image
        self.pixels  = self.img.load()
        self.draw    = self.ImageDraw.Draw(self.img)

    def add_line(self,line):
        self.draw.line((line.x1,line.y1, line.x2,line.y2), fill=line.colour, width=line.width)

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
                # if (this_pixel == self.background) and (that_pixel == self.background): continue
                if this_pixel == that_pixel:
                    if this_pixel == self.background: score += 0.1
                    else:                             score += 1
                # else:
                    # score-=0.1

        return score

    def find_filled_pixels(self):
        self.filled_pixels = []
        for i in range(self.img.size[0]):
            for j in range(self.img.size[1]):
                if self.pixels[i,j] == self.background: continue
                self.filled_pixels.append((i,j))

    def __repr__(self):
        return "Canvas: [%i x %i]"%(self.width,self.height)
