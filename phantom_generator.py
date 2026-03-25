import numpy as np

def create_circle_phantom(size=512):

    img = np.zeros((size,size))

    cx = size//2
    cy = size//2

    for x in range(size):
        for y in range(size):

            r = ((x-cx)**2 + (y-cy)**2)**0.5

            if r < size/3:
                img[y,x] = 1

    return img
