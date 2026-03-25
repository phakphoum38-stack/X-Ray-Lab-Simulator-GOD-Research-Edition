import os
import numpy as np

class ImageStore:

    def save(self,image,name):

        os.makedirs("images",exist_ok=True)

        np.save("images/"+name,image)
