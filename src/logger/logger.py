import os
import socket
import traceback
from datetime import datetime

from kivy.logger import Logger as KivyLogger
from kivy.config import Config

from constants import DATE_FORMAT, LOG_PATH, DIR_PATH
from data_structures import Identity
from system.software import calculate_version

class Logger:

    def __init__(self):
        current_date = datetime.now().strftime(DATE_FORMAT)
        Config.set('kivy', 'log_name', f'pygenes_{current_date}.log')
        Config.set('kivy', 'log_dir', LOG_PATH)
        Config.set('kivy', 'log_level', 'error')

    def error(self, exception: Exception):
        now = datetime.now().strftime(DATE_FORMAT)
        stack_trace = ''.join(traceback.TracebackException.from_exception(exception).format())
        identity = Identity()
        version = calculate_version()
        log_message = f"{now} Error occurred on identity {identity} software version {version} \n{stack_trace}"
        KivyLogger.error(log_message)