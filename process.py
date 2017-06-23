#!/usr/bin/env python

import numpy as np
import cv2
import os
import pdb
#function that creates 3D array
#function that walks through the os,varies with user

def	img_array(path='c:/Users/Charles/Desktop/landsat8_images'):
	#State the path where the images are located
	path='/home/croberson/LSAT8'
	my_array=np.array([])
	#Walk through the path and grab the file location names
	for(path,dirs,files) in os.walk(path):
		for file in files:
			if file.endswith('.TIF'):
				thefile = os.path.join(path,file)
				my_array = np.append(my_array,thefile)
	return(my_array)
	
def	print_img(my_array):
	#Define array clusters
	#path='/home/melrobin/research/chrism/landsat8-processing/LSAT8/'
	path='/home/croberson/LSAT8'
	blues=np.array([])
	greens=np.array([])
	reds=np.array([])
	image_files=['LC80250392016062LGN00_B2.TIF','LC80250392016062LGN00_B4.TIF','LC80250392016062LGN00_B8.TIF']
	img_red = cv2.imread(path+image_files[0], 0)
	img_green = cv2.imread(path+image_files[1], 0)
	img_blue = cv2.imread(path+image_files[2], 0)
	#We need to verify the shape of the images to ensure integrity
	#print img_red.shape, img_green.shape, img_blue.shape
        red = cv2.imread('/home/croberson/LSAT8/LC80250392016062LGN00_B2.TIF', 0)
        print(red)
        print(red.shape)
	return

def	main():
	#State the path where the images are located
	#path='/home/melrobin/research/chrism/landsat8-processing/LSAT8'
	path='/home/croberson/LSAT8'
	
	#Create the array
	my_array=img_array(path)
	
	#Print the array
	print_img(my_array)

main()
