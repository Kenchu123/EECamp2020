import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('flower.jpg') 
# img would be a numpy array

h,w,c = img.shape # (height,width,color)


#----------------------convert to gray scale----------------------------
print('RBG to gray scale...')
gray = np.ones(img.shape) # new array for gray scale
for i in range(h):
    for j in range(w):
        #TODO
        gray[i,j]=np.array([Y,Y,Y])
#-----------------------------------------------------------------------
plt.imshow(gray)
plt.axis('off')
plt.show()
plt.savefig('gray.jpg')

#-----------------------prewiit edge detector---------------------------
print('start to prewiit...')
result = np.ones(img.shape)*255 # new array for prewiit 
for i in range(1,h-1):
    for j in range(1,w-1):
        #TODO
        result[i,j]=np.array([G,G,G])
#------------------------------------------------------------------------

#--------------------- show the image------------------------------------
plt.imshow(result)
plt.axis('off')
plt.show()

plt.savefig('result.jpg') # save the image