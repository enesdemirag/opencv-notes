import numpy as np
import cv2

#Kernels:
|1 1 1|
|1 1 1| x 1/9
|1 1 1|

#Box Filters
kernel_3x3 = np.ones((3,3) , np.float32) / 9
kernel_5x5 = np.ones((5,5) , np.float32) / 25
kernel_7x7 = np.ones((7,7) , no.float32) / 49

#Blur - Normalized
blurred = cv2.filter2D(image, -1, kernel_3x3)

#Blur - Averaged
blured_box = cv2.blur(image, (3,3))

#Blur - Gaussian
blurred_gauss = cv2.GaussianBlur(image, (7,7), 0)

#Blur Median
blurred_median = cv2.medianBlur(image, 5) #Paintted type effect

#Blur - Bilateral
blurred_bileteral = cv2.bilateralFilter(image, 9, 75, 75)
