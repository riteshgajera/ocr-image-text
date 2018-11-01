class Data(object):
    """__init__() functions as the class constructor"""
    def __init__(self, **kwargs):
        self.variables = kwargs

    def set(self, k, v):
        self.variables[k] = v

    def get(self, k):
        return self.variables.get(k, None)