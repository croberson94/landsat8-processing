import numpy as np
import cv2
import os

#function that creates 3D array
#function that walks through the os, varies with user

def img_array():
	rootdir = 'C:/Users/Charles/Downloads/LC80250392016062LGN00.tar/LC80250392016062LGN00'
	for subdir, dirs, files in os.walk(rootdir)
		for file in files:
			print os.path.join(subdir, file)
	my_array = []
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
	print_img()
main()
