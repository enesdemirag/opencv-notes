import numpy as np
import cv2

#Kernels:
|1 1 1|
|1 1 1| x 1/9
|1 1 1|

#Box Filters
kernel_3x3 = np.ones((3,3) , np.float32) / 9 #Ned to divide 9 due to normalization
kernel_5x5 = np.ones((5,5) , np.float32) / 25
kernel_7x7 = np.ones((7,7) , no.float32) / 49

#Blur - Convolotion
blurred = cv2.filter2D(image, -1, kernel_3x3)

#Blur - Averaged
blured_box = cv2.blur(image, (3,3))

#Blur - Gaussian
blurred_gauss = cv2.GaussianBlur(image, (7,7), 0)

#Blur Median
blurred_median = cv2.medianBlur(image, 5) #Painted type effect

#Blur - Bilateral
blurred_bileteral = cv2.bilateralFilter(image, 9, 75, 75) #Very effective noise but keeps edges sharp

#Image Denoising
#Nonlocal Means Denoising (Cleaning noise and making image more DSLR)
dst = cv2.fastNlMeansDenoisingColored(image, None, 6, 6, 7, 21) # For color image
      cv2.fastNlMeansDenoising()  # Works with single grayscale image
      cv2.fastNlMeansDenoisingMulti() # works with image sequence captured in short period of time (grayscale)
      cv2.fastNlMeansDenoisingColoredMulti() # works with image sequence captured in short period of time (color)


#Sharpening
