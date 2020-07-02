from PIL import Image, ImageDraw
import random as rd
import glob

class Shape:
    def __init__(self, size, seed=None):
        self.seed = seed
        if self.seed != None : rd.seed(seed)
        self.r = [(rd.random()-.5)*2 for _ in range(8)] #alea [-1,1]
        self.im = Image.new("RGBA", (size,size), "#0000")
        self.draw = ImageDraw.Draw(self.im)
        self.x, self.y = self.im.size


        self.posEyes = [ (self.x*(7/24 + self.r[0]/40), self.y*(10/24 + self.r[1]/60)),
                         (self.x*(17/24 - self.r[0]/40), self.y*(10/24 + self.r[1]/60)) ]
        self.shapeEyes = ((.17+self.r[2]/50)*self.x, (.17+self.r[3]/50)*self.y, (.17+min(self.r[2],self.r[3])/50)*self.x)
        self.posMouth = (self.x/2, self.y*(1/2 + self.r[4]/20))
        self.posNose = (self.x/2, self.y*(19/48 + self.r[5]/50))
        self.posCheeks = ( (self.x*(1/3 - self.r[6]/30), self.y*(1/2 + self.r[4]/20)), (self.x*(2/3 + self.r[6]/30), self.y*(1/2 + self.r[4]/20)) )
        self.posHat = (self.x/2, self.y*(1/3+self.r[7]/20))
        self.shapeBody = [ (self.x*(1/6 + self.r[6]/20), self.y*(1/3+self.r[7]/20), self.x*(5/6 - self.r[6]/20), self.y),
                           (self.x*(1/6 + self.r[6]/20), self.y*4/6 - self.y/10, self.x*(5/6 - self.r[6]/20), self.y*4/6 + self.y/10)]

    def get(self, color, debug=False):

        # body shape generation
        self.draw.ellipse(self.shapeBody[0], fill="#f00" if debug else color)
        self.draw.rectangle((0,(self.shapeBody[1][1]+self.shapeBody[1][3])/2,self.x,self.y), fill="#0000")
        self.draw.ellipse(self.shapeBody[1], fill="#f00" if debug else color)

        # eyes
        for posX,posY in self.posEyes:
            bbox =  (posX - self.shapeEyes[0]/2, posY - self.shapeEyes[1]/2, posX + self.shapeEyes[0]/2, posY + self.shapeEyes[1]/2)
            self.draw.ellipse(bbox, fill="#0f0" if debug else color)

        # cheeks
        radius = self.x *(1/10- rd.random()/20)
        dec = rd.randint(25,40) * (-1 if rd.random()>.5 else 1)
        color_cheek = tuple([max(min(v + dec, 255),0) for v in color])
        for posX,posY in self.posCheeks:
            bbox =  (posX - radius/2, posY - radius/2, posX + radius/2, posY + radius/2)
            self.draw.ellipse(bbox, fill=color_cheek)

        if debug:
            eX, eY = .05*self.x, .05*self.y
            bbox =  (self.posMouth[0] - eX/2, self.posMouth[1] - eY/2, self.posMouth[0] + eX/2, self.posMouth[1] + eY/2)
            self.draw.ellipse(bbox, fill="#00f")
            eX, eY = .05*self.x, .05*self.y
            bbox =  (self.posNose[0] - eX/2, self.posNose[1] - eY/2, self.posNose[0] + eX/2, self.posNose[1] + eY/2)
            self.draw.ellipse(bbox, fill="#00f")

        #outline
        ls = 1.05
        bg = self.im.resize((int(self.im.size[0]*ls), int(self.im.size[1]*ls)))
        black = Image.new("RGBA", bg.size, "black")
        bg = Image.composite(black, bg, bg)

        left = self.im.size[0]*(ls-1)/2
        top = self.im.size[1]*(ls-1)/2
        right = self.im.size[0]-left
        bottom = self.im.size[1]-top

        bg.paste( self.im, (int(left), int(top)), self.im)
        im2 = bg.crop((left, top, right, bottom))

        return im2

