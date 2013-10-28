#!/opt/local/bin/python3.3

from basemap import basemap

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


if __name__ == '__main__':
    self_test()
