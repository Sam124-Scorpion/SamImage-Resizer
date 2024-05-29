import cv2
#import numpy as np

image = cv2.imread("jam.png", cv2.IMREAD_UNCHANGED)
cv2.imshow("title", image)

cv2.waitKey(0)

height, width = image.shape[:2]
resImage = cv2.resize(image,(int(width/2), int(height/2)), interpolation = cv2.INTER_AREA)

cv2.imshow('Newimage',resImage)
cv2.waitKey(0)
cv2.destroyAllWindows()