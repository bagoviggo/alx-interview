#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics as specified:
- Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
- After every 10 lines and/or a keyboard interruption (CTRL + C), print statistics:
  - Total file size: File size: <total size>
  - Number of lines by status code:
    - Possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500
    - Format: <status code>: <number> (status codes should be printed in ascending order)
"""

import sys

# Initialize status code counters
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}

total_size = 0
line_count = 0  # Keep track of the number of lines processed

try:
    for line in sys.stdin:
        line_list = line.split()

        if len(line_list) >= 7:
            status_code = line_list[-2]
            file_size = int(line_list[-1])

            if status_code in status_codes:
                status_codes[status_code] += 1

            total_size += file_size
            line_count += 1

            if line_count % 10 == 0:
                print(f'File size: {total_size}')
                for code, count in sorted(status_codes.items()):
                    if count > 0:
                        print(f'{code}: {count}')

except KeyboardInterrupt:
    pass  # Handle keyboard interrupt and print statistics in the finally block

finally:
    print(f'File size: {total_size}')
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f'{code}: {count}')
