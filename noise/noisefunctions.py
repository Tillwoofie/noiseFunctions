#!/opt/local/bin/python3.3

# a collections of noise functions

import math

def noise1_1d(x):
    n = (x<<13) ^ x
    return ( 1.0 - ( (n * (n * n * 15731 + 789221) + 1376312589) & 0x7fffffff) / 1073741824.0)


def noise1_2d(x, y):
    #n = x + y * 57
    n = x * 17483 + y * 19979
    n = (n<<13) ^ n
    return ( 1.0 - ( (n * (n * n * 15731 + 789221) + 1376312589) & 0x7fffffff) / 1073741824.0)


def noise2_2d(x, y):
    #makes crazy weird patterns, like a starburst
    n = math.fabs((float(x or 1)/float(y or 1)) * 773)
    n += math.fabs((float(y or 1)/float(x or 1)) * 967)
    n = int(n)
    #n = x * 17483 + y * 19979
    n = (n<<13) ^ n
    return ( 1.0 - ( (n * (n * n * 15731 + 789221) + 1376312589) & 0x7fffffff) / 1073741824.0)


def linear_interpolation(a, b, x):
    return a*(1-x) + b*x


def cosine_interpolation(a, b, x):
    ft = x * math.pi
    f = (1 - math.cos(ft)) * 0.5

    return a*(1-f) + b*f


def smooth_noise_1d(x, noiseFunc):
    nf = noiseFunc
    return nf(x)/2 + nf(x-1)/4 + nf(x+1)/4


def smooth_noise_2d(x, y, noiseFunc):
    nf = noiseFunc
    corners = ( nf(x-1,y-1) + nf(x+1,y-1) + nf(x-1,y+1) + nf(x+1,y+1) ) / 16.0
    sides = ( nf(x-1,y) + nf(x+1,y) + nf(x,y-1) + nf(x,y+1) ) / 8.0
    center = nf(x,y)
    return corners + sides + center


def interpolated_noise_1d(x, noiseFunc, interpFunc):
    nf = noiseFunc

    # this shouldn't be a static value, but i don't know a decent way
    # to generate something from one input variable.
    x_fac = math.pi - 3

    v1 = smooth_noise_1d(x, nf)
    v2 = smooth_noise_1d(x+1, nf)

    return interpFunc(v1, v2, x_fac)


def interpolated_noise_2d(x, y, noiseFunc, interpFunc):
    nf = noiseFunc
    inf = interpFunc

    # need 2 repeatable (non-random) factors to interp by...
    # going to try this, but don't know how good it will work...
    x_fac = ( float(x or 1) / float(y or 1) ) % 1
    y_fac = ( float(y or 1) / float(x or 1) ) % 1

    v1 = smooth_noise_2d(x, y, nf)
    v2 = smooth_noise_2d(x+1, y, nf)
    v3 = smooth_noise_2d(x, y+1, nf)
    v4 = smooth_noise_2d(x+1, y+1, nf)

    i1 = inf(v1, v2, 0)
    i2 = inf(v3, v4, 0)

    return inf(i1, i2, 0)


def perlin_noise_1d(x, persistence, octaves, noiseFunc, interpFunc):
    total = 0
    for i in range(0, octaves):
        freq = pow(2, i)
        ampl = pow(persistence, i)

        total += interpolated_noise_1d(x * freq, noiseFunc, interpFunc) * ampl
    return total


def perlin_noise_2d(x, y, persistence, octaves, noiseFunc, interpFunc):
    total = 0
    for i in range(0, octaves):
        freq = pow(2, i)
        ampl = pow(persistence, i)

        total += interpolated_noise_2d(x * freq, y * freq, noiseFunc, interpFunc) * ampl
    return total


if __name__ == '__main__':
    print(noise1_2d(5,7))
    q = [ perlin_noise_1d(x, 2, 2, noise1_1d, linear_interpolation) for x in range(30) ]
    print(q)
    n = [[ perlin_noise_2d(x,y,2,2, noise1_2d, linear_interpolation) for y in range(1,6)] for x in range(1,6) ] 
    print(n)
