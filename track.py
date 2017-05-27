import numpy as np
import cv2

cap = cv2.VideoCapture('DJI_0092r.MOV')
fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    #Median blur


    median = cv2.medianBlur(fgmask,7)
    cv2.imshow('Median Blur',median)

    
    cv2.imshow('fgmask',frame)
    cv2.imshow('frame',fgmask)
    cv2.imshow('median',median)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    

cap.release()
cv2.destroyAllWindows()

