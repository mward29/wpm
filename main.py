import yaml
import os
import commands
from logger import logger
from config.config import initialize

root_path = initialize.ROOT_PATH
LOG = logger.get_root_logger(
    __name__, filename=os.path.join(root_path, 'output.log'))

p = {}

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
        #LOG.debug(cmd)
        if 'LIST' in cmd:
            getattr(commands, cmd)(p)
        else:
            getattr(commands, cmd)(line, p)


def run():
    """
    Primary runtime of WPM
    """
    #LOG.debug("and so it begins")
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
    #LOG.debug(lines)

    parse_lines(lines, p)

    #LOG.debug(p)

# execute if main
if __name__ == "__main__":
    """
    Run this if this app is being run from main
    """
    run()