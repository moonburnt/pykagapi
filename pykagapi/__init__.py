#importing all valid scripts from subfolders to make it possible to import pykagapi as a whole
from .kag import *
from .kagstats import *

import logging

#this is necessary to dont flood stderr with errors if library's user dont use logging module
logging.getLogger(__name__).addHandler(logging.NullHandler())
