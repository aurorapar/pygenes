import os
import socket
import traceback
from datetime import datetime

from kivy.logger import Logger as KivyLogger
from kivy.config import Config

from hardware import identify_machine

class Logger:

    DATE_FORMAT = '%Y-%m-%d_%H-%M-%S'
    LOG_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'logs')

    def __init__(self):
        current_date = datetime.now().strftime(Logger.DATE_FORMAT)
        Config.set('kivy', 'log_name', f'pygenes_{current_date}.log')
        Config.set('kivy', 'log_dir', Logger.LOG_PATH)
        Config.set('kivy', 'log_level', 'error')

    def error(self, exception: Exception):
        now = datetime.now().strftime(Logger.DATE_FORMAT)
        stack_trace = ''.join(traceback.TracebackException.from_exception(exception).format())
        machine_id = identify_machine()
        machine_name = socket.gethostname()
        log_message = f"{now} Error occurred on hostname {machine_name} machine id {machine_id} \n{stack_trace}"
        KivyLogger.error(log_message)
