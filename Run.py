from enum import Enum

import json

class Category(Enum):
    correct = 'correct'
    wrong = 'wrong'
    error = 'error'

class Run:
    def __init__(self, name, time, expected, status, category):
        self.name = name

        assert time[-1] == 's'
        time = time[0:-1]
        self.time = float(time)

        self.expected = expected
        self.status = status
        self.category = Category(category)