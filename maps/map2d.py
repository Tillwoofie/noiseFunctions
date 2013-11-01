#!/opt/local/bin/python3.3

import site
site.addsitedir("/Users/jhickson/nonwork/noiseFunctions/")
from basemap import basemap
from PIL import Image

class map2d(basemap):
    def __init__(self, x_size, y_size):
        #x verification
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
        self.data = [[ noiseType(x, y, persistence, octaves, noiseFunction, interpFunction) \
            for x in range(self.x_size)] for y in range(self.y_size)]

        
    def to_image(self):
        #floating point values between 0-256
        img = Image.new("F", (self.x_size, self.y_size), 256.0 )
        
        img.putdata(self._stream_conv_data())
        return img
    
    
    def _convert_range(val):
        #convert values from noise range (-1.0 - 1.0) to (0.0 - 256.0)
        return (val + 1.0) * 128.0
    
    
    def _stream_conv_data(self):
        for x in range(self.x_size):
            for y in range(self.y_size):
                yield _convert_range(self.data[x][y])


def coord_order_test():
    x_size = 5
    y_size = 3
    test_map = map2d(x_size,y_size)

    size = test_map.get_size()
    if size[0] == x_size and size[1] == y_size:
        return True
    else:
        return False


def self_test():
    if coord_order_test():
        print("yay all good")


def image_test():
    import noise.noisefunctions as nf
    q = map2d(100,100)
    q.gen_noise(2, 2, nf.perlin_noise_2d, nf.noise1_2d, nf.linear_interpolation)

    img = q.to_image()
    img.show()


if __name__ == '__main__':
    self_test()
    image_test()
