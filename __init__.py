#@Author = "Chase Carlson"
#@Name = "py-image utilities"
#@Date = 10/30/2019
#@Version = 1.0

import numpy as np
import sys
import matplotlib.pyplot as plt
import random
import cv2 as cv


# Finds the average color inside an image
def averagecolor(img):
	RedValue = 0
	GreenValue = 0
	BlueValue = 0

	img = cv.imread(img)

	height, width, channels = img.shape

	ImageArea = width * height

	for i in range(height):
		for j in range(width):
			color = img[i,j]
			RedValue = RedValue + color[0]
			GreenValue = GreenValue + color[1]
			BlueValue = BlueValue + color[2]

	RedValue = RedValue / ImageArea
	GreenValue = GreenValue / ImageArea
	BlueValue = BlueValue / ImageArea

	return RedValue,GreenValue,BlueValue


# Creates television style static using RGB colors from 0 to 255
def rgbstatic(height, width):

	img_array = np.zeros((height,width,3), np.uint8)
	for i in range(height):
		for j in range(width):
				img_array[i,j] = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
				
	return img_array

