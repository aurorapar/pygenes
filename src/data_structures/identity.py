import os
from socket import gethostname

from system.hardware import identify_machine
from state import PLATFORM

class Identity:

    def __init__(self):
        self.hostname = gethostname()
        user_var = 'USER' if PLATFORM != 'windows' else 'USERNAME'
        self.username = os.environ[user_var]
        self.machine_id = identify_machine()

    def __repr__(self):
        return f"{self.hostname}/{self.username}/{self.machine_id}"
