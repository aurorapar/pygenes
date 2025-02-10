import os
import hashlib

from constants import DIR_PATH

def calculate_version():
    source_files = []
    for source_dir, _, files in os.walk(DIR_PATH):
        source_files += [os.path.join(source_dir, x) for x in files if x.endswith('.py')]
    source_files.sort()
    source_code = ""
    for source_file in source_files:
        with open(source_file, 'r') as f:
            source_code += f.read()

    return hashlib.sha512(source_code.encode('UTF-8')).hexdigest()