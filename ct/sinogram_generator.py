import numpy as np

def generate_sinogram(image,angles=180):

    size = image.shape[0]

    sinogram = np.zeros((angles,size))

    for a in range(angles):

        projection = np.sum(image,axis=0)

        sinogram[a] = projection

    return sinogram
