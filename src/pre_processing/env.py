from scanning.error import error

class PreEnv: # holds all the data for the preprocess
    def __init__(self):
        self.data = {}
        self.included_files = []

    def define_macro(self, key, value):
        self.data[key] = value
    
    def get(self, key: str) -> str:
        return self.data[key]
    
    def updata_from_env(self, env: 'PreEnv') -> None:
        for key, value in env.data.items():
            self.data[key] = value
        for file_name in env.included_files:
            self.include(file_name)
    
    # returns if a macro exists in the environment
    def has(self, key: str) -> bool:
        return key in self.data

    # updates env with new included file name
    def include(self, file_name: str) -> None:
        self.included_files.append(file_name)
    
    # returns if a file has been included
    def has_included(self, file_name: str) -> bool:
        return file_name in self.included_files

        