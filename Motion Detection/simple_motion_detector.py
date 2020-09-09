"""
Author: Ambareesh V Sankaran
Email : ambareeshvs@gmail.com
"""

import cv2

cap = cv2.VideoCapture("Walking Office People.mp4")
ret,frame1 = cap.read()
ret,frame2 = cap.read()

while(cap.isOpened):
    f_diff = cv2.absdiff(frame1, frame2)
    f_gray = cv2.cvtColor(f_diff, cv2.COLOR_BGR2GRAY)
    f_blur = cv2.GaussianBlur(f_gray, (1,1),sigmaX =1, sigmaY = 3)
    ret,f_thresh = cv2.threshold(f_blur, 30, 255, cv2.THRESH_BINARY)
    f_dilate = cv2.dilate(f_thresh,None,iterations = 3)
    f_contour,hierarcy = cv2.findContours(f_dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in f_contour:
        if cv2.contourArea(contour) < 950:
            continue
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame1, (x,y), (x+w,y+h), (0,255,0),2)
    
    cv2.imshow("Output", frame1)

    frame1 = frame2
    ret,frame2 = cap.read()
    
    key = cv2.waitKey(40)
    if key == ord('q'):
        break
cv2.destroyAllWindows()

