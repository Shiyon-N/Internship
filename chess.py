import numpy as np
import cv2
b=np.zeros([600,600],dtype='uint8')
list1=np.arange(0,461,150)
list2=np.arange(0,461,150)
for i in list1:
    for j in list2:
        b[i:i+75,j:j+75]=255
list3=np.arange(75,526,150)
list4=np.arange(75,526,150)
for i in list3:
    for j in list4:
        b[i:i+75,j:j+75]=255
       
cv2.imshow('CheckBoard',b)
cv2.waitKey(0)
cv2.destroyAllWindows()