class Eye:
    def __init__(self, size, model=None, seed=None):
        self.seed = seed
        if self.seed != None : rd.seed(seed)
        self.model = model
        self.size = int(size)
        self.im = Image.new("RGBA", (self.size,self.size), "#0000")
        self.draw = ImageDraw.Draw(self.im)

        self.models = [">","<","o","O",".","-","x","♥"," "]
        if self.model not in self.models:
            self.model = rd.choice( self.models )

        self.width = self.size//15

        self.bg_color = "#fff"
        self.fg_color = "#333"

    def draw_circle(self):
        self.draw.ellipse((self.size/5,self.size/5,4/5*self.size,4/5*self.size),fill=self.bg_color)

    def draw_right(self):
        self.draw_circle()
        x1, x2 = self.size/3, self.size*2/3
        y1,y2,y3 = self.size/3, self.size/2, self.size*2/3
        self.draw.line( ((x1,y1),(x2,y2),(x1,y3)) ,fill=self.fg_color, width=self.width)

    def draw_line(self):
        self.draw_circle()
        x1, x2 = self.size/3, self.size*2/3
        y1, y2 = self.size/2, self.size/2
        self.draw.line( ((x1,y1),(x2,y2)) ,fill=self.fg_color, width=self.width)

    def draw_cross(self):
        self.draw_circle()
        x1, x2 = self.size/3, self.size*2/3
        y1, y2 = self.size/3, self.size*2/3
        self.draw.line( ((x1,y1),(x2,y2)) ,fill=self.fg_color, width=self.width)
        self.draw.line( ((x1,y2),(x2,y1)) ,fill=self.fg_color, width=self.width)


    def draw_left(self):
        self.draw_circle()
        x1, x2 = self.size*2/3, self.size*1/3
        y1,y2,y3 = self.size/3, self.size/2, self.size*2/3
        self.draw.line( ((x1,y1),(x2,y2),(x1,y3)) ,fill=self.fg_color, width=self.width)


    def draw_small(self):
        self.draw_circle()
        self.draw.ellipse((self.size*2/5,self.size*2/5,3/5*self.size,3/5*self.size),fill=self.fg_color)

    def draw_simple(self):
        self.draw_circle()
        self.draw.ellipse((self.size/3,self.size/3,2/3*self.size,2/3*self.size),fill=self.fg_color)

    def draw_heart(self):
        self.draw_circle()
        l = [ (self.size/3, self.size/2), (self.size/2, self.size*2/3), (self.size*2/3, self.size/2), (self.size/2, self.size/3)]
        self.draw.polygon( l ,fill=self.fg_color)

        centers = [((l[0][0]+l[3][0])/2, (l[0][1]+l[3][1])/2), ((l[2][0]+l[3][0])/2, (l[2][1]+l[3][1])/2)]
        r = self.size/12 * 2**.5
        for c in centers:
            self.draw.ellipse( [c[0]-r, c[1]-r, c[0]+r, c[1]+r] ,fill=self.fg_color)


    def draw_big(self):
        self.draw_circle()
        self.draw.ellipse((self.size*3/12,self.size*3/12,9/12*self.size,9/12*self.size),fill=self.fg_color)

    def get(self):
        if self.model == ">":
            self.draw_right()
        elif self.model == "<":
            self.draw_left()
        elif self.model == "o":
            self.draw_simple()
        elif self.model == "O":
            self.draw_big()
        elif self.model == ".":
            self.draw_small()
        elif self.model == "-":
            self.draw_line()
        elif self.model == "x":
            self.draw_cross()
        elif self.model == "♥":
            self.draw_heart()
        elif self.model == " ":
            self.draw_circle()

        return self.im

