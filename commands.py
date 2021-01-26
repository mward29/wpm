import os
from config.config import initialize
from logger import logger
from utils.struct import Package as pk

root_path = initialize.ROOT_PATH
LOG = logger.get_root_logger(
    __name__, filename=os.path.join(root_path, 'output.log'))


def DEPEND():
    LOG.debug("depend function")

def LIST():
    LOG.debug("list function")

def REMOVE():
    LOG.debug("remove function")

def INSTALL():
    LOG.debug("install function")