#!/usr/bin/python3


def canUnlockAll(boxes):
    """Starting with the first box that is already open"""
    opened_boxes = set([0])

    """To keep track of the keys we find, we'll use a list"""
    keys = [0]

    while keys:
        current_key = keys.pop()

        for key in boxes[current_key]:
            if key not in opened_boxes and key < len(boxes):
                opened_boxes.add(key)
                keys.append(key)

    return len(opened_boxes) == len(boxes)