class Nose():
    def __init__(self, size, seed=None):
        self.seed = seed
        if self.seed != None : rd.seed(seed)
        self.size = int(size/15)
        self.color = "#000"
        self.im = Image.new("RGBA", (self.size,self.size//2), "#0000")
        self.draw = ImageDraw.Draw(self.im)
        self.width = self.size//15

    def draw_small(self):
        self.draw.line( ((self.size*4/20, self.size*3/20),(self.size*5/20, self.size*5/20)), fill=self.color, width=self.width)
        self.draw.line( ((self.size*16/20, self.size*3/20),(self.size*15/20, self.size*5/20)), fill=self.color, width=self.width)

    def draw_blush(self):
        self.color = "#900"
        self.draw.line( ((self.size*4/20, self.size*3/20),(self.size*5/20, self.size*5/20)), fill=self.color, width=self.width)
        self.draw.line( ((self.size*6/20, self.size*3/20),(self.size*7/20, self.size*5/20)), fill=self.color, width=self.width)
        self.draw.line( ((self.size*2/20, self.size*3/20),(self.size*3/20, self.size*5/20)), fill=self.color, width=self.width)

        self.draw.line( ((self.size*16/20, self.size*3/20),(self.size*15/20, self.size*5/20)), fill=self.color, width=self.width)
        self.draw.line( ((self.size*14/20, self.size*3/20),(self.size*13/20, self.size*5/20)), fill=self.color, width=self.width)
        self.draw.line( ((self.size*18/20, self.size*3/20),(self.size*17/20, self.size*5/20)), fill=self.color, width=self.width)

    def get(self):
        if rd.random() > .5:
            self.draw_blush()
        else:
            self.draw_small()
        return self.im

class Cheek():
    def __init__(self, size, seed=None):
        self.seed = seed
        if self.seed != None : rd.seed(seed)
        self.size = int(size/5)
        self.alpha = rd.randint(20,255)
        self.color = ("#303030" if rd.random()>.5 else "#c0c0c0") + str(hex(self.alpha))[2:]
        self.im = Image.new("RGBA", (self.size,self.size), "#0000")
        self.draw = ImageDraw.Draw(self.im)
        self.radius = self.size * (rd.random()/2)

    def get(self):
        eX, eY = self.radius, self.radius
        bbox =  (self.size/2 - eX/2, self.size/2 - eY/2, self.size/2 + eX/2, self.size/2 + eY/2)
        self.draw.ellipse(bbox, fill=self.color)
        return self.im

class Mouth():
    def __init__(self, size, seed=None):
        self.seed = seed
        if self.seed != None : rd.seed(seed)
        self.size = int(size * (rd.random()/2+1))
        self.f = rd.choice( glob.glob("mouths/*.png") )

    def get(self):
        self.im = Image.open(self.f)
        self.im = self.im.resize( (self.size,self.size) )
        return self.im

class Hat():
    def __init__(self, size, seed=None):
        self.seed = seed
        if self.seed != None : rd.seed(seed)
        self.size = int(size)
        self.f = rd.choice( glob.glob("hats/*.png") )
        self.rotation = rd.random()*10 - 5

    def get(self):
        self.im = Image.open(self.f)
        self.im = self.im.resize( (self.size,self.size) )
        self.im = self.im.rotate( self.rotation, Image.NEAREST, expand = 1 )
        self.im.paste(self.im, (int(-self.rotation/150 * self.size),0))
        return self.im



class Frog():
    def __init__(self, size=1000, eyes=None, goodeyes=True, seed=None):
        self.size = size
        self.shape = Shape(size, seed=seed)
        if eyes == None: eyes=["",""]
        if goodeyes:
            ge = [">>","<<","oo","OO","..","--","xx","♥♥","  ", "><", "-o", "o-","♥-","-♥", "oO", "Oo", ".o", "o." ]
            eyes = rd.choice( ge )
        self.le = Eye(self.shape.shapeEyes[2],model=eyes[0],seed=seed)
        self.re = Eye(self.shape.shapeEyes[2],model=eyes[1],seed=seed)
        self.nose = Nose(size, seed=seed)
        self.mouth = Mouth(size, seed=seed)
        self.hat = Hat(size, seed=seed)
        self.color = tuple([rd.randint(0,254) for _ in range(3)])

    def get(self, returnsize):
        im = self.shape.get(self.color, False)

        leim = self.le.get()
        reim = self.re.get()
        noseim = self.nose.get()
        mouthim = self.mouth.get()
        hatim = self.hat.get()

        lePos = tuple(map(lambda x: int(x-self.shape.shapeEyes[2]/2),self.shape.posEyes[0]))
        rePos = tuple(map(lambda x: int(x-self.shape.shapeEyes[2]/2),self.shape.posEyes[1]))

        nPos = ( int(self.shape.posNose[0]-noseim.size[0]/2), int(self.shape.posNose[1]-noseim.size[1]/2) )
        mPos = ( int(self.shape.posMouth[0]-mouthim.size[0]/2), int(self.shape.posMouth[1]-mouthim.size[1]/2) )
        hPos = ( int(self.shape.posHat[0]-hatim.size[0]/2), int(self.shape.posHat[1]-hatim.size[1]/2) )

        im.paste(leim,    lePos,  leim)
        im.paste(reim,    rePos,  reim)
        im.paste(noseim,  nPos,   noseim)
        im.paste(mouthim, mPos,   mouthim)
        im.paste(hatim,   hPos,   hatim)

        return im.resize((returnsize,returnsize))


