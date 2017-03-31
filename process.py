import numpy as np
import cv2
import os

#function that creates 3D array
#function that walks through the os, varies with user

def img_array():
	path = 'c:/Users/Charles/Desktop/landsat8_images'
	for (path, dirs, files) in os.walk(path):
		#print(path)
		#print(files)
		for file in files:
			if file.endswith('.TIF'):
				print(file)
	return
	
def print_img():
	#load the color image in grayscale 0
	#location = '*.tif'
	img = cv2.imread(location)
	cv2.imshow('image_1',img)
	b, g, r = cv2.split(img)
	cv2.imshow('image_2',b)
	cv2.imshow('image_3',g)
	cv2.imshow('image_4',r)
	k = cv2.waitKey()
	#press ESC key to close window
	while (k != 27):
		k = cv2.waitKey()
	cv2.destroyAllWindows()
	return

def main():
	img_array()
main()
