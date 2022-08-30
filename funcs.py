import imp
from os.path import realpath,join,dirname,exists,abspath
import sys

# get file path relative to python script location
def get_file_path(file_name):
    if getattr(sys, 'frozen', False):
        application_path = dirname(sys.executable)
    elif __file__:
        application_path = dirname(__file__)
    return join(application_path, file_name)

# Get absolute path to resource, works for dev and for PyInstaller
def get_resource_path(file_name):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = dirname(__file__)
    return join(base_path, file_name)