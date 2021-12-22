#!/usr/bin/env python3

# Script to process files matching *.data.json in folder given on the command line
# if not folder is given prompt to run against the current directory

# Author: Dean Layton-James
# Date Created: 2021-12-27
# Last Update: 2021-12-27
# Code Style: PEP 8

# Import required packages
import os
import sys
import glob
from pathlib import Path


def main():
    """Main procedure to process data files

    First check our python version
    Check for a path on the command line and make sure it exists (and is a directory)

    If the checks are good we pass execution to the process_files function that handles all file operations
    and calculations on our data files
    """
    check_python_version()

    try:
        data_path = get_data_path()

        process_files(data_path)

    except Exception as ex:
        script_error(ex)


def check_python_version():
    """Require Python 3 or later to run this program
    raise an exception if we are running python versions less than 3
     """
    if sys.version_info.major < 3:
        script_error('This program requires Python 3, you are running Python ' + sys.version_info.major)


def get_data_path():
    """Checks for a data path

    First look on the command line and if we have a path check that it exists and is in deed a path and not a file
     """
    if len(sys.argv) != 2:
        usage()

    file_path = Path(sys.argv[1])
    if not file_path.is_dir():
        raise Exception('The folder ' + sys.argv[1] + ' does not exist')

    # Make sure out path has the OS compatible trailing slash
    return str(os.path.join(str(file_path), ''))


def process_files(data_path):
    """Find matching files and process each one in turn

    Each processed file gives a total of seqlen in that file to add to our running total
     """
    print(f'Data directory is ' + (data_path) + '...')

    files = glob.glob(data_path + '*.data.json')

    for file in files:
        process_file(file)


def process_file(file_name):
    print(f'Processing ' + file_name)


def script_error(msg):
    """General Catch Al exception handler

    It does the job ;)
     """
    print(f'\n{msg}\n')
    sys.exit(2)


def usage():
    """Output usage information for out program
     """
    script_error(
        'usage: sumall.py <path to files containing *.data.json files>\n\nPlease specify the folder containing the data files\n')


# Run our script
if __name__ == '__main__':
    main()
