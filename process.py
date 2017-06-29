import numpy as np
import cv2
import os
import pdb
import sys
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
	
def create_image(my_array,path):
	#Define array clusters
	#path='/home/melrobin/research/chrism/landsat8-processing/LSAT8/'
	#path='c:/Users/Charles/Desktop/LSAT8'
	blues=np.array([])
	greens=np.array([])
	reds=np.array([])
	image_files=['LC80250392017096LGN00_B2.TIF','LC80250392017096LGN00_B3.TIF','LC80250392017096LGN00_B4.TIF']
	img_red = cv2.imread(path+image_files[0])
	img_green=cv2.imread(path+image_files[1])
	img_blue=cv2.imread(path+image_files[2])
        #Display the shapes to ensure that we have the correct spectral images
        print img_red.shape,img_green.shape,img_blue.shape	
	#We need to verify the shape of the images to ensure integrity
	#print img_red.shape, img_green.shape, img_blue.shape
	# Each band that we need is used for different studies
	# Band for terrain occlusion (2), water (3), and vegetation (4)
	# Band 8 is for cloud coverage (supposed panochromatic)? will look into BIT for landsatlook quality images
	
	# if reading with cv2, use 1 for color, 0 for grayscale, -1 for alpha 
	img_band2 = cv2.imread(path+'LC80250392017096LGN00_B2.TIF', 1)
        #Allocate and fill an output array
        final_picture=np.empty(img_band2.shape)
        final_picture[:,:,0]=img_red[:,:,0]
        final_picture[:,:,1]=img_green[:,:,0]
        final_picture[:,:,2]=img_blue[:,:,0]
	# if 1 is chosen, image will have three channels, split required?
	
	# Resize the band if needed to view the image before saving
	small_band2 = cv2.resize(final_picture, (500,500))
	cv2.imshow('blue band',final_picture)
	k = cv2.waitKey(0)
	
	# wait for escape key to be pressed to terminate 
	if k == 27:
		cv2.destroyAllWindows()
	# save the image when the s key is pressed
	elif k == ord('s'):
		cv2.imwrite('band 2', small_band2)
		cv2.destroyAllWindows()
	return

def main():
	#State the path where the images are located
	#path='/home/melrobin/research/chrism/landsat8-processing/LSAT8'
	#path='c:/Users/Charles/Desktop/LSAT8'
    if (len(sys.argv) != 2):
        print "Not enough command line arguments provided...outie!"
        exit()
    path = sys.argv[1]
    #Create the array
    my_array=img_array(path)
	
	#Print the array
    create_image(my_array,path)

main()
