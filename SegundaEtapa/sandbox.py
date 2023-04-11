import cv2
import numpy as np



def getContourCol(min, max):
    hsvCol = np.array([(min[0] + max[0]) / 2, (min[1] + max[1]) / 2, (min[2] + max[2]) / 2])
    bgrCol = cv2.cvtColor(hsvCol, cv2.COLOR_HSV2BGR) 
    print(bgrCol)



getContourCol([0,0,0], ([255,255,255]))
