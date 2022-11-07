"""
Appending project directory to path to allow import of project code in tests
"""

import os
import sys

FILE_DIRECTORY = os.path.dirname(__file__)
PROJECT_DIRECTORY = os.path.dirname(FILE_DIRECTORY)
sys.path.append(PROJECT_DIRECTORY)
