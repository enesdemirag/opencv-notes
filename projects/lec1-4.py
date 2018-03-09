import numpy as np
import cv2
from matplotlib import pyplot as plt

#Normal
input = cv2.imread("media/daytime.jpg")
cv2.imshow("Nature", input)
cv2.waitKey()
cv2.destroyAllWindows()

#Translation
height, width = input.shape[:2]
shift_height, shift_width = height/4, width/4
T = np.float32([[1, 0, shift_width], [0, 1, shift_height]])
img_translation = cv2.warpAffine(input, T, (width, height))
cv2.imshow("Translation", img_translation)
cv2.waitKey()
cv2.destroyAllWindows()

#Rotation
rotated_image = cv2.transpose(input)
cv2.imshow("Rotation", rotated_image)
cv2.waitKey()
cv2.destroyAllWindows()

#Resize
img_scaled = cv2.resize(input, None, fx=0.2, fy=0.7, interpolation = cv2.INTER_CUBIC)
cv2.imshow("Resize", img_scaled)
cv2.waitKey()
cv2.destroyAllWindows()

#Flip
flipped_image = cv2.flip(input, 0)
cv2.imshow("Flip", flipped_image)
cv2.waitKey()
cv2.destroyAllWindows()

#Crop
height, width = input.shape[:2]
start_row, start_col = 100, 100
end_row, end_col = height - 100, width - 100
cropped = input[start_row:end_row , start_col:end_col]
cv2.imshow("Crop", cropped)
cv2.waitKey()
cv2.destroyAllWindows()

#Grayscale
grayscale = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", grayscale)
cv2.waitKey()
cv2.destroyAllWindows()

#HSV
hsv_image = cv2.cvtColor(input, cv2.COLOR_BGR2HSV)
cv2.imshow('Hue channel', hsv_image[:, :, 0])
cv2.imshow('Saturation channel', hsv_image[:, :, 1])
cv2.imshow('Value channel', hsv_image[:, :, 2])
cv2.waitKey()
cv2.destroyAllWindows()

#BGR
cv2.imshow("Red", input[:, :, 2])
cv2.imshow("Green", input[:, :, 1])
cv2.imshow("Blue", input[:, :, 0])
cv2.waitKey()
cv2.destroyAllWindows()

#Filter
B, G, R = cv2.split(input)
filter_image = cv2.merge([B+100, G-20, R+10])
cv2.imshow("Filter", filter_image)
cv2.waitKey()
cv2.destroyAllWindows()

#Actual BGR
zeros = np.zeros(input.shape[:2], dtype = "uint8")
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey()
cv2.destroyAllWindows()

#Brightness
M = np.ones(input.shape, dtype = "uint8")
bright_image = cv2.add(input, M*100)
dark_image = cv2.subtract(input, M*100)
cv2.imshow("Bright", bright_image)
cv2.imshow("Dark", dark_image)
cv2.waitKey()
cv2.destroyAllWindows()

#Text
cv2.putText(input, 'Hello World!', (150,150), cv2.FONT_HERSHEY_COMPLEX, 2, (100,170,0), 3)
cv2.imshow("Text", input)
cv2.waitKey()
cv2.destroyAllWindows()

#Histogram
histogram = cv2.calcHist([input], [0], None, [256], [0, 256])
plt.plot(histogram)
plt.hist(input.ravel(), 256, [0, 256])
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()

#Histogram BGR
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histogram = cv2.calcHist([input], [i], None, [256], [0, 256])
    plt.plot(histogram, color = col)
    plt.xlim([0,256])
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()
