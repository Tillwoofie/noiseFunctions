#!/opt/local/bin/python3.3

import site
site.addsitedir("/Users/jhickson/nonwork/noiseFunctions/")
from basemap import basemap
from PIL import Image

class map2d(basemap):
    def __init__(self, x_size, y_size, scaling_factor):
        #x verification
        self.scale = scaling_factor
        if x_size > 0:
            self.x_size = x_size
        elif x_size < 0:
            self.x_size = abs(x_size)
        else:
            #aka, x_size = 0
            raise ValueError("This should be more than 0")

        #y verifiction
        if y_size > 0:
            self.y_size = y_size
        elif y_size < 0:
            self.y_size = abs(y_size)
        else:
            #aka, y_size = 0
            raise ValueError("This should be more than 0")

        #initialize the data structure
        self.data = [[ 0 for x in range(self.x_size) ] for y in range(self.y_size) ]
    
    
    def get_size(self):
        return (self.x_size, self.y_size)


    def set_block(self, x, y, data):
        if (x >= 0 and x < self.x_size) and (y >= 0 and y < self.y_size):
            self.data[x][y] = data
        else:
            raise IndexError("Provided coordinates are out of range")


    def get_block(self, x, y):
        return self.data[x][y]


    def get_gen_iter(self):
        for x in range(self.x_size):
            for y in range(self.y_size):
                yield (x,y)


    def verify_coords(self, x, y):
        if (x >= 0 and x < self.x_size) and (y >= 0 and y < self.y_size):
            return True
        else:
            return False


    def gen_noise(self, persistence, octaves, noiseType, noiseFunction, interpFunction):
        self.data = [[ noiseType(float(x)/float(self.scale), float(y)/float(self.scale), \
            persistence, octaves, noiseFunction, interpFunction) \
            for x in range(self.x_size)] for y in range(self.y_size)]

        
    def _test_gen_noise_func(self, noiseType):
        self.data = [[ noiseType(x,y) for x in range(self.x_size)] for y in range(self.y_size)]


    def to_image(self, colour):
        #floating point values between 0-256
        if colour:
            img = Image.new("RGB", (self.x_size, self.y_size), (256, 256, 256) )
        else:
            img = Image.new("F", (self.x_size, self.y_size), 256.0 )
        
        for x, y, data in self._stream_conv_data():
            if colour:
                img.putpixel((x,y), cosine_colourize(data))
            else:
                img.putpixel((x,y), data):
        #img.putdata(self._stream_conv_data())
        return img
    
    
    def _convert_range(self, val):
        #convert values from noise range (-1.0 - 1.0) to (0.0 - 256.0)
        return (val + 1.0) * 128.0
    
    
    def _stream_conv_data(self):
        for x in range(self.x_size):
            for y in range(self.y_size):
                yield (x, y, self._convert_range(self.data[x][y]))


def cosine_colourize(x):
    import math
    samp = x/256.0
    R = math.cos(samp*(math.pi))
    if R < 0:
        R = 0
    G = math.cos(samp*(math.pi)+60)
    if G < 0:
        G = 0
    B = math.cos(samp*(math.pi)+180)
    if B < 0:
        B = 0
    return (int(R*256), int(G*256), int(B*256))
    
    
def coord_order_test():
    x_size = 5
    y_size = 3
    test_map = map2d(x_size,y_size, 1)

    size = test_map.get_size()
    if size[0] == x_size and size[1] == y_size:
        return True
    else:
        return False


def self_test():
    if coord_order_test():
        print("yay all good")


def test_cos_col():
    for x in range(0,257):
        print("X:{} Colour:{}".format(x, cosine_colourize(x)))


def image_test(colour):
    import noise.noisefunctions as nf
    import math
    q = map2d(100,100, 1)
    q.gen_noise(1.0/math.sqrt(2), 5, nf.perlin_noise_2d, nf.noise1_2d, nf.cosine_interpolation)
    #q._test_gen_noise_func(nf.noise1_2d)

    img = q.to_image(False)
    img.show()


if __name__ == '__main__':
    self_test()
    #test_cos_col()
    image_test()
