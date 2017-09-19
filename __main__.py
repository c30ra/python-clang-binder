# @Date:   2017-06-24T11:57:00+02:00
# @Last modified time: 2017-07-05T16:05:53+02:00

import argparse
from config_parser import Configuration
import include_parser


def printDummy(node):
    try:
        print(node.kind, node.spelling)
        if node.kind == node.kind.CLASS_DECL:
            print(node.kind, node.spelling)
    except:
        pass
    for c in node.get_children():
        printDummy(c)


def main():
    """Eentry point."""
    parser = argparse.ArgumentParser(description='Creates binds')
    parser.add_argument('dir', metavar='file', nargs=1,
                        help='working directory')
    parser.add_argument('--config',
                        help='configuration file',
                        nargs=1,)

    args = parser.parse_args()
    configuration = Configuration(args.config[0])

    clang_args = configuration.includes
    print(clang_args)
    clang_args.append("-std=c++14")
    clang_args.append("-fms-compatibility")
    clang_args.append("-fms-extensions")
    clang_args.append("-fmsc-version=19")

    file_parser = include_parser.Parser(args, clang_args, configuration.modules)
    file_parser.parse()
        # printDummy(tu.cursor)

    # tu = index.parse(sys.argv[1], args=clang_args)
    # tu_classes = parseAstNodes(tu.cursor)

    # for i in tu.get_includes():
       # print(i.include)
    # for i in tu.diagnostics:
       # print(i)


if __name__ == '__main__':
    main()
