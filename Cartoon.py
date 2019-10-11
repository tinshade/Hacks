'''

	OPEN-CV & NUMPY CARTOONIZER
	Just a demonstration of using Numpy in OpenCV to manipulate brightness and vibrance,
	along with some experiments

	
'''


import cv2 #Working with images
import numpy as np #Manipulation using numbers

img = cv2.imread("image.png") #Reading the image

# 1) Edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Grayscaling the image
gray = cv2.medianBlur(gray, 5) #Using Median Blur to blur the image
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9) #Detecting edges

# 2) Color
color = cv2.bilateralFilter(img, 9, 300, 300) #This gives the 'WaterColor Effect'

# 3) Cartoon
cartoon = cv2.bitwise_and(color, color, mask=edges) #Creating cartoon image with dark egdes detected above
cv2.imshow("Cartoonized", cartoon) #Displaying the conventional cartoon image as expected

# 4)Manipulations
c1 = cv2.bilateralFilter(color, 50, 250, 50) #1 #Taking the colorized image
c2 = cv2.bitwise_and(c1, color,mask=edges) #2 with edges as the mask
c3 = cv2.bilateralFilter(c2, 2, 50, 50) #Changing values with #2 as input
cv2.imshow("result.jpeg", c3) #Displaying the image
cv2.imwrite("./result.jpeg", c3) #Saving the image in root folder

#NOTE : Images can be outputed in any mainstream format(JPEG, JPG, PNG, BMP, etc;)
cv2.waitKey(0) #Holds the output
cv2.destroyAllWindows() #Destroys the process when all result windows are closed