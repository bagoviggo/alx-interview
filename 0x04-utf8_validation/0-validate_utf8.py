#!/usr/bin/python3
"""
Module: 0-validate_utf8

This module defines the validUTF8 function, which is used to determine if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing 1 byte of data each.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes expected to follow a start byte (0-4)
    expected_bytes = 0
    
    for byte in data:
        # Check if the current byte is a start byte
        if expected_bytes == 0:
            if (byte >> 5) == 0b110:
                expected_bytes = 1
            elif (byte >> 4) == 0b1110:
                expected_bytes = 2
            elif (byte >> 3) == 0b11110:
                expected_bytes = 3
            elif (byte >> 7) == 0b1:
                return False
        else:
            # Check if the current byte is a continuation byte
            if (byte >> 6) != 0b10:
                return False
            expected_bytes -= 1

    # Ensure all expected bytes have been found
    return expected_bytes == 0

