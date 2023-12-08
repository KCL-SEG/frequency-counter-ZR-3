"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        if not isinstance(item, str):
            item_string = str(item)
        else:
            item_string = item

        if item_string in frequencies:
            frequencies[item_string] += 1
        else:
            frequencies[item_string] = 1
    return frequencies
