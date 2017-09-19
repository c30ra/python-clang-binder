# @Author: rebellion
# @Date:   2017-06-26T10:13:20+02:00
# @Last modified by:   rebellion
# @Last modified time: 2017-06-29T15:53:53+02:00
# @License: GPLv3
import clang.cindex


class Param():
    def __init__(self, name, type):
        self.name = name
        self.type = type


class Methods():
    def __init__(self):
        self.name = ""
        self.returnType = ""
        self.args = []


class Class():
     def __init__(self):
         self.methods = []
         self.enums = []
         self.fields = []
         self.name = ""


class Module():
    """A Module configuration."""

    def __init__(self):
        self.name = ""
        self.classes = []
        self.global_methods = []
        self.global_enums = []
        self.submodules = []

class Parser():

    def __init__(self, args, clang_args, moduleConfig):
        self._index = clang.cindex.Index.create(True)
        self._moduleConfig = moduleConfig
        self._args = args
        self._clang_args = clang_args

    def _parseClass(self, node):
        """Parse a class node in the translation unit."""
        class_ = Class()
        class_.name = node.spelling
        print("\tclass:", node.spelling)
        for c in node.get_children():
            if c.access_specifier == c.access_specifier.PUBLIC:
                try:
                    if c.kind == c.kind.CXX_METHOD:
                        print("\t\t|__", c.spelling)
                        class_.methods.append(c.spelling)
                    if c.kind == c.kind.FIELD_DECL:
                        print("\tField", c.spelling)
                except:
                    pass
        return class_

    def _parseAstNodes(self, node, module):
        """Parse the given AST node."""
        for c in node.get_children():
            try:
                if c.kind == c.kind.CLASS_DECL:
                    data = self._parseClass(c)
                    classes.append(data)
                elif c.kind == c.kind.CXX_METHOD:
                    pass
                elif c.kind == c.kind.ENUM_DECL:
                    pass
                elif c.kind == c.kind.NAMESPACE:
                    print("namespace")
                    self._parseAstNodes(c, module)
                else:
                    self._parseAstNodes(c, module)
            except:
                pass
        return module

    def _createModule(self, module):
        new_module = Module()
        for i in self._moduleConfig:
            for s in i.submodules:
                new_module.name = s.name
                for file_ in s.files:
                    fullName = self._args.dir[0] + '/' + file_
                    tu = self._index.parse(fullName, args=self._clang_args)
                    print('Translation unit:', tu.cursor.spelling)
                    tu_classes = self._parseAstNodes(tu.cursor, s)
                # m = self._createModule(module)
                # if m:
                    # new_module.submodules.append(m)
                # return new_module
        return None

    def parse(self):
        """Parse the source code and return a rappresentation of it."""
        module = Module()
        module.name = self._moduleConfig[0].name

        return self._createModule(module)
