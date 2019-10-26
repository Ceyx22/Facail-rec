import numpy as np 
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame) #imgshow
    cv2.imshow('gray', gray) #imgshow
    cv2.imshow('frame2', frame) #imgshow //can run any amount of frames 
    cv2.imshow('frame3', frame) #imgshow
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break