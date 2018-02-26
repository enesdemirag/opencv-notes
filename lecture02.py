from matplotlib import pyplot as plt # for creating histograms

histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])

# images : it is the source image of type uint8 or float32. it should be given in square brackets, ie, "[img]".

# channels : it is also given in square brackets. It is the index of channel for which we calculate histogram. For example, if input is grayscale image, its value is [0]. For color image, you can pass [0], [1] or [2] to calculate histogram of blue, green or red channel respectively.

# mask : mask image. To find histogram of full image, it is given as "None". But if you want to find histogram of particular region of image, you have to create a mask image for that and give it as mask. (I will show an example later.)

# histSize : this represents our BIN count. Need to be given in square brackets. For full scale, we pass [256].

# ranges : this is our RANGE. Normally, it is [0,256].

plt.plot(histogram) # Shows line histogram
plt.hist(image.ravel(), 256, [0, 256]) # With ravel() it shows column histogram
plt.show()

# For seeing all channels (colors) we can use for loop

color = ('b', 'g', 'r')

for i, col in enumerate(color):
    histogram = cv2.calcHist([image], [i], None, [256], [0, 256]) # Inserted i for channel
    plt.plot(histogram, color = col)
    plt.xlim([0,256])
    
plt.show()

image = np.zeros((512,512,3), np.uint8) # Makes a black square 3 for BGR colors
image_bw = np.zeros((512,512), np.uint8) # This is for Black & White image (2 dimension)

cv2.line(image, (0,0), (511,511), (255,127,0), 5) # Draw a line from 0,0 to 512,512 thickness of 5 pixels with the color (255,127,0) blueish

cv2.line(image, starting cordinates, ending cordinates, color, thickness)
cv2.rectangle(image, starting vertex, opposite vertex, color, thickness) # -1 for thickness fills inside 
cv2.cirlce(image, center, radius, color, fill) # -1 for thickness fills inside 

pts = np.array( [[10,50], [400,50], [90,200], [50,500]], np.int32) # Define a polygon with corner points
pts = pts.reshape((-1,1,2)) # Reshape the points to tell cv2 we want a shape
cv2.polylines(image, [pts], True, (0,0,255), 3) 
# Draw a polygon in "image" with [pts] corners 
# True for combine the first and the last points
# color of the polygon is red (0,0,255) and the thickness is 3

cv2.putText(image, 'Hello World!', (75,290), cv2.FONT_HERSHEY_COMPLEX, 2, (100,170,0), 3) # Adding text
# cv2.putText(image, 'Text to Display', bottom left starting point, Font, Font Size, Color, Thickness)




