wpm/__init__.py                                                                                     000644  000765  000024  00000000000 14003657270 014064  0                                                                                                    ustar 00ward                            staff                           000000  000000                                                                                                                                                                         wpm/__pycache__/                                                                                    000755  000765  000024  00000000000 14003664700 014171  5                                                                                                    ustar 00ward                            staff                           000000  000000                                                                                                                                                                         wpm/__pycache__/commands.cpython-39.pyc                                                             000644  000765  000024  00000003227 14003664700 020427  0                                                                                                    ustar 00ward                            staff                           000000  000000                                                                                                                                                                         a
    �i`�  �                   @   s~   d dl Z d dlmZ d dlmZ d dlmZ ejZej	e
e j�ed�d�Zdd� Zd	d
� Zdd� Zdd� Zdd� Zdd� ZdS )�    N)�
initialize)�logger)�Packagez
output.log)�filenamec                 C   s@   t | �\}}tt||��||< d�|�}td| d | � d S )N� zDEPEND )�
split_line�vars�pk�join�print)�line�p�pkg�depsZ	deps_join� r   �*/Users/ward/Documents/test/wpm/commands.py�DEPEND   s    
r   c                 C   s.   g }| � � D ]}|�|� qtd�|�� d S )Nr   )�keys�appendr   r
   )r   Zkey_list�keyr   r   r   �LIST   s    r   c                 C   sb   t | �\}}t||�}|r(t|d � n6z||= t|d � W n ty\   t|d � Y n0 d S )Nz is still neededz successfull removedz is not installed)r   �is_dependencyr   �KeyError)r   r   r   r   �resultr   r   r   �REMOVE   s    
r   c                 C   s"   t | �\}}tt||��||< d S )N)r   r   r	   )r   r   r   r   r   r   r   �INSTALL'   s    r   c                 C   s&   | � d�}|d }|dd � }||fS )Nr   �   �   )�split)r   �xr   r   r   r   r   r   ,   s    
r   c                 C   s:   d}|� � }z
|| = W n ty(   Y n0 | |v r6d}|S )NFT)�copyr   )r   r   r   �testr   r   r   r   3   s    
r   )�os�config.configr   r   Zutils.structr   r	   �	ROOT_PATH�	root_path�get_root_logger�__name__�pathr
   �LOGr   r   r   r   r   r   r   r   r   r   �<module>   s   �                                                                                                                                                                                                                                                                                                                                                                         wpm/commands.py                                                                                     000644  000765  000024  00000002257 14003664652 014150  0                                                                                                    ustar 00ward                            staff                           000000  000000                                                                                                                                                                         import os
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
    return x                                                                                                                                                                                                                                                                                                                                                 wpm/config/                                                                                         000755  000765  000024  00000000000 14003660035 013223  5                                                                                                    ustar 00ward                            staff                           000000  000000                                                                                                                                                                         wpm/config/config.py                                                                                000644  000765  000024  00000000227 14003657473 015057  0                                                                                                    ustar 00ward                            staff                           000000  000000                                                                                                                                                                         class initialize():
    '''
    initialize data for use by Package Installer
    '''
    
    '''
    Static Configuration
    '''

    ROOT_PATH = '.'                                                                                                                                                                                                                                                                                                                                                                         wpm/config/__pycache__/                                                                             000755  000765  000024  00000000000 14003660035 015433  5                                                                                                    ustar 00ward                            staff                           000000  000000                                                                                                                                                                         wpm/config/__pycache__/config.cpython-39.pyc                                                        000644  000765  000024  00000000573 14003660035 021336  0                                                                                                    ustar 00ward                            staff                           000000  000000                                                                                                                                                                         a
    ;_`�   �                   @   s   G d d� d�Z dS )c                   @   s   e Zd ZdZdZdS )�
initializez6
    initialize data for use by Package Installer
    �.N)�__name__�
__module__�__qualname__�__doc__�	ROOT_PATH� r   r   �//Users/ward/Documents/test/wpm/config/config.pyr      s   r   N)r   r   r   r   r	   �<module>   �                                                                                                                                         wpm/logger/                                                                                         000755  000765  000024  00000000000 14003657530 013243  5                                                                                                    ustar 00ward                            staff                           000000  000000                                                                                                                                                                         wpm/logger/__init__.py                                                                              000644  000765  000024  00000000026 14003657530 015352  0                                                                                                    ustar 00ward                            staff                           000000  000000                                                                                                                                                                         from .logger import *
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          wpm/logger/__pycache__/                                                                             000755  000765  000024  00000000000 14003662770 015455  5                                                                                                    ustar 00ward                            staff                           000000  000000                                                                                                                                                                         wpm/logger/logger.py                                                                                000644  000765  000024  00000001446 14003661577 015107  0                                                                                                    ustar 00ward                            staff                           000000  000000                                                                                                                                                                         ''' wrapper around logging module '''
import os
import logging

