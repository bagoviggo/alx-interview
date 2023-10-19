#!/usr/bin/python3
import sys

def print_statistics(total_size, status_codes):
    """
    Print the calculated statistics.

    Args:
        total_size (int): Total file size.
        status_codes (dict): Dictionary containing the counts of each status code.

    Prints:
        File size and counts of status codes in ascending order.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def main():
    total_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()

            # Split the log line into its components
            parts = line.split()
            if len(parts) >= 7:
                status_code = parts[-2]
                file_size = parts[-1]

                # Check if status code is a valid integer and within the allowed status codes
                if status_code.isdigit() and status_code in status_codes:
                    total_size += int(file_size)
                    status_codes[status_code] += 1

                line_count += 1

                # Print statistics every 10 lines
                if line_count % 10 == 0:
                    print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        # Handle a KeyboardInterrupt (CTRL + C) by printing the current statistics
        print_statistics(total_size, status_codes)
        raise  # Re-raise the KeyboardInterrupt

if __name__ == "__main__":
    main()
