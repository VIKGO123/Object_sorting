import cv2
import numpy as np

img=cv2.imread("C:/Users/hp/Desktop/paint6.jpg")
cv2.imshow("original",img)
cv2.waitKey(0)

gray=cv2.imread("C:/Users/hp/Desktop/paint6.jpg",0)
cv2.waitKey(0)

#find canny edge
edged=cv2.Canny(gray,30,200)
cv2.imshow("canny edged",edged)
cv2.waitKey(0)
#Finding contour
_,contours,hierarchy=cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)#"""WE CAN USE INPLACE OF EXTERNAL LIST OR TREE """

cv2.imshow("cannY after EDing",edged)
cv2.waitKey(0)
print("Number of contours found",str(len(contours)))
a=[]
for i in range(len(contours)):
    area=cv2.contourArea(contours[i])
    a.append(area)
    print(area)

k=sorted(a);



for i in range(3):
    cv2.putText(img,str(4-i),(contours[i][0][0][0],contours[i][0][0][1]),cv2.FONT_HERSHEY_COMPLEX,2,(100,170,0),3)
    
cv2.putText(img,'1',(35,55),cv2.FONT_HERSHEY_COMPLEX,2,(100,170,0),3)#used outside loop because text crosses image size so appropiate coordinate is choosen

cv2.drawContours(img,contours,-1,(0,255,0),3)
cv2.imshow("contours",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

      
