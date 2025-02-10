import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
REQUIREMENTS_FILE = os.path.join(DIR_PATH, '..', 'requirements.txt')

DATE_FORMAT = '%Y-%m-%d_%H-%M-%S'
LOG_PATH = os.path.join(DIR_PATH, 'logs')

USER_HOME = os.environ['HOME']

FILE_EXTENSION = ".pyg"
