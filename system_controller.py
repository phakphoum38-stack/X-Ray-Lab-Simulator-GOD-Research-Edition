from hardware.xray_tube import XRayTube
from hardware.detector_panel import DetectorPanel
from imaging.exposure_engine import ExposureEngine

class XRaySystem:

    def __init__(self):

        self.tube = XRayTube()
        self.detector = DetectorPanel()
        self.engine = ExposureEngine(self.tube,self.detector)

    def warmup(self):

        print("Warming X-ray tube...")
        self.tube.warmup()

    def scan(self):

        print("Starting scan")
        image = self.engine.capture()

        return image
