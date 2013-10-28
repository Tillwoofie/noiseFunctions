#!/opt/local/bin/python3.3

import math

class 2dmap(basemap):
    def __init__(self, x_size, y_size):
        #x verification
        if x_size > 0:
            self.x_size = x_size
        else if x_size < 0:
            self.x_size = math.abs(x_size)
        else:
            #aka, x_size = 0
            raise ValueError("This should be more than 0")

        #y verifiction
        if y_size > 0:
            self.y_size = y_size
        else if y_size < 0:
            self.y_size = math.abs(y_size)
        else:
            #aka, y_size = 0
            raise ValueError("This should be more than 0")

        #initialize the data structure
        self.data = [[ 0 for x in range(self.xsize) ] for y in range(self.y_range) ]
    
    
    def get_size(self):
        return (x_size, y_size)


    def set_block(self, x, y, data):
        if (x >= 0 and x < x_size) and (y >= 0 and y < y_size):
            self.data[x][y] = data
        else
            raise IndexError("Provided coordinates are out of range")


    def get_block(self, x, y):
        return self.data[x][y]


    def get_gen_iter(self):
        for x in range(self.x_size):
            for y in range(self.y_size):
                yield (x,y)


def coord_order_test():
    x_size = 5
    y_size = 3
    2d_test = 2dmap(x_size,y_size)

    size = 2d_test.get_size()
    if size[0] = x_size and size[1] = y_size:
        return True
    else
        return False


def self_test():
    if coord_order_test():
        print("yay all good")


if __name__ = '__main__':
    self_test()
