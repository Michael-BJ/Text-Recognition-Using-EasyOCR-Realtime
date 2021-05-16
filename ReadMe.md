# How it's works
1. Import the library that we need
````
import cv2
import numpy as np
from matplotlib import pyplot as plt
import easyocr
````
First install the pytoch library before installing the easyocr library. The pytorch library can be downloaded from here (https://pytorch.org/).
2. Add the image you want to use for identification
````
img_path = "stop.jpg"
````
3.Load the model into memory
````
reader = easyocr.Reader(['en'], gpu = False)
````
4. Make a program that can read and identify images, also print the result
````
result = reader.readtext(img_path)
print (result)
````
# Demo

Clik the picture to see the Video
[![Watch the video](https://img.youtube.com/vi/QOrSCVVKoaM&t/maxresdefault.jpg)](https://youtu.be/QOrSCVVKoaM&t)
