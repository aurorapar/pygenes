import os
import json

from data_structures import MetaData
from file_operations import FileSaver

class FamilyLine:

    def __init__(self):
        self.path = None
        self.metadata = MetaData()

    def save(self):
        FileSaver().execute()