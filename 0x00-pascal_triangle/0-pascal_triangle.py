#!/usr/bin/python3
""" function def pascal_triangle(n): that returns a list of lists of
    integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    # Initialize the result list with the first row
    result = [[1]]

    for i in range(1, n):
        # Generate the current row based on the previous row
        current_row = [1]  # The first element is always 1
        previous_row = result[-1]

        for j in range(1, i):
            current_element = previous_row[j - 1] + previous_row[j]
            current_row.append(current_element)

        current_row.append(1)  # The last element is always 1
        result.append(current_row)

    return result
