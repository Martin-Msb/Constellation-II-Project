import os
import pickle

WORK_DIR = os.path.dirname(os.path.realpath(__file__))

# Requires presence of Constellations_TOP_002/003 folder in unstructured_data folder
INPUT_DIR = os.path.join(WORK_DIR, "../unstructured_data/Constellations_TOP_003") # "../input_data/Test"
OUTPUT_DIR = os.path.join(WORK_DIR, "../unstructured_data/")

TEST_SET_IMAGENAMES = [name for name in os.listdir(INPUT_DIR) if os.path.isdir(os.path.join(INPUT_DIR, name))]

with open(os.path.join(OUTPUT_DIR, 'test_set_imagenames'), 'wb') as fp:
    pickle.dump(TEST_SET_IMAGENAMES, fp)

