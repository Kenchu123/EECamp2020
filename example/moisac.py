import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('flower.bmp')     # open image
# img would be a numpy array

h,w,c = img.shape # (height,width,color)


result = img.copy() # new array for moisac

for i in range(0,h,10):
    for j in range(0,w,10):
        result[i:i+10,j:j+10] = img[i+5,j+5]

plt.imshow(result)
plt.axis('off')
plt.show()

