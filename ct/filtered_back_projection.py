import numpy as np

def reconstruct(sinogram):

    angles,detectors = sinogram.shape

    img = np.zeros((detectors,detectors))

    for i in range(angles):

        img += np.tile(
            sinogram[i],
            (detectors,1)
        )

    img = img / angles

    return img
