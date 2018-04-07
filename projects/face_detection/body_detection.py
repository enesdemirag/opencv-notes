import cv2
import numpy as np

body_cascade = cv2.CascadeClassifier("haarcascade_upperbody.xml")
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    body = body_cascade.detectMultiScale(gray)

    for (x, y, w, h) in body:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 2)

    cv2.imshow("Body Track", img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
