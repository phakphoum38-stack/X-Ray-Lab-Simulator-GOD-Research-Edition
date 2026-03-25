import random

class XRayTube:

    def __init__(self):

        self.kvp = 80
        self.ma = 200

    def warmup(self):

        print("Tube ready")

    def emit_photons(self):

        photons = random.randint(50000,100000)

        return photons
