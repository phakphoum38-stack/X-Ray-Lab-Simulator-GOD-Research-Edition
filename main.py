from core.system_controller import XRaySystem

system = XRaySystem()

system.warmup()

image = system.scan()

print("Image generated")
print(image.shape)
