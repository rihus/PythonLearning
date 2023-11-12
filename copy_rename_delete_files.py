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
PARENT_DIR = r"C:\Users\HUSDQ4\Desktop\Images for Keyhole Reconstruction\UniDens Healthy"
destination_directory = r"C:\Users\HUSDQ4\OneDrive - cchmc\cincy_work\human_data\VDP_analysis\ILD_HCs"
file_to_copy = 'img_ventilation_corrected.nii.gz'

for root, dirs, files in os.walk(PARENT_DIR):
    for dir in dirs:
        if file_to_copy in os.listdir(os.path.join(root, dir)):
            source_file = os.path.join(root, dir, file_to_copy)
            destination_dir = os.path.join(destination_directory, dir)
            destination_file = os.path.join(destination_dir, file_to_copy)
            print(f'Copying {source_file} to {destination_file}')
            shutil.copy(source_file, destination_file)


#%%Renaming files in a prticular directory
PARENT_DIR = r'C:\Users\HUSDQ4\OneDrive - cchmc\cincy_work\human_data\VDP_analysis\ILD_HCs'
file_to_rename = 'img_ventilation_corrected.nii.gz'

# Define a regular expression pattern to match the desired file name format
pattern = r'^ILD-HC-\d{3}_Vent_\d{8}\.nii\.gz$'

# Loop through all directories and files in the source directory
for root, dirs, files in os.walk(PARENT_DIR):
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
PARENT_DIR = (r"C:\Users\HUSDQ4\OneDrive - cchmc\cincy_work\human_data\VDP_analysis"
              r"\CFNonCF_Bronch\IRC740H_2Dcartesian_Healthy")
#Indentify files to be renamed
ORIG_FILE = r'^IRC740H-\d{3}c_Vent_\d{8}\.nii\.gz$'
N4_FILE = r'^IRC740H-\d{3}c_Vent_\d{8}_N4\.nii\.gz$'
#FA_FILE = r'^ILD-HC-\d{3}_Vent_\d{8}_corrected\.nii\.gz$'
MASK_FILE = r'^IRC740H-\d{3}c_Vent_\d{8}_mask\.nii\.gz$'
PROTON_FILE = r'^IRC740H-\d{3}c_Vent_\d{8}_proton\.nii\.gz$'

#New file names
ORIG_NEW_NAME = 'img_ventilation.nii.gz'
N4_NEW_NAME = 'img_ventilation_N4.nii.gz'
FA_NEW_NAME = 'img_ventilation_corrected.nii.gz'
MASK_NEW_NAME = 'img_ventilation_mask.nii.gz'
PROTON_NEW_NAME = 'img_proton.nii.gz'

# Loop through all directories and files in the source directory
for root, dirs, files in os.walk(PARENT_DIR):
    for file in files:
        # Check if the file name matches the original file name pattern
        if re.match(ORIG_FILE, file):
            # Construct the new file name by replacing the original file name with the new file name
            new_file1 = re.sub(ORIG_FILE, ORIG_NEW_NAME, file)
            # Construct the full file paths
            old_file_path1 = os.path.join(root, file)
            new_file_path1 = os.path.join(root, new_file1)
            print(f'Renamed file: \n {old_file_path1} -> {new_file_path1}')
            # Rename the file
            os.rename(old_file_path1, new_file_path1)
        elif re.match(N4_FILE, file):
            # Construct the new file name by replacing the original file name with the new file name
            new_file2 = re.sub(N4_FILE, N4_NEW_NAME, file)
            # Construct the full file paths
            old_file_path2 = os.path.join(root, file)
            new_file_path2 = os.path.join(root, new_file2)
            print(f'Renamed file: \n {old_file_path2} -> {new_file_path2}')
            # Rename the file
            os.rename(old_file_path2, new_file_path2)
        # elif re.match(FA_FILE, file):
        #     # Construct the new file name by replacing the original with the new
        #     new_file3 = re.sub(FA_FILE, FA_NEW_NAME, file)
        #     # Construct the full file paths
        #     old_file_path3 = os.path.join(root, file)
        #     new_file_path3 = os.path.join(root, new_file3)
        #     print(f'Renamed file: \n {old_file_path3} -> {new_file_path3}')
        #     # Rename the file
        #     os.rename(old_file_path3, new_file_path3)
        elif re.match(MASK_FILE, file):
            # Construct the new file name by replacing the original with the new
            new_file4 = re.sub(MASK_FILE, MASK_NEW_NAME, file)
            # Construct the full file paths
            old_file_path4 = os.path.join(root, file)
            new_file_path4 = os.path.join(root, new_file4)
            print(f'Renamed file: \n {old_file_path4} -> {new_file_path4}')
            # Rename the file
            os.rename(old_file_path4, new_file_path4)
        elif re.match(PROTON_FILE, file):
            # Construct the new file name by replacing the original with the new
            new_file4 = re.sub(PROTON_FILE, PROTON_NEW_NAME, file)
            # Construct the full file paths
            old_file_path4 = os.path.join(root, file)
            new_file_path4 = os.path.join(root, new_file4)
            print(f'Renamed file: \n {old_file_path4} -> {new_file_path4}')
            # Rename the file
            os.rename(old_file_path4, new_file_path4)

#%%Detecting cetain files in provided directories
SOURCE_DIR = (r"C:\Users\HUSDQ4\OneDrive - cchmc\cincy_work\human_data\VDP_analysis"
                        r"\CFNonCF_Bronch\IRC740H_2Dcartesian")
