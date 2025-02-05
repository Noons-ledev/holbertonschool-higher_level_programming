#!/usr/bin/python3
"""
Comment here
"""


class VerboseList(list):
    """
    Class doc here
    """

    def append(self, item):
        print(f"Added [{item}] to the list.")
        super().append(item)

    def extend(self, item):
        print(f"Extended the list with [{len(item)}] items.")
        super().extend(item)

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, item=-1):
        if self[item] is None:
            raise IndexError("Index does not exist")
        print(f"Popped [{self[item]}] from the list.")
        super().pop(item)
