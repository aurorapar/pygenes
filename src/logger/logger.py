import os
import socket
import traceback
from datetime import datetime

from kivy.logger import Logger as KivyLogger
from kivy.config import Config

from constants import DATE_FORMAT, LOG_PATH, DIR_PATH
from hardware import identify_machine

class Logger:

    def __init__(self):
        current_date = datetime.now().strftime(DATE_FORMAT)
        Config.set('kivy', 'log_name', f'pygenes_{current_date}.log')
        Config.set('kivy', 'log_dir', LOG_PATH)
        Config.set('kivy', 'log_level', 'error')

    def error(self, exception: Exception):
        now = datetime.now().strftime(DATE_FORMAT)
        stack_trace = ''.join(traceback.TracebackException.from_exception(exception).format())
        machine_id = identify_machine()
        machine_name = socket.gethostname()
        version = calculate_version()
        log_message = f"{now} Error occurred on hostname {machine_name} machine id {machine_id} on software version {version} \n{stack_trace}"
        KivyLogger.error(log_message)

def calculate_version():
    source_files = []
    for source_dir, _, files in os.walk(DIR_PATH):
        source_files += [os.path.join(source_dir, x) for x in files if x.endswith('.py')]
    source_files.sort()
    source_code = ""
    for source_file in source_files:
        with open(source_file, 'r') as f:
            source_code += f.read()

    import hashlib
    return hashlib.sha512(source_code.encode('UTF-8')).hexdigest()