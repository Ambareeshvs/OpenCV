"""
Author: Ambareesh V Sankaran
Email: ambareeshvs@gmail.com
"""

import cv2
import numpy as np

def drawrect(img,c_points):
    print(c_points)
    cv2.line(img, (c_points[0][0][0],c_points[0][0][1]), (c_points[1][0][0],c_points[1][0][1]), (0,255,0),3)
    cv2.line(img, (c_points[0][0][0],c_points[0][0][1]), (c_points[3][0][0],c_points[3][0][1]), (0,255,0),3)
    cv2.line(img, (c_points[3][0][0],c_points[3][0][1]), (c_points[2][0][0],c_points[2][0][1]), (0,255,0),3)
    cv2.line(img, (c_points[1][0][0],c_points[1][0][1]), (c_points[2][0][0],c_points[2][0][1]), (0,255,0),3)
    return img

def arrange(point):
    point = point.reshape((4,2))
    dummy = np.zeros((4,1,2),dtype = np.int32)
    add = np.sum(point, axis = 1)
    diff = np.diff(point, axis = 1)
    dummy[0] = point[np.argmin(add)]
    dummy[2] = point[np.argmax(add)]
    dummy[1] = point[np.argmin(diff)]
    dummy[3] = point[np.argmax(diff)]
    return dummy

def biggest(contours):
    c_biggest = np.array([])
    max_area = 0
    for i in contours:
        area = cv2.contourArea(i)
        if area > 3000:
            perimeter = cv2.arcLength(i, True)
            points = cv2.approxPolyDP(i, 0.02*perimeter, True)
            if area > max_area and len(points) == 4:
                c_biggest = points
                max_area = area
    return c_biggest,max_area
                

def func1(x):
    pass

def func2(x):
    pass


def trackbar():
    cv2.namedWindow("Threshold Setup")
    cv2.createTrackbar("Th1", "Threshold Setup", 0, 255, func1)
    cv2.createTrackbar("Th2", "Threshold Setup", 0, 255, func2)
    
def trackvalue():
    thresh1 = cv2.getTrackbarPos("Th1", "Threshold Setup")
    thresh2 = cv2.getTrackbarPos("Th2","Threshold Setup")
    thresh = thresh1,thresh2
    return thresh

