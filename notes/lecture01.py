import cv2 # Include OpenCV module

input = cv2.imread("path/image.jpg") # Read image

cv2.imshow("Title", input) # Show image

cv2.waitKey() # Wait until key pressed

cv2.waitKey(0) # Same thing

cv2.waitKey(1000) # Close program after 1000 ms (1 sn)

cv2.destroyAllWindows() # Terminate everything

import numpy as np # Include numpy module and named it as np

input.shape # shape attribute gives a tuple of (height,width,rgb value) pixels

input.shape[0] # Height of image
input.shape[1] # Width of image
input.shape[2] # Color dimension

cv2.imwrite("output.jpg", input) # Save image .jpg .png .bmp etc.

grayscale = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY) # Convert image color from BGR to GRAY
# BGR is actually RGB but due to the storing format opencv uses BGR.

input = cv2.imread("path/image.jpg",0) # Automatically read image as grayscale

# Color Spaces: RGB HSV CMYK these are standart for formatting the color in images

# HSV: Hue, Saturation, Value(Brightness)

# ---------------------------------------------------------- #

B, G, R = input[0,0] # Gives BGR values of pixel at x = 0 y = 0

grayscale_img[0,0] # Gives just one value because it just have 1 value and it is shade of gray

hsv_img = cv2.cvtColor(input, cv2.COLOR_BGR2HSV) # Converts RGB to HSV

cv2.imshow('Hue channel', hsv_image[:, :, 0]) # For all pixels (:,:) show just Hue
cv2.imshow('Saturation channel', hsv_image[:, :, 1]) # For all pixels (:,:) show just Saturation
cv2.imshow('Value channel', hsv_image[:, :, 2]) # For all pixels (:,:) show just Value

# For RGB

cv2.imshow("Red", image[:, :, 2])
cv2.imshow("Green", image[:, :, 1])
cv2.imshow("Blue", image[:, :, 0])

# or

B, G, R = cv2.split(image)

cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)

# These 2 samples are not like colors because they are one dimensional images

# ---------------------------------------------------------- #

# We can merge a image to its RGB values and change those values.

B, G, R = cv2.split(image) # First split the RGB values

merged_image = cv2.merge([B+100, G-20, R+10]) # Basic color filter example

# ---------------------------------------------------------- #

# We want to see actual red and greens and blues in image so we need to fill those pixels with zeros

zeros = np.zeros(image.shape[:2], dtype = "uint8") # Using numpy we create a matrix same dimension with our image easily. image.shape[:2] return the height and width values of image

cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))

# Above three lines are the RGB images which we really want