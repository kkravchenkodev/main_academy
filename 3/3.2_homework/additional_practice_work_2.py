import os
import re

"""
Write a function that reads data from the file,
parses the line by line and prints the following information to the new file:
- ip address from which the request came,
- error time,
- error text.
It is a mistake to read the entry in the log file
if [ERROR] is specified as the logging level.
The rest of the lines should be ignored.
"""

LOG_FILE = os.path.abspath('app.log')
OUTPUT_FILE = LOG_FILE.split('.')[0] + '_errors.log'
LOG_LEVEL = r'[ERROR]'

ip = r'[0-9]{1,3}[\.][0-9]{1,3}[\.][0-9]{1,3}[\.][0-9]{1,3}'
time = r'\d{2}\:\d{2}\:\d{2}\.\d+'
msg = r'AppLog:[\sa-zA-Z_]*'


def parse_log_file(path_to_file):
    with open(path_to_file) as log_file:
        with open(OUTPUT_FILE, 'w') as output_file:
            for row in log_file:
                if LOG_LEVEL in row:
                    items = re.search(ip, row)
                    print(items.group())
                    # output_file.write(' '.join(items))


parse_log_file(LOG_FILE)
