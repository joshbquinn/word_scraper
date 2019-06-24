import shutil
import os
from datetime import datetime


def unique_directory(directory_name):
    now = datetime.now()
    date = now.strftime("_%d.%m.%Y %H.%M.%S")
    return directory_name + date


def create_directory(directory):
    """Create a directory, if it doesn't exist, in the current working directory to store the various files of keywords.

    Args:
        directory: specified directory name to create in cwd.
    """
    if not os.path.isdir(directory):
        os.mkdir(directory)


def write_to_directory(file_name, directory_name):
    """Move a specified file to  a specified directory in the current working directory.

    Args:
        file_name: The specified file name to move into the directory
        directory_name: specified directory name to write to.
    """
    shutil.move(file_name, directory_name)

