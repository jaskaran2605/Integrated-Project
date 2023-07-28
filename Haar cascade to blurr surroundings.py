#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2
import copy
from scipy.ndimage import gaussian_filter
cap=cv2.VideoCapture(0)
facemodel=cv2.CascadeClassifier("haarcascade_frontalface_default (1).xml")
while True:
    status,photo=cap.read()
    q=facemodel.detectMultiScale(photo)
    if len(q)==1:
        x1=q[0][0]
        y1=q[0][0]
        x2=q[0][0]+tt[0][2]
        y2=q[0][1]+tt[0][3]
        cv2.rectangle(photo,(x1,y1),(x2,y2),[0,255,0],5)
        a=copy.deepcopy(photo)
        blurred_image = gaussian_filter(photo, 2)
        blurred_image[x1:x2,y1:y2,]=photo[x1:x2,y1:y2,]
        cv2.imshow("jas",blurred_image)
        if cv2.waitKey(100)==13:
            break
cv2.destroyAllWindows()
cap.release()


# In[ ]:




