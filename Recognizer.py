import pytesseract
import multiprocessing
try:
    from PIL import Image
except ImportError:
    import Image
global text
text="none"

import cv2
# print(cv2.__version__)
cap = cv2.VideoCapture(0)
# Check if the webcam is opened correctly
if not cap.isOpened():
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open webcam")

def ExtractText(frame):
 img = Image.fromarray(frame)
#  Image.FLIP_LEFT_RIGHT(img)
 global text
#  if(len(text)!=0):
 text = pytesseract.image_to_string(img)
#  t+=1

 print(text)

 

while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    text2='Recognized Text : '+text
    frame = cv2.rectangle(frame, (300,200), (900,500), (255, 0, 0) , 3)
    frame=cv2.putText(frame,text2 , (80, 34), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,165,0), 2, cv2.LINE_AA)
     
    cv2.imshow('ExtractText',frame)
          
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
    roi_gray = gray[200:500, 300:900]
   
    ExtractText(roi_gray)

cap.release()
cv2.destroyAllWindows()