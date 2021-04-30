import cv2
import numpy as np
from matplotlib import pyplot as plt
import easyocr

# img_path = "stop.jpg"
# reader = easyocr.Reader(['en'], gpu = False)
# result = reader.readtext(img_path)
# print (result)


# img = cv2.imread(img_path)

# for detection in result: 
#     top_left = tuple(detection[0][0])
#     bottom_right = tuple(detection[0][2])
#     text = detection[0]
#     img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),2)

#     print (text)

# plt.imshow(img)
# plt.show()


# realtime recognition
cap = cv2.VideoCapture(0)
reader = easyocr.Reader(['en'], gpu = False)

while True :
    _, frame = cap.read()
    result = reader.readtext(frame)
    for detection in result:
        top_left = tuple(detection[0][0])
        bottom_right = tuple(detection[0][2])
        text = detection[1]
        print (text)
        img = cv2.rectangle(frame,top_left,bottom_right,(0,255,0),2)
    cv2.imshow("Text Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