ROOT_PATH = os.environ.get('ROOT_PATH') or '.'


def get_root_logger(logger_name, filename=None):
    ''' get the logger object '''
    logger = logging.getLogger(logger_name)
    debug = os.environ.get('ENV', 'development') == 'development'
    logger.setLevel(logging.DEBUG if debug else logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    if filename:
        fh = logging.FileHandler(filename)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger


def get_child_logger(root_logger, name):
    return logging.getLogger('.'.join([root_logger, name]))                                                                                                                                                                                                                          wpm/logger/__pycache__/__init__.cpython-39.pyc                                                      000644  000765  000024  00000000243 14003657753 021651  0                                                                                                    ustar 00ward                            staff                           000000  000000                                                                                                                                                                         a
    X_`   �                   @   s   d dl T dS )�   )�*N)�logger� r   r   �1/Users/ward/Documents/test/wpm/logger/__init__.py�<module>   �                                                                                                                                                                                                                                                                                                                                                                 wpm/logger/__pycache__/logger.cpython-39.pyc                                                        000644  000765  000024  00000001700 14003662770 021363  0                                                                                                    ustar 00ward                            staff                           000000  000000                                                                                                                                                                         a
    c`&  �                   @   s:   d Z ddlZddlZej�d�p"dZd	dd�Zdd� ZdS )
z wrapper around logging module �    N�	ROOT_PATH�.c                 C   s~   t �| �}tj�dd�dk}|�|r*t jnt j� t �d�}t �	� }|�
|� |�|� |rzt �|�}|�
|� |�|� |S )z get the logger object ZENVZdevelopmentz4%(asctime)s - %(name)s - %(levelname)s - %(message)s)�logging�	getLogger�os�environ�getZsetLevel�DEBUG�INFOZ	FormatterZStreamHandlerZsetFormatterZ
addHandlerZFileHandler)Zlogger_name�filename�logger�debugZ	formatter�chZfh� r   �//Users/ward/Documents/test/wpm/logger/logger.py�get_root_logger   s    
�




r   c                 C   s   t �d�| |g��S )Nr   )r   r   �join)Zroot_logger�namer   r   r   �get_child_logger   s    r   )N)�__doc__r   r   r   r   r   r   r   r   r   r   r   �<module>   s
   
                                                                wpm/main.py                                                                                         000644  000765  000024  00000002542 14003666311 013262  0                                                                                                    ustar 00ward                            staff                           000000  000000                                                                                                                                                                         import yaml
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

    reloop = True
    while reloop is True:
        lines = []
        print("Awaiting your input: ")
        print('EXIT or ctrl-c to quit WPM')
        test = ''
        while test != 'END' and test != 'EXIT':
            line = input()
            if line == 'EXIT':
                exit()
            elif line != "END":
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
    run()                                                                                                                                                              wpm/output.log                                                                                      000644  000765  000024  00000012170 14003665134 014027  0                                                                                                    ustar 00ward                            staff                           000000  000000                                                                                                                                                                         2021-01-25 17:19:41,040 - __main__ - DEBUG - and so it begins
