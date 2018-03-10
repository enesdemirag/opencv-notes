# Bitwise Operations (Mask Images)

# Making a square
square = np.zeros((300, 300), np.uint8)
cv2.rectangle(square, (50, 50), (250, 250), 255, -2)

# Making a ellipse
ellipse = np.zeros((300, 300), np.uint8)
cv2.ellipse(ellipse, (150, 150), (150, 150), 90, 30, 45, 255, -1)

# Shows only where they intersect
bitwiseAnd = cv2.bitwise_and(square, ellipse)

# Shows where either square or ellipse is
bitwiseOr = cv2.bitwise_or(square, ellipse)

# Shows where either exist by itself
bitwiseXor = cv2.bitwise_xor(square, ellipse)

# Shows everything that isn't part of the square
bitwiseNot = cv2.bitwise_not(square) # Inversing an image
