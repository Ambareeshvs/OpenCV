"""
Author: Ambareesh V Sankaran
Email: ambareeshvs@gmail.com
"""

import cv2
import numpy as np
import require

imgWidth = 480
imgHeight = 540
require.trackbar()

while(True):
    img = cv2.imread("Image.jpg")
    img = cv2.resize(img,(imgWidth,imgHeight))
    
    img_copy = img.copy()
    img_copy1 = img.copy()
    
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    thresh = require.trackvalue()
    threshold = cv2.Canny(blur, thresh[0], thresh[1])
    threshold = cv2.dilate(threshold, np.ones((3,3)),iterations = 1)
    #cv2.imshow("Threshold", threshold)
    
    contours,_ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img_copy, contours, -1, (0,255,0),4)  
    biggest_C,max_area_C = require.biggest(contours)
    print(biggest_C.shape)
    if biggest_C.size != 0:
        biggest = require.arrange(biggest_C)
        cv2.drawContours(img_copy1, biggest, -1, (0,255,0),15)
        image = require.drawrect(img_copy1,biggest)
        cv2.imshow("Scannning", image)
        
        point1 = np.float32(biggest)
        point2 = np.float32([(0,0),(imgWidth,0),(imgWidth,imgHeight),(0,imgHeight)])
        transformed = cv2.getPerspectiveTransform(point1, point2)
        final_img = cv2.warpPerspective(img, transformed, (imgWidth,imgHeight)) 
        cv2.imshow("Output", final_img)
        
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cv2.destroyAllWindows()