import numpy as np
import cv2
import os
import pdb
#function that creates 3D array
#function that walks through the os,varies with user

def	img_array(path='c:/Users/Charles/Desktop/LSAT8'):
	#State the path where the images are located
	#path='/home/croberson/LSAT8'
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
	path='c:/Users/Charles/Desktop/LSAT8'
	blues=np.array([])
	greens=np.array([])
	reds=np.array([])
	image_files=['LC80250392016062LGN00_B2.TIF','LC80250392016062LGN00_B8.TIF','LC80250392016062LGN00_B8.TIF']
	img_red = cv2.imread(path+image_files[0])
	img_green=cv2.imread(path+image_files[1])
	img_blue=cv2.imread(path+image_files[2])
	
	#We need to verify the shape of the images to ensure integrity
	#print img_red.shape, img_green.shape, img_blue.shape
	# Each band that we need is used for different studies
	# Band for terrain occlusion (2), water (3), and vegetation (4)
	# Band 8 is for cloud coverage (supposed panochromatic)? will look into BIT for landsatlook quality images
	
	# if reading with cv2, use 1 for color, 0 for grayscale, -1 for alpha 
	img_band2 = cv2.imread("C:/Users/Charles/Desktop/LSAT8/LC80250392016062LGN00_B2.TIF", 1)
	print(img_band2.shape)
	
	# Resize the band if needed to view the image before saving
	small_band2 = cv2.resize(img_band2, (500,500))
	cv2.imshow('blue band', small_band2)
	k = cv2.waitKey(0)
	
	# wait for escape key to be pressed to terminate 
	if k == 27:
		cv2.destroyAllWindows()
	# save the image when the s key is pressed
	elif k == ord('s'):
		cv2.imwrite('band 2', small_band2)
		cv2.destroyAllWindows()
	return

def	main():
	#State the path where the images are located
	#path='/home/melrobin/research/chrism/landsat8-processing/LSAT8'
	path='c:/Users/Charles/Desktop/LSAT8'
	
	#Create the array
	my_array=img_array(path)
	
	#Print the array
	print_img(my_array)

main()
