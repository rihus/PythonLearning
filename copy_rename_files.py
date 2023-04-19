# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 11:47:21 2023

@author: Riaz Hussain, PhD
"""
# Import files from one
import os
import shutil
import re

#%%to copy files from subdirectories to corresponding subdirectories in new location
source_directory = r'C:\Users\HUSDQ4\Desktop\Images for Keyhole Reconstruction\UniDens Healthy'
destination_directory = r'C:\Users\HUSDQ4\OneDrive - cchmc\cincy_work\human_data\VDP_analysis\ILD_HCs'
file_to_copy = 'img_ventilation_corrected.nii.gz'

for root, dirs, files in os.walk(source_directory):
    for dir in dirs:
        if file_to_copy in os.listdir(os.path.join(root, dir)):
            source_file = os.path.join(root, dir, file_to_copy)
            destination_dir = os.path.join(destination_directory, dir)
            destination_file = os.path.join(destination_dir, file_to_copy)
            print(f'Copying {source_file} to {destination_file}')
            shutil.copy(source_file, destination_file)


#%%Renaming files in a prticular directory

source_directory = r'C:\Users\HUSDQ4\OneDrive - cchmc\cincy_work\human_data\VDP_analysis\ILD_HCs'
file_to_rename = 'img_ventilation_corrected.nii.gz'

# Define a regular expression pattern to match the desired file name format
pattern = r'^ILD-HC-\d{3}_Vent_\d{8}\.nii\.gz$'

# Loop through all directories and files in the source directory
for root, dirs, files in os.walk(source_directory):
    for file in files:
        # Check if the file matches the pattern "ILD-HC-001_Vent_YYYYMMDD.nii.gz"
        name_match = re.search(r'ILD-HC-(?P<number>\d+)_Vent_(?P<date>\d{8})\.nii\.gz$', file)
        if name_match:
            number = name_match.groupdict().get('number')
            print("\nNumber:", number)
            date = name_match.groupdict().get('date')
            print("Date:", date)
            new_file_name = f'ILD-HC-{number}_Vent_{date}_corrected.nii.gz'
            ## Construct the source and destination file paths
            destination_file = os.path.join(root, new_file_name)
            source_file = os.path.join(root, file_to_rename)
            print(f"File: \n{source_file} \nRenamed as: \n{destination_file}")
            # Copy the file to the destination with the new name
            os.rename(source_file, destination_file)

#%%





