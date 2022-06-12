class ConfigOptions:
    def __init__(self, config):
        self.config = config
        self.pre_processor = config.get('pre_processor', None)
        self.compiler = config.get('compiler', None)

        # TODO: better design pattern for this stuff

        # try get include_path from pre_processor
        if self.pre_processor:
            self.include_paths = self.pre_processor.get('include_paths', None) + ["."]
        else:
            self.include_paths = ["."]
        
        # try get output_path from compiler
        if self.compiler:
            self.output_path = self.compiler.get('output_path', None)
        else:
            self.output_path = "."

        print(self.output_path)
        print(self.pre_processor)