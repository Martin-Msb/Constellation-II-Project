from sklearn.model_selection import train_test_split
import pickle
import shutil
import os

CONST_DIFFICULTIES = ["4", "6", "8", "9", "11", "13", "15", "17"]

WORK_DIR = os.path.dirname(os.path.realpath(__file__))

INPUT_DIR = os.path.join(WORK_DIR, "../unstructured_data/Constellations_All_003")
OUTPUT_DIR = os.path.join(WORK_DIR, "../structured_data/")

OUTPUT_FOLDERS = ["A_n003", "B_n003"]

with open ('../unstructured_data/test_set_imagenames', 'rb') as fp:
    TEST_SET_IMAGENAMES = pickle.load(fp)

def copy_to_AB(list_of_cons_and_outs, output_folders, set_name, const_difficulty):
    for image_paths, output_folder in zip(list_of_cons_and_outs, output_folders):
        for image_path in image_paths:
            if output_folder.startswith(OUTPUT_FOLDERS[0]):
                destination_path = os.path.join(OUTPUT_DIR, f"{output_folder}_d{const_difficulty}", set_name)
            else:
                destination_path = os.path.join(OUTPUT_DIR, output_folder, set_name)
            destination_filename = shutil.copy(image_path, destination_path)

            renamed_file = destination_filename[:-4].removesuffix("_" + const_difficulty) + ".jpg" # Remove difficulty from name
            os.rename(destination_filename, renamed_file)

for output_folder in OUTPUT_FOLDERS:
    for set in ["train", "val", "test"]:
        # Folder A has multiple difficulties of constellations
        if output_folder.startswith(OUTPUT_FOLDERS[0]):
            for CONST_DIFFICULTY in CONST_DIFFICULTIES:
                os.makedirs(os.path.join(OUTPUT_DIR, f"{output_folder}_d{CONST_DIFFICULTY}", set))
        # But folder B has only one outline corresponding to all difficulties
        else:
            os.makedirs(os.path.join(OUTPUT_DIR, output_folder, set))

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

    # CONS -> Constellations, OUTS -> Outlines
    TEST_CONS, TEST_OUTS = [], []
    for TEST_SET_IMAGENAME in TEST_SET_IMAGENAMES:

        for CONSTELLATION_FILEPATH in CONSTELLATION_FILEPATHS:
            if TEST_SET_IMAGENAME == CONSTELLATION_FILEPATH.split("\\")[-3]:
                TEST_CONS.append(CONSTELLATION_FILEPATH)

        for OUTLINE_FILEPATH in OUTLINE_FILEPATHS:
            if TEST_SET_IMAGENAME == OUTLINE_FILEPATH.split("\\")[-3]:
                TEST_OUTS.append(OUTLINE_FILEPATH)
    
    CONSTELLATION_FILEPATHS = [fp for fp in CONSTELLATION_FILEPATHS if fp not in TEST_CONS]
    OUTLINE_FILEPATHS = [fp for fp in OUTLINE_FILEPATHS if fp not in TEST_OUTS]

    TRAIN_CONS, VAL_CONS, TRAIN_OUTS, VAL_OUTS = train_test_split(CONSTELLATION_FILEPATHS, OUTLINE_FILEPATHS, test_size=0.1, random_state=1)

    copy_to_AB([TRAIN_CONS, TRAIN_OUTS], OUTPUT_FOLDERS, "train", CONST_DIFFICULTY)
    copy_to_AB([VAL_CONS, VAL_OUTS], OUTPUT_FOLDERS, "val", CONST_DIFFICULTY)
    copy_to_AB([TEST_CONS, TEST_OUTS], OUTPUT_FOLDERS, "test", CONST_DIFFICULTY)

