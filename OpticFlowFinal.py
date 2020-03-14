import cv2 
import numpy as np
import math
import random
#Load Video


def valRet():
  cap = cv2.VideoCapture("fast1.mp4")
  flag = 0
  #Taking the first frame and enhancing it
  ret,prevOrg= cap.read()
  prev=cv2.cvtColor(prevOrg,cv2.COLOR_BGR2GRAY)
  kernel = np.array([ [-1,-3,-4,-3,-1],
                      [-3, 0, 6, 0,-3],
                      [-4, 6,20,6,-4],
                      [-3, 0, 6,0,-3],
                      [-1,-3,-4,-3,-1]])
  prev = cv2.filter2D(prev, -1, kernel)
  hsv = np.zeros_like(prevOrg)
  hsv[...,1] = 255
  imgShape=np.shape(prevOrg)
  heightCentre=int(imgShape[0]/2)
  widthCentre=int(imgShape[1]/2)


  #Loop to view the next slides
  while(True):
    ret,currOrg=cap.read()
    writeOrg=currOrg
    curr=cv2.cvtColor(currOrg,cv2.COLOR_BGR2GRAY)
    kernel = np.array([ [-1,-3,-4,-3,-1],
                        [-3, 0, 6, 0,-3],
                        [-4, 6,20,6,-4],
                        [-3, 0, 6,0,-3],
                        [-1,-3,-4,-3,-1]])
    curr = cv2.filter2D(curr, -1, kernel)
  
    flow = cv2.calcOpticalFlowFarneback(prev,curr, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
    cv2.imshow('currOrg', rgb)
    hsv[...,0] = ang*180/np.pi/2
    hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
  
    ####OUTPUT 1
    velocity=np.average(mag)*(5/6)         
    crossectionArea=8000

    ####OUTPUT 2
    currentVolume=velocity*(crossectionArea)
  
  
    T=28;P=0;

    ####OUTPUT 3
    forecastVolume=(math.exp(17+(0.035*P)-(0.0769*T)+(1.137*pow(10,-6)*P*T)))/30
    if forecastVolume>85000:
      flag = 1
    randVal=np.random.randint(7)
    if randVal==3:
      return(velocity,currentVolume,forecastVolume,flag)
    

#cap.release()
#cv2.destroyAllWindows()


