import time


class MyTimer:
    def __init__(self, units='s'):
        self.units = {'s': 0, 'm': 1, 'h': 2}[units]
        self.start = time.time()
        self.spent_time = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        self.spent_time = (end - self.start) / (60 ** self.units)