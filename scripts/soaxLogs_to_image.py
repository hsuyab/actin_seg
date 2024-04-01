from glob import glob
import numpy as np
import matplotlib.pyplot as plt
import os 
import sys
from tqdm import tqdm

#create a function to take in a text path and convert it to image and save it in a location
def text_path_to_image(text_path):
    with open(text_path, 'r') as f:
        lines = f.readlines()
    #find the locations of lines that have '#' in them and store the index for next line in a list
    hash_lines = []
    for i, line in enumerate(lines):
        if '#' in line:
            hash_lines.append(i+1)
    #process the list of list data and convert it into a list of lists of floats
    def actin_data_process(x):
        data = []
        for i in x:
            if '#' in i[0]:
                pass
            else: 
                data.append([float(k.strip()) for k in i])
        
        return data
    #now store the data from the lines starting from the index in the hash_lines list till the next index in the hash_lines list
    # using [i.split() for i in lines[hash_lines[0]:hash_lines[1]]] and then convert the data in a every list to a float
    # and store it in a actin dictionary
    actin = {}
    actin_num = 1
    for i in range(len(hash_lines)-1):
        
        if i == len(hash_lines)-1:
            actin_data = []
            for l in [i.split() for i in lines[hash_lines[i]:]]:
                if int(l[0].strip()) == actin_num: 
                    actin_data.append(l)
        else:
            actin_data = [i.split() for i in lines[hash_lines[i]:hash_lines[i+1]]]
        
        actin[i] = actin_data_process(actin_data)
        actin_num+=1


    #now actin cotinas the data for each actin in the image
    #with each actin having a list of data for 's', 'p', 'x', 'y', 'z', 'fg_int', 'bg_int'
    #now we can use this data to plot the actin data in a 512x512 image
    
    #initialize the image with zeros
    image = np.zeros((512, 512))

    #now we can use the x and y data to plot the actin data in the image
    for i in range(len(actin)):
        x = [int(i[2]) for i in actin[i]]
        y = [int(i[3]) for i in actin[i]]
        image[x, y] = 1

    # #plot the image
    # plt.imshow(image, cmap='gray')
    # plt.show()

    #rotate the image array by flipping it across the y-axis and rotate it by 90 degrees using np.rot90
    image_rotated = np.rot90(np.fliplr(image))

    #save_location = f"soax_to_image/{str(fname)}/"

    #return save_location, image_rotated
    return image_rotated

'''
Need to pass a file path to the function and then get the corresponding image
(   
    '/Users/hsuyab/Documents/Spring 2024/RA Staiger/SOAX project
    /Atharva/SOAX analysis/soax_raw_output_all_files_gray 121923/
    AB(11)/AB (11) g--ridge0.03000--stretch0.7000.txt'

)

img <- text_path_to_image(text_path)

Here img is the img from the soax logs

'''
