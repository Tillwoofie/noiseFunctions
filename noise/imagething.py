#!/opt/local/bin.python3.3

from PIL import Image
import noisefunctions as noise

datas = [[ noise.perlin_noise_2d (x,y,2,2,noise.noise1_2d,noise.linear_interpolation) for y in range(100)] for x in range(100)]

img = Image.fromarray(datas)
img.show()
