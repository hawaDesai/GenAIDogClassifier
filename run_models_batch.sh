#!/bin/sh
# */AIPND-revision/intropyproject-classify-pet-images/run_models_batch.sh
#                                                                             
# PROGRAMMER: Jennifer S.
# DATE CREATED: 02/08/2018                                  
# REVISED DATE: 02/27/2018  - 
# PURPOSE: Runs all three models to test which provides 'best' solution.
#          Please note output from each run has been piped into a text file.
#
# Usage: sh run_models_batch.sh    -- will run program from commandline within Project Workspace
#  
python /workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/check_images.py --dir /workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/pet_images --arch resnet  --dogfile dognames.txt > resnet_pet-images.txt
python /workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/check_images.py --dir /workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/pet_images --arch alexnet --dogfile dognames.txt > alexnet_pet-images.txt
python /workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/check_images.py --dir /workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/pet_images --arch vgg  --dogfile dognames.txt > vgg_pet-images.txt
