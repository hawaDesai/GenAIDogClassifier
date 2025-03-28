#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function

    results_dic = dict() #results_dic dictionary 
    file_name = listdir(image_dir)
    # start of for loop to run through folder of images
    for filename in range(0,len(file_name),1):
      name = "" #temporary variable that holds name that is lowered and stripped 
      for dog_file_name in file_name[filename].split('_'): #splits names by underscore
        if (dog_file_name.lower().strip() not in results_dic): #if the file name is not in results_dic it will add the file to the dictionary
          if (dog_file_name.isalnum() == True and len(file_name[filename].split('_')) < 3): # if the length of the split is less than two words (eg. basenji vs. )
            results_dic[file_name[filename]] = [dog_file_name.lower().strip()] # adds to the results_dic dictionary
          if (dog_file_name.isalnum() == True and len(file_name[filename].split('_')) > 2):
            name += (dog_file_name + " ")  # adds space in between words
            results_dic[file_name[filename]] = [name.lower().strip()]  #adds to the results_dic dictionary
    #end of for loop to run through folder of images
      

    return results_dic #returns dictionary to pass into other functions
