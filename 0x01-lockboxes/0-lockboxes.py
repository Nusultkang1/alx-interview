#!/usr/bin/python3
"""function that checks all boxes (functions) and returns True if they can be opened and False if they can't"""

def canUnlockAll(boxes):
    """defines a function to examnine boxes and determine their openability"""

    n = len(boxes)
    unlocked = [False] * n  # Track the unlocked status of each box
    unlocked[0] = True  # The first box is initially unlocked
    stack = [0]  # Start with the first box in the stack

    while stack:
        box = stack.pop()
        keys = boxes[box]
        for key in keys:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)

