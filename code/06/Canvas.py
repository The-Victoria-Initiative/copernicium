class Canvas():
    from PIL import Image, ImageDraw, ImageColor
    from Pixel import Pixel
    from math import fabs, sqrt
    import numpy as np
    import json

    def __init__(self, width, height, n_pixels=False, image=False, fill="white", verbose=False):
        self.verbose = verbose
        self.width   = width
        self.height  = height
        self.fill    = fill
        self.image   = image
        self.background = self.ImageColor.getcolor(self.fill,"RGB")
        self.clear()
        # counters for custom pixels
        self.custom_pixels = False
        if n_pixels:
            self.x_pix = int(self.sqrt(n_pixels))
            self.y_pix = int(self.sqrt(n_pixels))
            self.d_x   = self.width / self.x_pix
            self.d_y   = self.width / self.y_pix
            self.current_x = 0
            self.current_y = 0
            self.custom_pixels = []
            for i in range(self.x_pix):
                for j in range(self.y_pix):
                    if j == 0: self.custom_pixels.append([])
                    self.custom_pixels[i].append(False)
                    self.custom_pixels[i][j] = (0,0,0)

            if self.verbose:
                print "cnvs: n pixels: %i"%n_pixels
                print "cnvs:     x_pix: %i, dx: %i"%(self.x_pix,self.d_x)
                print "cnvs:     y_pix: %i, dy: %i"%(self.y_pix,self.d_y)

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

    def add_pixel(self,pixel):
        # print "adding pixel %i, %i"%(self.current_x,self.current_y)
        x1 = self.current_x * self.d_x
        y1 = self.current_y * self.d_y
        x2 = x1 + self.d_x
        y2 = y1 + self.d_y
        self.draw.rectangle((x1,y1, x2,y2), fill=pixel.colour)
        # increment counters
        if self.current_x < (self.x_pix-1):
            self.current_x += 1
        else:
            self.current_x = 0
            self.current_y += 1
        assert(self.current_y <= self.y_pix), "Pixel limit exceeded, current y: %i, y_pix: %i"%(self.current_y, self.y_pix)

    def add_pixel_summary(self,pixel):
        self.custom_pixels[self.current_x][self.current_y] = pixel.colour
        # increment counters
        if self.current_x < (self.x_pix-1):
            self.current_x += 1
        else:
            self.current_x = 0
            self.current_y += 1
        assert(self.current_y <= self.y_pix), "Pixel limit exceeded, current y: %i, y_pix: %i"%(self.current_y, self.y_pix)

    def save(self, file_name,flip=False):
        if self.verbose: print "cnvs : Saving canvas as: %s"%file_name
        if flip: self.img = self.img.rotate(90).transpose(self.Image.FLIP_TOP_BOTTOM)
        self.img.save(file_name)

    def save_summary(self, file_name):
        if self.verbose: print "cnvs : Saving canvas summary as: %s"%file_name
        self.current_x = 0
        self.current_y = 0
        blank_canvas = Canvas(self.width,self.height,n_pixels=self.n_pixels)
        for i in range(self.x_pix):
            for j in range(self.y_pix):
                this_pixel =   self.custom_pixels[i][j]
                blank_canvas.add_pixel(self.Pixel(this_pixel))
        blank_canvas.save(file_name)

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

    def compare_summary(self, canvas):
        if self.verbose: print "cnvs : Comparing summary canvases"
        if self.custom_pixels == False:
           print "cnvs : Cannot compare as this canvas that doesn't have a summary"
           assert False
        
        if canvas.custom_pixels == False:
            print "cnvs : Cannot compare to a canvas that doesn't have a summary"
            assert False

        if len(self.custom_pixels) != len(canvas.custom_pixels):
            print "cnvs : Cannot compare canvases of different size"
            print "cnvs :  this:  ",self.custom_pixels
            print "cnvs :  other: ",self.custom_pixels
            assert False
        score = 0
        # for i,j in self.filled_pixels:    # for every filled pixel:
        for i in range(self.x_pix):
            for j in range(self.y_pix):
                this_pixel =   self.custom_pixels[i][j]
                that_pixel = canvas.custom_pixels[i][j]
                # compare in colour space
                diff = self.fabs(this_pixel[0]-that_pixel[0]) + \
                       self.fabs(this_pixel[1]-that_pixel[1]) + \
                       self.fabs(this_pixel[2]-that_pixel[2])
                if diff == 0: score += 2
                else:         score += 1. / diff
        return score

    def prepare_summary(self, n_pixels):
        if self.verbose: print "cnvs : Preparing summary canvas"
        self.n_pixels = n_pixels
        self.x_pix = int(self.sqrt(n_pixels))
        self.y_pix = int(self.sqrt(n_pixels))
        self.d_x   = self.width / self.x_pix
        self.d_y   = self.width / self.y_pix
        if self.verbose:
            print "cnvs: n pixels: %i"%n_pixels
            print "cnvs:     x_pix: %i, dx: %i"%(self.x_pix,self.d_x)
            print "cnvs:     y_pix: %i, dy: %i"%(self.y_pix,self.d_y)
        self.custom_pixels = []
        for i in range(self.x_pix):
            for j in range(self.y_pix):
                if j == 0: self.custom_pixels.append([])
                self.custom_pixels[i].append(False)
                
                current_sum = [0,0,0]
                number_of_pixels = 0
                x1 = i * self.d_x
                y1 = j * self.d_y
                x2 = x1 + self.d_x
                y2 = y1 + self.d_y
                for k in range(x1,x2):
                    for l in range(y1,y2):
                        this_pixel =   self.pixels[l,k]
                        current_sum[0] += this_pixel[0]
                        current_sum[1] += this_pixel[1]
                        current_sum[2] += this_pixel[2]
                        number_of_pixels += 1
                current_sum[0] = int(current_sum[0]/number_of_pixels)
                current_sum[1] = int(current_sum[1]/number_of_pixels)
                current_sum[2] = int(current_sum[2]/number_of_pixels)
                self.custom_pixels[i][j] = (current_sum[0],current_sum[1],current_sum[2])
                if self.verbose: print "cnvs :  [%i,%i]: %s"%(i,j,self.custom_pixels[i][j])

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

    def pixels_to_json(self,file_name):
        p_dict = {}
        p_dict["pixels"] = []
        for i in range(self.x_pix):
            for j in range(self.y_pix):
                this_pixel =   self.custom_pixels[j][i]
                p_dict["pixels"].append({"x":i*self.d_x,
                                         "y":j*self.d_y,
                                         "width":self.d_x,
                                         "height":self.d_y,
                                         "r":this_pixel[0],
                                         "g":this_pixel[1],
                                         "b":this_pixel[2],
                                         })
        output_file = open(file_name,"w")
        output_file.write(self.json.dumps(p_dict)+"\n")
        output_file.close()