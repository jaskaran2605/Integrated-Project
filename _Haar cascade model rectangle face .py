#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy
import os
cap = cv2.VideoCapture(0)
model = cv2.CascadeClassifier("haarcascade_frontalface_default (1).xml")
while True:
    status , photo = cap.read()
    myfacecoord = model.detectMultiScale(photo)
    if len(myfacecoord) == 1 :
        x1 = myfacecoord[0][0]
        y1 = myfacecoord[0][1]
        x2 = myfacecoord[0][0] + myfacecoord[0][2]
        y2 = myfacecoord[0][1] + myfacecoord[0][3]
        
        cv2.rectangle(photo , (x1 , y1) , (x2,y2) ,[255 , 0 , 0] , 5)
    cv2.imshow("my_photo" , photo)
    if cv2.waitKey(10) == 13:
        break
        
cv2.destroyAllWindows()  
cap.release()


# In[ ]:




