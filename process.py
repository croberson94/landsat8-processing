import numpy as np
import cv2
import os

#function that creates 3D array
#function that walks through the os, varies with user

def img_array():
	#label the current directory
	return
	#use os.walk or another module thats good for iteration

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
	# download the images
	# create the image array
	my_array = img_array()
	# create the printable image
	# print_img(my_array)
	img_array()
main()
