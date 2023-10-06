#!/usr/bin/python3

"""
This module defines a function canUnlockAll(boxes) that checks if all the boxes
can be opened in a given list of boxes using keys.

Requirements:
- The first box (boxes[0]) is unlocked.
- A key with the same number as a box opens that box.
- You can assume all keys will be positive integers.
- There can be keys that do not have boxes.
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes (list of list of int): A list of lists
        representing boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    stack = [0]  # Start with the first box, which is unlocked

    while stack:
        box = stack.pop()
        visited[box] = True

        for key in boxes[box]:
            if 0 <= key < n and not visited[key]:
                stack.append(key)

    return all(visited)

if __name__ == "__main__":
    # Test cases
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # False
