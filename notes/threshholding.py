ret, thresh0 = cv2.threshold(image,threshold value, max value, threshold type) #Images need to be converted grayscale before thresholding

#Types (These simple types require us to provide the threshold value)
cv2.THRESH_BINARY # Most common
cv2.THRESH_BINARY_INV # Most common
cv2.THRESH_TRUNC
cv2.THRESH_TOZERO
cv2.THRESH_TOZERO_INV

#Adaptive thresholding (especially with documents) --> no need to choose threshold value
thresh1 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5) #Adaptive Mean Thresholding
ret, thresh2 = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) #Otsu's Thresholding

blur = cv2.GaussianBlur(image, (5, 5), 0)
ret, thresh3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) #Gaussian Otsu's Thresholding
