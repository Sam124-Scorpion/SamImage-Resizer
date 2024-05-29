import cv2

source = "jano.jpg"
destination = "Now-show.jpg"
image = cv2.imread(source,cv2.IMREAD_UNCHANGED)

cv2.imshow("title",image)
cv2.waitKey(0)

scale_percent = 50;

height = int(image.shape[1] * scale_percent / 100)
width = int(image.shape[0] * scale_percent / 100)

dsize = (height,width)

resImage = cv2.resize(image,dsize)

#height,width = image.shape[:2]
#resImage = cv2.resize(image,(int(height/2) , int(width/2)), interpolation = cv2.INTER_AREA)

cv2.imshow("Now-show",resImage)
cv2.imwrite(destination,resImage)

cv2.waitKey(0)