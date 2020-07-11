import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from scipy import special
# import scipy.signal
import numpy as np
from PIL import Image
import cmath


# omega = cutoff frequency in radians (pi is max), N = horizontal size of the kernel, also its vertical size, must be odd.
def circularLowpassKernel(omega_c, N):
    kernel = np.fromfunction(lambda x, y: omega_c*special.j1(omega_c*np.sqrt((x - (N - 1)/2)**2 + (
        y - (N - 1)/2)**2))/(2*np.pi*np.sqrt((x - (N - 1)/2)**2 + (y - (N - 1)/2)**2)), [N, N])
    kernel[(N - 1)//2, (N - 1)//2] = omega_c**2/(4*np.pi)
    return kernel


tmp = Image.open("moisac.jpeg")
h,w = tmp.size                   # (height,width,color)
tmp2 = tmp.resize((w, w), resample=Image.BILINEAR)
tmp2.show()
input_img = np.asarray(tmp2)
h, w, c = input_img.shape

# Horizontal size of the kernel, also its vertical size. Must be odd.
kernelN = w
omega_c = np.pi / 4  # Cutoff frequency in radians <= pi
kernel = circularLowpassKernel(omega_c, kernelN)
kernel_fft = np.fft.fft2(kernel)
# plt.imshow(kernel, vmin=-1, vmax=1, cmap='bwr')
# plt.colorbar()
# plt.show()

# DTFT of kernel
'''
kernel_dtft = np.empty((w, w))
for row in range(w):
    for col in range(w):
        num1 = 0J
        for i in range(w):
            num2 = 0J
            for j in range(w):
                num2 += kernel[i, j]*cmath.exp(-cmath.pi*2J*(row*j + col*i))
            num1 += num2
        kernel_dtft[row, col] = num1
'''       

result = np.empty((w, w, c))

for i in range(c):
    result[:, :, i] = np.fft.fft2(input_img[:, :, i])
    result[:, :, i] = np.multiply(result[:, :, i], kernel_fft)
    result[:, :, i] = np.fft.ifft2(result[:, :, i]) / 255.0

# Convolution of signal and filter
# for i in range(c):
#      result[:, :, i] = scipy.signal.convolve2d(input_img[:, :, i], kernel, 'same') / 255.0

# print(result)
plt.imshow(result)
plt.axis('off')
plt.show()
