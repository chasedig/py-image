#@Author = "Chase Carlson"
#@Name = "RGB Static"
#@Date = 10/30/2019
#@Version = 1.0

import numpy as np
import matplotlib.pyplot as plt
import random
import cv2

def main(height, width):

	img_array = np.zeros((height,width,3), np.uint8)
	for i in range(height):
		for j in range(width):
				img_array[i,j] = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
				
	return img_array
