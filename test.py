from time import sleep

import torch
import cv2

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Image
vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)
sleep(5)

while (True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # Display the resulting frame
    results = model(frame)

    cv2.imshow('webcam', results.render()[0])

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) == 27:
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
