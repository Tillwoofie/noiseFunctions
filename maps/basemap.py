#!/opt/local/bin/python3.3

class basemap(object):
    
    def __init__(self):
        raise NotImplementedError("This should init the class with the correct skeleton data structures.")

    def get_size(self):
        raise NotImplementedError("This should return a tuple of the size of the internal size of the structure.")

    def set_block(self):
        raise NotImplementedError("This should take coords and a value to set")

    def get_block(self):
        raise NotImplementedError("This should return the block at the coords")

    def get_region(self):
        raise NotImplementedError("This should return a region bounded by min/max coords")

    def get_gen_iter(self):
        raise NotImplementedError("This should return a generator function to iterate over all cells")

    def verify_coords(self):
        raise NotImplementedError("This should verify the coords given are inside the object's range")

    def gen_noise(self,  persistence, octaves, noiseFunction, interpFunction):
        raise NotImplementedError("This triggers noise to be generated and stored in the object.")

    def to_image(self):
        raise NotImplementedError("This should return a pillow image object")
