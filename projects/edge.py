import numpy as np
import cv2

def auto_canny(image, sigma = 0.33):
    v = np.median(image)
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    auto_edge = cv2.Canny(image, lower, upper)
    return auto_edge

def resize(image):
    return cv2.resize(image, None, fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)

def show_stages(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    wide = cv2.Canny(blurred, 10, 200)
    tight = cv2.Canny(blurred, 225, 250)
    auto = auto_canny(blurred)

    cv2.imshow("Stages", np.hstack([resize(gray), resize(blurred), resize(wide), resize(tight), resize(auto)]))
    return auto

cam = cv2.VideoCapture(0)
frame_width = int(cam.get(3))
frame_height = int(cam.get(4))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
recorder = cv2.VideoWriter('out.avi',fourcc, 20.0, (frame_width, frame_height))

while True:
    ret, image = cam.read()
    edged_frame = show_stages(image)

    if ret == True:
        recorder.write(edged_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cam.release()
recorder.release()
cv2.destroyAllWindows()
