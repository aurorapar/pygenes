import os

DATA_FILE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', 'data')
if not os.path.exists(DATA_FILE_DIR):
    os.mkdir(DATA_FILE_DIR)