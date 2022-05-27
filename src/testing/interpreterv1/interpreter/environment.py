from scanning.error import error

# class where variables are stored
class Environment:
    def __init__(self):
        self.values = {}
        self.enclosing = None # environment for shadowing
    
    # puts vairable name and value into the environment
    def define(self, name, value):
        self.values[name] = value
    
    def get(self, name):
        if name in self.values:
            return self.values[name]
        if self.enclosing is not None:
            return self.enclosing.get(name)
        error(name.line, f"Undefined variable '{name}'.")
    
    def assign(self, name, value):
        if name in self.values:
            self.values[name] = value
            return
        if self.enclosing is not None:
            self.enclosing.assign(name, value)
            return
       
        error(name.line, f"Undefined variable '{name.lexeme}'.")
        
    def set_enclosing_env(self, env):
        self.enclosing = env
         