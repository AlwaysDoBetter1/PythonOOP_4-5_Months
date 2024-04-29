'''
Implement a Config class that follows the singleton pattern and describes a configuration object with fixed parameters.
When instantiated, the class must not accept any arguments.

The first call to the Config class should create and return an instance of that class, and subsequent calls should
return the instance created on the first call.

An instance of the Config class must have four attributes:

program_name — attribute with string value GenerationPy
environment — attribute with string value release
loglevel - attribute with string value verbose
version - attribute with string value 1.0.0
'''

class Config:
    _inital = None

    def __new__(cls, *args, **kwargs):
        if cls._inital == None:
            cls._inital = object.__new__(cls)
        return cls._inital

    def __init__(self):
        self.program_name = "GenerationPy"
        self.environment = "release"
        self.loglevel = "verbose"
        self.version = "1.0.0"


# Example:
config = Config()

print(config.program_name)
print(config.environment)
print(config.loglevel)
print(config.version)

# Output:
# GenerationPy
# release
# verbose
# 1.0.0
