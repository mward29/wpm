import yaml
import os
from logger import logger
from config.config import initialize

root_path = initialize.ROOT_PATH
LOG = logger.get_root_logger(
    __name__, filename=os.path.join(root_path, 'output.log'))


# intro to wpm
def intro():
    print("""
Welcome to the Ward Package Manager
Where the force MAY be with you ...
""")

def parse_lines(lines, packages):
    """
    Parse lines and execute commands
    """
    for line in lines:
        x = line.split(' ')
        cmd = x[0].upper()
        LOG.debug(cmd)


def run():
    """
    Primary runtime of WPM
    """
    LOG.debug("and so it begins")
    intro()

    lines = []
    print("Awaiting your input: ")
    test = ''
    while test != 'END':
        line = input()
        if line != "END":
            lines.append(line)
        else:
            test = 'END'
    LOG.debug(lines)


# execute if main
if __name__ == "__main__":
    """
    Run this if this app is being run from main
    """
    run()