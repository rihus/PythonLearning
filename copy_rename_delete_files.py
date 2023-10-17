# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 11:47:21 2023

@author: Riaz Hussain, PhD
"""
#%% Import files from one
import os
import shutil
import re
import glob
#%%%
#%%to copy files from subdirectories to corresponding subdirectories in new location
source_directory = r"C:\Users\HUSDQ4\Desktop\Images for Keyhole Reconstruction\UniDens Healthy"
destination_directory = r"C:\Users\HUSDQ4\OneDrive - cchmc\cincy_work\human_data\VDP_analysis\ILD_HCs"
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

#%%Detecting cetain files in provided directories
source_directory_gre = r"C:\Users\HUSDQ4\OneDrive - cchmc\cincy_work\human_data\VDP_analysis\CFNonCF_Bronch\IRC740H_2Dcartesian"
source_directory_spiral = r"C:\Users\HUSDQ4\OneDrive - cchmc\cincy_work\human_data\VDP_analysis\CFNonCF_Bronch\IRC740H_2Dspiral"

# Loop through all directories and files in the source directory
for root, dirs, files in os.walk(source_directory_spiral):
    for file in files:
        # Check if the file matches the pattern: IRC740H-[number 3digits]_Vent_[date].nii'gz
        # name_match_orig = re.search(r'IRC740H-(?P<number>\d+)_Vent_(?P<date>\d{8})\.nii\.gz$', file)
        # name_match_N4 = re.search(r'IRC740H-(?P<number>\d+)_Vent_(?P<date>\d{8})_N4\.nii\.gz$', file)
        # name_match_mask = re.search(r'IRC740H-(?P<number>\d+)_Vent_(?P<date>\d{8})_mask\.nii\.gz$', file)
        name_match_orig = re.search(r"img_ventilation\.nii\.gz$", file)
        name_match_N4 = re.search(r"img_ventilation_N4\.nii\.gz$", file)
        name_match_keyhole = re.search(r"img_ventilation_corrected\.nii\.gz$", file)
        name_match_mask = re.search(r"img_ventilation_mask\.nii\.gz$", file)
        if name_match_orig:
            print(f"\nFound the orig image in {root}")
            # number = name_match_orig.groupdict().get('number')
            # print("Number:", number)
            # date = name_match_orig.groupdict().get('date')
            # print("Date:", date)
            # Delete the desired file or (empty) folder
            #os.remove("demofile.txt")
            #os.rmdir()
        elif name_match_N4:
            print("Found the N4 cor image")
        elif name_match_keyhole:
            print("Found FA keyhole cor image")
        elif name_match_mask:
            print("Found the mask")
         

#%%Deleting files in certain directories
#SOURCE_DIR = r"C:\Users\HUSDQ4\OneDrive - cchmc\cincy_work\human_data\VDP_analysis\CFNonCF_Bronch\IRC740H_2Dcartesian"
#SOURCE_DIR = r"C:/Users/HUSDQ4/OneDrive - cchmc/cincy_work/human_data/VDP_analysis/healthy_subjects/"
SOURCE_DIR = r"C:\Users\HUSDQ4\Desktop\Images_for_Keyhole_Reconstruction\UniDens_CF_Visit1"
#COMMON_STRING = "ILD-HC-0"
COMMON_STRING = "IRC740H-0"
FILE_2_DEL = "img_ventilation_mask.nii.gz"
# FOLDER_2_DEL1 = "vdp_analysis_Orig"
# FOLDER_2_DEL2 = "vdp_analysis_N4"
#FOLDER_2_DEL3 = "vdp_analysis_FAkey"

# Walk through all the directories and subdirectories that contain the common_string
for root, dirs, files in os.walk(SOURCE_DIR, topdown=True):
    for name in dirs:
        if COMMON_STRING in name:
            print(name)
            # Check if the folder to delete exists
            # print(root + "\\" + name + "\\" + FOLDER_2_DEL1)
            # print("found the folder: ", FOLDER_2_DEL1)
            # shutil.rmtree(root + "\\" + name + "\\" + FOLDER_2_DEL1)
            # print("found the folder: ", FOLDER_2_DEL2)
            # shutil.rmtree(root + "\\" + name + "\\" + FOLDER_2_DEL2)
            # print("found the folder: ", FOLDER_2_DEL3)
            # shutil.rmtree(root + "\\" + name + "\\" + FOLDER_2_DEL3)
            if FILE_2_DEL in os.listdir(root + "\\" + name):
                # Delete the file
                print("found the file: ", FILE_2_DEL)
                os.remove(root + "\\" + name + "\\" + FILE_2_DEL)      

#%%