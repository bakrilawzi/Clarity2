import cv2 
import numpy as np
import os 
import sys
path = os.path.join("C:","Users","user","Desktop","Project 308","myvenv","views","utils")
path2 = os.path.join("C:","Users","user","Desktop","Project 308","myvenv","models","utils")
pathroot = os.path.join("C:","Users","user","Desktop","Project 308","myvenv") 
sys.path.append(pathroot)
sys.path.append(path)
sys.path.append(path2)
from views.utils.trackinghand import HandTracker
from time import sleep


class virtualpainter:
     def __init__(self,drawColor = (255,0,255),xp=0,yp=0,imgCanvas=np.zeros((600,600,3),np.uint8)):
          # self.img = cv2.imread(folderPath)
          self.drawColor = drawColor
          self.xp = xp
          self.yp = yp
          self.imgCanvas = imgCanvas
          self.cap = cv2.VideoCapture(0)
          self.cap.set(0,1280)
          self.detector  = HandTracker(detectionThresh=0.85)  
     
     def open_camera(self)->np.array:
          #Import The Image 
               self.ret,self.frame = self.cap.read()
               self.frame = cv2.flip(self.frame,1)              
               # Find hand landmarks
               # print(self.frame)
               self.frames = self.detector.findHands(self.frame)
               self.lmlist  = self.detector.findHandsPosition(self.frame,draw=False)
               # cv2.imshow("Image",self.frame)
               return self.frames
     
     def detection_fingers(self)->list:
          if(len(self.lmlist)!=0):
           #Tip of index and middle finger
              self.x1,self.y1 = self.lmlist[8][1:]
              self.x2,self.y2 = self.lmlist[12][1:]
          #Check which finger is Up
              fingers = self.detector.findFingure()
     
              return fingers
          else:
               return [1,2] 

          
     def selection_mode(self,fingers) -> None:
      
          if(len(fingers)==2):
               pass
          elif fingers[1] and fingers[2]:
             self.xp = 0 
             self.yp = 0
             if cv2.waitKey(10) & 0xFF==ord("s"):
                imgCanvas = np.zeros((600,600,3),np.uint8)
             if cv2.waitKey(10) & 0XFF == ord("d"):
                  cv2.imwrite("Pred.png",imgCanvas)
          #    xp, yp = 0,0
             cv2.rectangle(self.frame,(self.x1,self.y1-25),(self.x2,self.y2+25),(0,255,0),3,cv2.FILLED)
          #    print("Selection Mode")
             if self.y1<125:
                  if 250<self.x1<450:
                    #    print("blue")
                       self.drawColor = (0,0,255)
                  elif 550<self.x1<700:
                    #    print("eraser")
                       self.drawColor=(0,0,0)
                  elif 450<self.x1<700:
                    #    print("green")
                       self.drawColor = (0,255,0)
                  else:
                    #    print("red")
                       self.drawColor = (255,0,0)
             cv2.rectangle(self.frame,(self.x1,self.y1-25),(self.x2,self.y2+25),self.drawColor,cv2.FILLED)
             
          elif fingers[1] and fingers[2]==False:
             cv2.circle(self.frame,(self.x1,self.y1),15,self.drawColor,cv2.FILLED)
          #    print("Drawing Mode")
             if self.xp == 0 and self.yp==0:
                  self.xp,self.yp =self.x1,self.y1

             if cv2.waitKey(10) & 0xFF==ord("s"):
                self.imgCanvas = np.zeros((600,600,3),np.uint8)
             cv2.line(self.frame,(self.xp,self.yp),(self.x1,self.y1),self.drawColor,10) 
             cv2.line(self.imgCanvas,(self.xp,self.yp),(self.x1,self.y1),self.drawColor,10) 
             self.xp,self.yp = self.x1,self.y1
             if cv2.waitKey(10) & 0XFF == ord("d"):
                  cv2.imwrite("Pred.png",self.imgCanvas)
          

     def endin_app(self,frame) -> None:
           frame = cv2.resize(self.frame,(1280,640))
          #  print(frame)
    #Setting The header Image 
          #  frame[0:125,0:1280] = self.img
          #  cv2.imshow("Image",frame)
           cv2.imshow("canvas",self.imgCanvas)
           
     
     def releasing(self) -> None:
          if cv2.waitKey(10) & 0XFF == ord("q"):
              self.cap.release()
              cv2.destroyAllWindows()

          


