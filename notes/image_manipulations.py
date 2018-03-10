""" Translation Matrix T = | 1 0 Tx |
                           | 0 1 Ty | """

height, width = image.shape[:2]
shift_height, shift_width = height/4, width/4

T = np.float32([[1, 0, shift_width], [0, 1, shift_height]]) # Translation matrix

# We use warpAffine to transform the image using the matrix T

img_translation = cv2.warpAffine(image, T, (width, height)) # Shifting quarter of its dimesions

""" Rotation Matrix R = | cosx -sinx | x is angle
                        | sinx  cosx | """

R = cv2.getRotationMatrix2D((width/2, height/2), 90, .5) # Rotation Matrix
# cv2.getRotationMatrix2D(rotation_center_x, rotation_center_y, angle of rotation, scale)
# getRotationMatrix2D rotates and scales at the same time

rotated_image = cv2.warpAffine(image, T, (width, height)) #width and height is changed so we now the new values for showing the whole image

rotated_image = cv2.transpose(image) # Another way is transpose() function and there is no black space because of rotating

flipped_image = cv2.flip(image, 0) # Flips image horizontally. Needs negative values or 0 for flip

# Scaling - Resizing - Interpolation

#Interpolation Algorithms
cv2.INTER_AREA          # Good for shrinking or down ampling
cv2.INTER_NEAREST       # Fastest
cv2.INTER_LINEAR        # Good for zooming or up sampling (default)
cv2.INTER_CUBIC         # Better
cv2.INTER_LANCZOS4      # Best

# Resizing image:  cv2.resize(image, dsize(output image size), fx = x scale, fy = y scale, interpolation)

img_scaled = cv2.resize(image, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

# We can use (height, width) instead of None, fx and fy arguments

img_scaled = cv2.resize(image, (900, 400), interpolation = cv2.INTER_AREA)

# Image Pyramids

smaller = cv2.pyrDown(image) # half of the original size
larger = cv2.pyrUp(image)    # double of the original size

# Cropping

height, width = image.shape[:2]
start_row, start_col = 100, 100
end_row, end_col = height - 100, width - 100
cropped = image[start_row:end_row , start_col:end_col]

# Arithmetic Operations - Brightness

M = np.ones(image.shape, dtype = "uint8") # Numpy function for creating matrix of ones

bright_image = cv2.add(image, M*100)
dark_image = cv2.subtract(image, M*100)
