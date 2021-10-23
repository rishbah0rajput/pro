import cv2
import random
import time 
start_time = time.time()


def takeImage():
    num=random.randint(1,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        name="image"+str( num )+".jpg"
        cv2.imwrite(name,frame)
        result = True
    videoCaptureObject.release()
    cv2.destroyAllWindows()

while(True):
    if ((time.time() - start_time) >= 5):
        takeImage()