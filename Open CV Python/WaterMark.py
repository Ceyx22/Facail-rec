import numpy as np 
import cv2

from utils import CFEVideoConf

cap = cv2.VideoCapture(0)

save_path = 'saved-media/watermark.mp4'
frames_per_seconds = 24
config = CFEVideoConf(cap, filepath=save_path, res='720p')
out = cv2.VideoWriter(save_path, config.video_type, frames_per_seconds, config.dims)

img_path = 'images/logo/cfre-coffee.jpg'
watermark = cv2.imread(img_path, -1)
cv2.imshow('watermark', watermark)

while(True):
    # capture frame by frame
    ret, frame = cap.read()
    #out.write(frame)
    # display the resulting frame       
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF ==ord ('q'):
        break

# when everything done realese the capture 
cap.release()
out.release()
cv2.destroyAllWindows()