2021-01-25 17:27:30,687 - __main__ - DEBUG - and so it begins
2021-01-25 17:28:12,123 - __main__ - DEBUG - and so it begins
2021-01-25 17:28:21,558 - __main__ - DEBUG - and so it begins
2021-01-25 17:28:46,471 - __main__ - DEBUG - and so it begins
2021-01-25 17:33:26,274 - __main__ - DEBUG - and so it begins
2021-01-25 17:33:30,119 - __main__ - DEBUG - ['DEPEND TELNET TCPIP NETCARD', 'DEPEND TCPIP NETCARD', 'DEPEND DNS TCPIP NETCARD', 'DEPEND BROWSER TCPIP HTML', 'INSTALL NETCARD', 'INSTALL TELNET', 'INSTALL foo', 'REMOVE NETCARD', 'INSTALL BROWSER', 'INSTALL DNS', 'LIST', 'REMOVE TELNET', 'REMOVE NETCARD', 'REMOVE DNS', 'REMOVE NETCARD', 'INSTALL NETCARD', 'REMOVE TCPIP', 'REMOVE BROWSER', 'REMOVE TCPIP', 'LIST']
2021-01-25 17:33:56,826 - __main__ - DEBUG - and so it begins
2021-01-25 17:33:58,312 - __main__ - DEBUG - ['DEPEND TELNET TCPIP NETCARD', 'DEPEND TCPIP NETCARD', 'DEPEND DNS TCPIP NETCARD', 'DEPEND BROWSER TCPIP HTML', 'INSTALL NETCARD', 'INSTALL TELNET', 'INSTALL foo', 'REMOVE NETCARD', 'INSTALL BROWSER', 'INSTALL DNS', 'LIST', 'REMOVE TELNET', 'REMOVE NETCARD', 'REMOVE DNS', 'REMOVE NETCARD', 'INSTALL NETCARD', 'REMOVE TCPIP', 'REMOVE BROWSER', 'REMOVE TCPIP', 'LIST']
2021-01-25 17:44:40,215 - __main__ - DEBUG - and so it begins
2021-01-25 17:44:44,196 - __main__ - DEBUG - ['DEPEND TELNET TCPIP NETCARD', 'DEPEND TCPIP NETCARD', 'DEPEND DNS TCPIP NETCARD', 'DEPEND BROWSER TCPIP HTML', 'INSTALL NETCARD', 'INSTALL TELNET', 'INSTALL foo', 'REMOVE NETCARD', 'INSTALL BROWSER', 'INSTALL DNS', 'LIST', 'REMOVE TELNET', 'REMOVE NETCARD', 'REMOVE DNS', 'REMOVE NETCARD', 'INSTALL NETCARD', 'REMOVE TCPIP', 'REMOVE BROWSER', 'REMOVE TCPIP', 'LIST']
2021-01-25 17:58:55,699 - __main__ - DEBUG - and so it begins
2021-01-25 17:58:59,164 - __main__ - DEBUG - ['DEPEND TELNET TCPIP NETCARD', 'DEPEND TCPIP NETCARD', 'DEPEND DNS TCPIP NETCARD', 'DEPEND BROWSER TCPIP HTML', 'INSTALL NETCARD', 'INSTALL TELNET', 'INSTALL foo', 'REMOVE NETCARD', 'INSTALL BROWSER', 'INSTALL DNS', 'LIST', 'REMOVE TELNET', 'REMOVE NETCARD', 'REMOVE DNS', 'REMOVE NETCARD', 'INSTALL NETCARD', 'REMOVE TCPIP', 'REMOVE BROWSER', 'REMOVE TCPIP', 'LIST']
2021-01-25 18:01:35,505 - __main__ - DEBUG - DEPEND
2021-01-25 18:01:35,505 - __main__ - DEBUG - DEPEND
2021-01-25 18:01:35,505 - __main__ - DEBUG - DEPEND
2021-01-25 18:01:35,506 - __main__ - DEBUG - DEPEND
2021-01-25 18:01:35,506 - __main__ - DEBUG - INSTALL
2021-01-25 18:01:35,506 - __main__ - DEBUG - INSTALL
2021-01-25 18:01:35,506 - __main__ - DEBUG - INSTALL
2021-01-25 18:01:35,506 - __main__ - DEBUG - REMOVE
2021-01-25 18:01:35,506 - __main__ - DEBUG - INSTALL
2021-01-25 18:01:35,506 - __main__ - DEBUG - INSTALL
2021-01-25 18:01:35,506 - __main__ - DEBUG - LIST
2021-01-25 18:01:35,506 - __main__ - DEBUG - REMOVE
2021-01-25 18:01:35,506 - __main__ - DEBUG - REMOVE
2021-01-25 18:01:35,507 - __main__ - DEBUG - REMOVE
2021-01-25 18:01:35,507 - __main__ - DEBUG - REMOVE
2021-01-25 18:01:35,507 - __main__ - DEBUG - INSTALL
2021-01-25 18:01:35,507 - __main__ - DEBUG - REMOVE
2021-01-25 18:01:35,507 - __main__ - DEBUG - REMOVE
2021-01-25 18:01:35,507 - __main__ - DEBUG - REMOVE
2021-01-25 18:01:35,507 - __main__ - DEBUG - LIST
2021-01-25 18:02:47,243 - __main__ - DEBUG - DEPEND
2021-01-25 18:02:47,243 - __main__ - DEBUG - DEPEND
2021-01-25 18:02:47,244 - __main__ - DEBUG - DEPEND
2021-01-25 18:02:47,244 - __main__ - DEBUG - DEPEND
2021-01-25 18:02:47,244 - __main__ - DEBUG - INSTALL
2021-01-25 18:02:47,244 - __main__ - DEBUG - INSTALL
2021-01-25 18:02:47,244 - __main__ - DEBUG - INSTALL
2021-01-25 18:02:47,244 - __main__ - DEBUG - REMOVE
2021-01-25 18:02:47,244 - __main__ - DEBUG - INSTALL
2021-01-25 18:02:47,244 - __main__ - DEBUG - INSTALL
2021-01-25 18:02:47,244 - __main__ - DEBUG - LIST
2021-01-25 18:02:47,245 - __main__ - DEBUG - REMOVE
2021-01-25 18:02:47,245 - __main__ - DEBUG - REMOVE
2021-01-25 18:02:47,245 - __main__ - DEBUG - REMOVE
2021-01-25 18:02:47,245 - __main__ - DEBUG - REMOVE
2021-01-25 18:02:47,245 - __main__ - DEBUG - INSTALL
2021-01-25 18:02:47,245 - __main__ - DEBUG - REMOVE
2021-01-25 18:02:47,245 - __main__ - DEBUG - REMOVE
2021-01-25 18:02:47,245 - __main__ - DEBUG - REMOVE
2021-01-25 18:03:24,432 - __main__ - DEBUG - DEPEND
2021-01-25 18:03:24,432 - __main__ - DEBUG - DEPEND
2021-01-25 18:03:24,432 - __main__ - DEBUG - DEPEND
2021-01-25 18:03:24,433 - __main__ - DEBUG - DEPEND
2021-01-25 18:03:24,433 - __main__ - DEBUG - INSTALL
2021-01-25 18:03:24,433 - __main__ - DEBUG - INSTALL
2021-01-25 18:03:24,433 - __main__ - DEBUG - INSTALL
2021-01-25 18:03:24,433 - __main__ - DEBUG - REMOVE
2021-01-25 18:03:24,433 - __main__ - DEBUG - INSTALL
2021-01-25 18:03:24,433 - __main__ - DEBUG - INSTALL
2021-01-25 18:03:24,434 - __main__ - DEBUG - LIST
2021-01-25 18:03:24,434 - __main__ - DEBUG - REMOVE
2021-01-25 18:03:24,434 - __main__ - DEBUG - REMOVE
2021-01-25 18:03:24,434 - __main__ - DEBUG - REMOVE
2021-01-25 18:03:24,434 - __main__ - DEBUG - REMOVE
2021-01-25 18:03:24,434 - __main__ - DEBUG - INSTALL
2021-01-25 18:03:24,434 - __main__ - DEBUG - REMOVE
2021-01-25 18:03:24,434 - __main__ - DEBUG - REMOVE
2021-01-25 18:03:24,434 - __main__ - DEBUG - REMOVE
                                                                                                                                                                                                                                                                                                                                                                                                        wpm/requirements.txt                                                                                000644  000765  000024  00000000007 14003657270 015246  0                                                                                                    ustar 00ward                            staff                           000000  000000                                                                                                                                                                         pyyaml
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         wpm/setup.py                                                                                        000644  000765  000024  00000000306 14003663423 013473  0                                                                                                    ustar 00ward                            staff                           000000  000000                                                                                                                                                                         setup(name='wpm',
      version='0.0.1',
      description='Ward Package Manager',
      author='Michael Ward',
      author_email='na@na.com',
      url='https://github.com/mward29/wpm.git',
     )                                                                                                                                                                                                                                                                                                                          wpm/utils/                                                                                          000755  000765  000024  00000000000 14003665446 013131  5                                                                                                    ustar 00ward                            staff                           000000  000000                                                                                                                                                                         wpm/utils/__pycache__/                                                                              000755  000765  000024  00000000000 14003662770 015336  5                                                                                                    ustar 00ward                            staff                           000000  000000                                                                                                                                                                         wpm/utils/struct.py                                                                                 000644  000765  000024  00000000256 14003660275 015025  0                                                                                                    ustar 00ward                            staff                           000000  000000                                                                                                                                                                         class Package:
    """
    Class to describe the structure of a given packager
    """
    def __init__(self, pkg, deps=[]): 
        self.pkg = pkg
        self.deps = deps
                                                                                                                                                                                                                                                                                                                                                  wpm/utils/__pycache__/struct.cpython-39.pyc                                                         000644  000765  000024  00000001005 14003662770 021307  0                                                                                                    ustar 00ward                            staff                           000000  000000                                                                                                                                                                         a
    �``�   �                   @   s   G d d� d�Z dS )c                   @   s   e Zd ZdZg fdd�ZdS )�Packagez=
    Class to describe the structure of a given packager
    c                 C   s   || _ || _d S )N)�pkg�deps)�selfr   r   � r   �./Users/ward/Documents/test/wpm/utils/struct.py�__init__   s    zPackage.__init__N)�__name__�
__module__�__qualname__�__doc__r   r   r   r   r   r      s   r   N)r   r   r   r   r   �<module>   �                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               