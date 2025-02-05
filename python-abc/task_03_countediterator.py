#!/usr/bin/python3
"""
Module documentation
"""


class CountedIterator:
    """
    Class documentation
    """
    def __init__(self, iterable):
        if iterable is None:
            raise ValueError("Missing Argument")
        self.iterator = iter(iterable)
        self.counter = 0
        self.iterable = iterable

    def get_count(self):
        return self.counter

    def __next__(self):
        try:
            item = next(self.iterator)
        except StopIteration:
            raise StopIteration
        self.counter += 1
        return item
