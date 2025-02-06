#!/usr/bin/python3
"""
Module documentation goes here
"""


class SwimMixin:
    """
    Class documentation goes here
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    Class documentation goes here
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Class documentation
    """
    def roar(self):
        print("The dragon roars!")
