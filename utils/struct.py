class Package:
    """
    Class to describe the structure of a given packager
    """
    def __init__(self, pkg, deps=[]): 
        self.pkg = pkg
        self.deps = deps
