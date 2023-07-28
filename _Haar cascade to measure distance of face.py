#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np

REFERENCE_OBJECT_WIDTH = 0.15  # 15 centimeters
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default (1).xml')

cap = cv2.VideoCapture(0)
focal_length = 1000.0
principal_point = (640, 480)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
    for (x, y, w, h) in faces:
        face_width_pixels = w
        

        distance = (REFERENCE_OBJECT_WIDTH * focal_length) / face_width_pixels
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, f"Distance: {distance:.2f} meters", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        cv2.imshow('Frame', frame)
    
    if cv2.waitKey(1) & 0xFF == 13:
        break

cap.release()
cv2.destroyAllWindows()


# In[ ]:




