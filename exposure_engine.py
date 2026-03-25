class ExposureEngine:

    def __init__(self,tube,detector):

        self.tube = tube
        self.detector = detector

    def capture(self):

        photons = self.tube.emit_photons()

        image = self.detector.capture(photons)

        return image
