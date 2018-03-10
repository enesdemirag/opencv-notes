Dilation # Adds pixels to the boundaries of objects in an image
Erosion  # Removes pixels at the boundaries of objects in an image
Opening  # Erosion + Dilation
Closing  # Dilation + Erosion --> Good for removing noise

erosion_image = cv2.erove(image, kernel, iterations = 1)
dilation_image = cv2.dilate(image, kernel, iterations = 1)

#Morphology Operations
opening_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
closing_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
