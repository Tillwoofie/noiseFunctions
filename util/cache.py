#!/usr/bin/env python3.3

# a cachable wrapper that implements a cache for called args.

import time

class Cachable(object):
    def __init__(self, size=100):
        self.size = size
        self.cache = {}

    def __call__(self, f):
        # only called once as part of the decoration process.
        def wrapped_f(*args):
            #check if args in cache
            if self.in_cache(args):
                return self.get_cache(args)
            else: #if not, run function
                x = f(*args)
                self.add_cache(args,x)
                return x
        return wrapped_f

    def in_cache(self, key):
        if key in self.cache:
            return True
        else:
            return False

    def add_cache(self, key, val):
        if len(self.cache) > self.size:
            #need to trim old objects
            self.evict_key()
        self.cache[key] = [1, val]

    def evict_key(self):
        # evicts the oldest (least used) key
        oldest_key = None
        min_use = None
        for x in self.cache.keys():
            if min_use == None:
                min_use = self.cache[x][0]
                oldest_key = x
                continue
            if self.cache[x][0] < min_use:
                min_use = self.cache[x][0]
                oldest_key = x
        del self.cache[oldest_key]

    def get_cache(self, key):
        self.cache[key][0] += 1
        return self.cache[key][1]

def timeme(f):
    #simple decorator that times execution of wrapped function.
    def wrapped_f(*args):
        one = time.time()
        x = f(*args)
        elapsed = time.time() - one
        print("Function run time: {}".format(elapsed))
        return x
    return wrapped_f
