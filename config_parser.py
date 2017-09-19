# @Date:   2017-06-25T11:49:03+02:00
# @Last modified time: 2017-06-29T15:47:36+02:00

import os
import xml.etree.ElementTree as ET
from module import ModuleConfig


class Configuration():
    """Parse a configuration file."""

    def __init__(self, file_):
        """Init the parser with a file name."""
        self.includes = []
        self.modules = []
        if os.path.isfile(file_):
            self._readConfiguration(file_)
        else:
            raise ValueError

    def _readConfiguration(self, fileName):
        tree = ET.parse(fileName)
        root = tree.getroot()
        self._parseNodes(root)

    def _parseModules(self, node):
        module = ModuleConfig()
        for n in node:
            if n.tag == 'module':
                module.name = n.attrib['name']
                # set other module fields
                self._setModuleAttrib(n, module)
                m = self._parseModules(n)
                if m:
                    module.submodules.append(m)
                return module
        return None

    def _printSub(self, module):
        print(module.name)
        for m in module.submodules:
            self._printSub(m)
            for f in m.files:
                print(f)
            for e in m.exclude_class:
                print(e)

    def _parseNodes(self, node):
        for n in node:
            if(n.tag == 'includes'):
                self.includes = self._parseIncludes(n)
            elif n.tag == 'modules':
                self.modules.append(self._parseModules(n))
            else:
                self._parseNodes(n)

    def _parseIncludes(self, node):
        includes = []
        for n in node:
            includes.append("-I" + n.attrib['name'])
        return includes

    def _setModuleAttrib(self, node, module):
        for child_node in node:
            if 'files' == child_node.tag:
                for f in child_node:
                    module.files.append(f.attrib['name'])
            elif child_node.tag == 'exclude':
                for e in child_node:
                    module.excluded_classes.append(e.attrib['name'])
