#!/usr/bin/env python3
"""
Comment here
"""


class VerboseList(list):
    """
    Class doc here
    """

    def append(self, item):
        """
        Method doc here
        """
        print(f"Added [{item}] to the list.")
        super().append(item)

    def extend(self, item):
        """
        method doc here
        """
        print(f"Extended the list with [{len(item)}] items.")
        super().extend(item)

    def remove(self, item):
        """
        method doc here
        """
        if item not in self:
            raise ValueError("Can't find this value in this instance")
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, item=-1):
        """
        method doc here
        """
        if self[item] is None:
            raise IndexError("Index does not exist")
        print(f"Popped [{self[item]}] from the list.")
        retour = super().pop(item)
        return retour
