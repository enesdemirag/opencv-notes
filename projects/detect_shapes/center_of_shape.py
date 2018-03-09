import imutils
import cv2

cam = cv2.VideoCapture(0)
t, image = cam.read()
cv2.imwrite("shot.jpg", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if imutils.is_cv2() else contours[1]

for c in contours:
    M = cv2.moments(c)
    try:
        cX = int(M['m10'] / M['m00'])
        cY = int(M['m01'] / M['m00'])
    except (ZeroDivisionError):
        cX = 0
        cY = 0
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
    cv2.putText(image, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    cv2.imshow("Image", image)
    cv2.waitKey(0)
cv2.destroyAllWindows()
