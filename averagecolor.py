#@Author = "Chase Carlson"
#@Name = "Average Color"
#@Date = 10/30/2019
#@Version 1.0

import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import sys

def main(img):

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
	GreenValue =GreenValue / ImageArea
	BlueValue = BlueValue / ImageArea

	return RedValue,GreenValue,BlueValue
