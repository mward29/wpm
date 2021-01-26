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

def LIST():
    LOG.debug("list function")

def REMOVE():
    LOG.debug("remove function")

def INSTALL():
    LOG.debug("install function")


def split_line(line):
    x = line.split(' ')
    pkg = x[1]
    deps = x[2:]
    return pkg, deps