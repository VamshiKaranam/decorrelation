# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../nbs/CLI/utils/logging.ipynb.

# %% auto 0
__all__ = ['get_logger']

# %% ../../../nbs/CLI/utils/logging.ipynb 3
import logging
import sys
import random
import string
import inspect

# %% ../../../nbs/CLI/utils/logging.ipynb 4
def _get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

# %% ../../../nbs/CLI/utils/logging.ipynb 5
def get_logger(name:str=None, # name of the application, optional. default: the function name that call this function
               logfile:str=None, # logfile, optional. default: no logfile
               level:str=None, # log level, debug or info, optional. default: info
              ):
    '''get logger for decorrelation cli application'''

    if not name:
        name = inspect.stack()[1][3] #obtain the previous level function name
    
    if not level:
        level = 'info'
    if level == 'info':
        level = logging.INFO
    elif level == 'debug':
        level = logging.DEBUG
    else:
        raise NotImplementedError('only debug and info level are supported')

    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
    random_logger_name = _get_random_string(36)
    #The real name of the logger is set to random string to prevent events propogating.

    logger = logging.getLogger(random_logger_name)
    logger.setLevel(level)
    formatter = logging.Formatter(f'%(asctime)s - {name} - %(levelname)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    if logfile:
        file_handler = logging.FileHandler(logfile)
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger
