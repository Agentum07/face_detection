# face detection

import cv2 as cv

# Load the cascade  
face_cascade = cv.CascadeClassifier('Resources/haarcascade_frontalface_default.xml') 

# load video from the camera
cap = cv.VideoCapture(0, cv.CAP_DSHOW)

cap.set(3, 640)  # width
cap.set(4, 480)  # height
cap.set(10, 100) # brightness

while True:
    success, img = cap.read()
    
    # Detect the face
    faces = face_cascade.detectMultiScale(img, 1.1, 4) 
    
    # Draw the rectangle around each face  
    for (x, y, w, h) in faces:  
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
    cv.imshow("My camera", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyWindow("My camera")
cv.waitKey(1)
