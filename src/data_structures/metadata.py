from datetime import datetime
from typing import List, Union

from constants import DATE_FORMAT
from data_structures import Identity
from system.software import calculate_version

class MetaData:

    modifications: List[List[Union[datetime, Identity, str]]]

    def __init__(self):
        self.create_date = datetime.now()
        self.create_user = Identity()
        self.version = calculate_version()
        self.modifications = [[self.create_date, self.create_user, self.version]]