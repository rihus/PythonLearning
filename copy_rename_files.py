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

#%%Another code for renaming multiple files in multiple directories
source_directory = r'C:\Users\HUSDQ4\OneDrive - cchmc\cincy_work\human_data\VDP_analysis\ILD_HCs'
#Indentify files to be renamed
file_name_orig = r'^ILD-HC-\d{3}_Vent_\d{8}\.nii\.gz$'
file_name_N4 = r'^ILD-HC-\d{3}_Vent_\d{8}N4\.nii\.gz$'
file_name_FAkey = r'^ILD-HC-\d{3}_Vent_\d{8}_corrected\.nii\.gz$'
file_name_mask = r'^ILD-HC-\d{3}_Vent_\d{8}_mask\.nii\.gz$'

#New file names
new_file_name_orig = 'img_ventilation.nii.gz'
new_file_name_N4 = 'img_ventilation_N4.nii.gz'
new_file_name_FAkey = 'img_ventilation_corrected.nii.gz'
new_file_name_mask = 'img_ventilation_mask.nii.gz'

# Loop through all directories and files in the source directory
for root, dirs, files in os.walk(source_directory):
    for file in files:
        # Check if the file name matches the original file name pattern
        if re.match(file_name_orig, file):
            # Construct the new file name by replacing the original file name with the new file name
            new_file1 = re.sub(file_name_orig, new_file_name_orig, file)
            # Construct the full file paths
            old_file_path1 = os.path.join(root, file)
            new_file_path1 = os.path.join(root, new_file1)
            print(f'Renamed file: \n {old_file_path1} -> {new_file_path1}')
            # Rename the file
            os.rename(old_file_path1, new_file_path1)
        elif re.match(file_name_N4, file):
            # Construct the new file name by replacing the original file name with the new file name
            new_file2 = re.sub(file_name_N4, new_file_name_N4, file)
            # Construct the full file paths
            old_file_path2 = os.path.join(root, file)
            new_file_path2 = os.path.join(root, new_file2)
            print(f'Renamed file: \n {old_file_path2} -> {new_file_path2}')
            # Rename the file
            os.rename(old_file_path2, new_file_path2)
        elif re.match(file_name_FAkey, file):
            # Construct the new file name by replacing the original file name with the new file name
            new_file3 = re.sub(file_name_FAkey, new_file_name_FAkey, file)
            # Construct the full file paths
            old_file_path3 = os.path.join(root, file)
            new_file_path3 = os.path.join(root, new_file3)
            print(f'Renamed file: \n {old_file_path3} -> {new_file_path3}')
            # Rename the file
            os.rename(old_file_path3, new_file_path3)
        elif re.match(file_name_mask, file):
            # Construct the new file name by replacing the original file name with the new file name
            new_file4 = re.sub(file_name_mask, new_file_name_mask, file)
            # Construct the full file paths
            old_file_path4 = os.path.join(root, file)
            new_file_path4 = os.path.join(root, new_file4)
            print(f'Renamed file: \n {old_file_path4} -> {new_file_path4}')
            # Rename the file
            os.rename(old_file_path4, new_file_path4)


#%%