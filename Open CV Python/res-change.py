import numpy as np 
import cv2

cap = cv2.VideoCapture(0)

def make_1080p():
    cap.set(3, 1920)
    cap.set(4, 1080)

def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)

def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)

def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)

# make_1080p()

# change_res(4000,2000) # will not go past what the webcam is capible of doing and gets really chopy
# do not upscale if anything down scale

def rescale_frame(frame, percent=75):                       # can use to resize scale of video
    width = int(frame.shape[1] * percent/ 100)              # def = void basically
    height = int(frame.shape[0] * percent/ 100)             # can write inside of while loop 
    dim = (width, height)                                   # the way it is now it is reusable
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)    # interpolation is how its going to scale

while(True):
    #capture fram by frame
    ret, frame = cap.read()
    frame = rescale_frame(frame, percent=30)
    #display the resulting frame
    cv2.imshow('frame',frame)                           #using to frames to show dirffrence in size of output
    frame2 = rescale_frame(frame, percent=500)
    cv2.imshow('frame2',frame2)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
# when everything done release the capture
cap.release()
cv2.destroyAllWindows()