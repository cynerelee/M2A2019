# created by Huang Lu
# 27/08/2016 17:05:45 
# Department of EE, Tsinghua Univ.

import cv2
import numpy as np
import os

cap = cv2.VideoCapture('G:\\MICCAI\\dataset 7\\keyframe_5\\data\\rgb.mp4')
Path='G:\\MICCAI\\dataset 7\\keyframe_5\\data\\left_image\\'

if not os.path.isdir(Path):
    os.mkdir(Path)

i=0
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(frame_count)

while(i<frame_count):
    # get a frame
    ret, frame = cap.read()
    # save a frame
   # print(frame.shape,type(frame))
    left=frame[:1024,:,:]
    # show a frame
    #cv2.imshow("capture", left)
    cv2.imwrite(Path+str(i)+".jpg",left)
    i=i+1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()

cv2.destroyAllWindows()