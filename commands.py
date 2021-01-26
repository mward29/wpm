import os
from config.config import initialize
from logger import logger
from utils.struct import Package as pk


root_path = initialize.ROOT_PATH
LOG = logger.get_root_logger(
    __name__, filename=os.path.join(root_path, 'output.log'))


def DEPEND(line, p):
    pkg, deps = split_line(line)
    p[pkg] = vars(pk(pkg, deps))
    deps_join = " ".join(deps)
    print("DEPEND " + pkg + " " + deps_join)


def LIST(p):
    key_list = []
    for key in p.keys():
        key_list.append(key)
    print(" ".join(key_list))


def REMOVE(line, p):
    pkg, deps = split_line(line)
    result = is_dependency(pkg, p)
    if result:
        print(pkg + " is still needed")
    else:
        try:
            del p[pkg]
            print(pkg + " successfull removed")
        except KeyError:
            print(pkg + " is not installed")


def INSTALL(line, p):
    pkg, deps = split_line(line)
    p[pkg] = vars(pk(pkg, deps))


def split_line(line):
    x = line.split(' ')
    pkg = x[1]
    deps = x[2:]
    return pkg, deps


def is_dependency(pkg, p):
    x = False
    test = p.copy()
    try:
        del test[pkg]
    except KeyError:
        pass
    if pkg in test:
        x = True
    return x