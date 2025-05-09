import os
import sys
import re


PROJECT_ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
TEST_DATA_PATH = os.path.join(PROJECT_ROOT_PATH, 'testing_data')
#Split bases on \ or / for Unix and windows
PROJECT_NAME = re.split(r'\/|\\', PROJECT_ROOT_PATH)[-1]
DB_NAME = "accounting"
REPORTS_ROOT_PATH = os.path.join(PROJECT_ROOT_PATH, 'src/reports')
ICON_PATH = os.path.join(PROJECT_ROOT_PATH, 'icons', 'infinity-gauntlet.png')
sys.path.insert(0, PROJECT_ROOT_PATH)
sys.path.insert(1, PROJECT_ROOT_PATH + '/src/')