# SOURCE_DIR = (r"C:\Users\HUSDQ4\OneDrive - cchmc\cincy_work\human_data\VDP_analysis"
#                     r"\CFNonCF_Bronch\IRC740H_2Dspiral_CF")
TOTAL_SUBJS1=0
TOTAL_SUBJS2=0
TOTAL_SUBJS3=0
TOTAL_SUBJS4=0
TOTAL_SUBJS5=0
# Loop through all directories and files in the source directory
for root, dirs, files in os.walk(SOURCE_DIR):
    for file in files:
        # Check if the file matches the pattern: IRC740H-[number 3digits]_Vent_[date].nii'gz
        # name_match_orig = re.search(r'IRC740H-(?P<number>\d+)_Vent_(?P<date>\d{8})\.nii\.gz$', file)
        # name_match_N4 = re.search(r'IRC740H-(?P<number>\d+)_Vent_(?P<date>\d{8})_N4\.nii\.gz$', file)
        # name_match_mask = re.search(r'IRC740H-(?P<number>\d+)_Vent_(?P<date>\d{8})_mask\.nii\.gz$', file)
        name_match_orig = re.search(r"img_ventilation\.nii\.gz$", file)
        name_match_N4 = re.search(r"img_ventilation_N4\.nii\.gz$", file)
        name_match_keyhole = re.search(r"img_ventilation_corrected\.nii\.gz$", file)
        name_match_mask = re.search(r"img_ventilation_mask\.nii\.gz$", file)
        name_match_proton = re.search(r"img_proton\.nii\.gz$", file)
        if name_match_orig:
            TOTAL_SUBJS1 = TOTAL_SUBJS1 + 1
            print(f"DIR:{root}")
            print("Found the orig image")
            # number = name_match_orig.groupdict().get('number')
            # print("Number:", number)
            # date = name_match_orig.groupdict().get('date')
            # print("Date:", date)
            # Delete the desired file or (empty) folder
            #os.remove("demofile.txt")
            #os.rmdir()
        elif name_match_N4:
            TOTAL_SUBJS3 = TOTAL_SUBJS3 + 1
            print("Found the N4 cor image\n")
        elif name_match_keyhole:
            TOTAL_SUBJS5 = TOTAL_SUBJS5 + 1
            print("Found FA keyhole cor image")
        elif name_match_mask:
            TOTAL_SUBJS4 = TOTAL_SUBJS4 + 1
            print("Found the mask")
        elif name_match_proton:
            TOTAL_SUBJS2 = TOTAL_SUBJS2 + 1
            print("Found the proton")
print(f"Total uncorrected {TOTAL_SUBJS1}")
print(f"Total N4 corrected {TOTAL_SUBJS3}")
print(f"Total keyhole corrected {TOTAL_SUBJS5}")
print(f"Total proton images {TOTAL_SUBJS2}")
print(f"Total mask images {TOTAL_SUBJS4}")

#%%Deleting files/folder in certain directories
SOURCE_DIR = (r"C:\Users\HUSDQ4\OneDrive - cchmc\cincy_work\human_data\VDP_analysis"
              r"\CFNonCF_Bronch\IRC740H_2Dcartesian")
SOURCE_DIR = (r"C:/Users/HUSDQ4/OneDrive - cchmc/cincy_work/human_data/VDP_analysis"
              "/healthy_subjects/")
#SOURCE_DIR = r"C:\Users\HUSDQ4\Desktop\Images_for_Keyhole_Reconstruction\UniDens_CF_Visit1"
#COMMON_STRING = "ILD-HC-0"
COMMON_STRING = "IRC740H-0"
#FILE_2_DEL = "flip_angle_map_mask.nii.gz"
#FILE_EXTENSIONS = ['.list', '.data', '.raw', '.lab', '.sin', '.npy']
FILE_EXTENSIONS = ['.txt']
FOLDER_2_DEL1 = "vdp_analysis_Orig"
FOLDER_2_DEL2 = "vdp_analysis_N4"
#FOLDER_2_DEL3 = "vdp_analysis_FAkey"

# Walk through all the directories and subdirectories that contain the common_string
for root, dirs, files in os.walk(SOURCE_DIR, topdown=True):
    for name in dirs:
        if COMMON_STRING in name:
            print(name)
            # Check if the folder to delete exists
            print(root + "\\" + name + "\\" + FOLDER_2_DEL1)
            print("found the folder: ", FOLDER_2_DEL1)
            shutil.rmtree(root + "\\" + name + "\\" + FOLDER_2_DEL1)
            print("found the folder: ", FOLDER_2_DEL2)
            shutil.rmtree(root + "\\" + name + "\\" + FOLDER_2_DEL2)
            # print("found the folder: ", FOLDER_2_DEL3)
            # shutil.rmtree(root + "\\" + name + "\\" + FOLDER_2_DEL3)
            # if FILE_2_DEL in os.listdir(root + "\\" + name):
            #     # Delete the file
            #     print(f"Found and deleted: {FILE_2_DEL}")
            #     os.remove(root + "\\" + name + "\\" + FILE_2_DEL)
            for ext in FILE_EXTENSIONS:
                files_to_delete = glob.glob(os.path.join(root, name, f"*{ext}"))
                for file_to_delete in files_to_delete:
                    try:
                        os.remove(file_to_delete)
                        print(f"Found and deleted: {file_to_delete}")
                    except OSError as e:
                        print(f"Error deleting {file}: {e}")

#%%
