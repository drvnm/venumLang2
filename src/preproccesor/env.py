from scanning.error import error

class PreEnv: # holds all the data for the preprocess
    def __init__(self):
        self.data = {}

    def set(self, key, value):
        self.data[key] = value

        