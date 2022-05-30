from sklearn.model_selection import train_test_split
import pickle
import shutil
import os

CONST_DIFFICULTIES = ["4", "6", "8", "9", "11", "13", "15", "17"]

WORK_DIR = os.path.dirname(os.path.realpath(__file__))

INPUT_DIR = os.path.join(WORK_DIR, "../unstructured_data/constellation")
OUTPUT_DIR = os.path.join(WORK_DIR, "../datasets/")

OUTPUT_FOLDERS = ["A_n003", "B_n003"]

for output_folder in OUTPUT_FOLDERS:
    for set in ["trainA", "trainB"]:
        # Folder A has multiple difficulties of constellations
        if output_folder.startswith(OUTPUT_FOLDERS[0]):
            for CONST_DIFFICULTY in CONST_DIFFICULTIES:
                os.makedirs(os.path.join(OUTPUT_DIR, f"{output_folder}_d{CONST_DIFFICULTY}", set))
        # But folder B has only one outline corresponding to all difficulties
        else:
            os.makedirs(os.path.join(OUTPUT_DIR, output_folder, set))