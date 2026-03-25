import numpy as np

class DetectorPanel:

    def __init__(self):

        self.width = 512
        self.height = 512

    def capture(self,photons):

        img = np.random.poisson(
            photons,
            (self.height,self.width)
        )

        return img
