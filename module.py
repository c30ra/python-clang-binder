class ModuleConfig():
    """A Module configuration."""

    def __init__(self):
        self.name = ""
        self.files = []
        self.excluded_classes = []
        self.excluded_class_methods = {}
        self.excluded_functions = []
        self.submodules = []
