import yaml
import os
from logger import logger

root_path = initialize.ROOT_PATH
LOG = logger.get_root_logger(
    __name__, filename=os.path.join(root_path, 'output.log'))


def run():
    LOG.debug("and so it begins")


# execute if main
if __name__ == "__main__":
    """
    Run this if this app is being run from main
    """
    run()