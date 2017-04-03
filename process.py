import numpy as np
import cv2
import os

#function that creates 3D array
#function that walks through the os, varies with user

def img_array():
	# State the path where the images are located 
	path = 'c:/Users/Charles/Desktop/landsat8_images'
	my_array = np.array([])
	
	# Walk through the path and grab the file location names
	for (path, dirs, files) in os.walk(path):
		for file in files:
			if file.endswith('.TIF'):
				thefile = os.path.join(path, file)
				my_array = np.append(my_array, thefile)
	return (my_array)
	
def print_img(my_array):
	# create the emtpy RGB array for images
	red_array = np.array([])
	green_array = np.array([])
	blue_array = np.array([])
	# create each individual RGB
	for elt in my_array:
		location = elt
		img = cv2.imread(location)
		resize_img = cv2.resize(img, (184,184))
		#cv2.imshow('image_1', resize_img)
		'''
		b, g, r = cv2.split(img)
		np.concatenate(blue_array, b)
		np.concatenate(green_array, g)
		np.concatenate(red_array, r)
		'''
		#cv2.imshow('image_2',b)
		#cv2.imshow('image_3',g)
		#cv2.imshow('image_4',r)
		k = cv2.waitKey()
		#press ESC key to close window
		'''
		while (k != 27):
			k = cv2.waitKey()
		cv2.destroyAllWindows()
		'''
	return

def main():
	my_array = img_array()
	print(my_array)
	#print(np.sort(my_array, axis= None))
	#print(my_array.size)
	# Problem with error in CV2, insufficient memory for band 8
	#print_img(my_array)
main()
