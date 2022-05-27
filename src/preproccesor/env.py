from scanning.error import error

class PreEnv: # holds all the data for the preprocess
    def __init__(self):
        self.data = {}

    def set(self, key, value):
        self.data[key] = value
    
    def updata_from_env(self, env: 'PreEnv') -> None:
        for key, value in env.data.items():
            self.data[key] = value

        