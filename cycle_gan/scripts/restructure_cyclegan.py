import os
import pickle
import shutil
from sklearn.model_selection import train_test_split

CONST_DIFFICULTIES = ["4", "6", "8", "9", "11", "13", "15", "17"]

WORK_DIR = os.path.dirname(os.path.realpath(__file__))

INPUT_DIR = os.path.join(WORK_DIR, "../unstructured_data/Constellations_All_003")
OUTPUT_DIR = os.path.join(WORK_DIR, "../datasets/")

OUTPUT_FOLDERS = ["A_n003"]


# Used for python version less than 3.9
def remove_suffix(input_string, suffix):
    if suffix and input_string.endswith(suffix):
        return input_string[:-len(suffix)]
    return input_string


def copy_to_AB(list_of_cons_and_outs, output_folders, set_name, const_difficulty):
    for image_paths, output_folder in zip(list_of_cons_and_outs, output_folders):
        for image_path in image_paths:
            destination_path = os.path.join(OUTPUT_DIR, f"{output_folder}_d{const_difficulty}", set_name)
            destination_filename = shutil.copy(image_path, destination_path)
            renamed_file = remove_suffix(destination_filename[:-4], "_" + const_difficulty) + ".jpg" # Remove difficulty from name
            os.rename(destination_filename, renamed_file)


for output_folder in OUTPUT_FOLDERS:
    for set in ["trainA", "trainB", "testA", "testB"]:
        for CONST_DIFFICULTY in CONST_DIFFICULTIES:
            os.makedirs(os.path.join(OUTPUT_DIR, f"{output_folder}_d{CONST_DIFFICULTY}", set))



for CONST_DIFFICULTY in CONST_DIFFICULTIES:

    OUTLINE_FILEPATHS = []
    CONSTELLATION_FILEPATHS = []


    for (dirpath, dirnames, filenames) in os.walk(INPUT_DIR):
        if dirpath.endswith("Outline"):
            if len(filenames) > 1:
                print("Warning, more than one outline in outline folder")
            OUTLINE_FILEPATHS.append(os.path.join(dirpath, filenames[0]))

        if dirpath.endswith("constellations"):
            file_of_interest = next(file for file in filenames if file[:-4].endswith(CONST_DIFFICULTY))
            CONSTELLATION_FILEPATHS.append(os.path.join(dirpath, file_of_interest))
