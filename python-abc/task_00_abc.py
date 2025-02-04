#!/usr/bin/python3
"""
this module will introduce us to abc
"""
from abc import ABC, abstractmethod
"""
Here we import ABC for the abstract property of our class
"""


class Animal(ABC):
    """
    This abstract class will introduce subclasses
    """
    @abstractmethod
    def sound(self):
        """
        abstract method will be implemented for each subclass
        """
        pass


class Dog(Animal):
    """
    Dog subclass for using the abstract method
    """
    def sound(self):
        """
        abstrac method implementation
        """
        return (f"Bark")


class Cat(Animal):
    """
    Cat subclass for implementing abstract method
    """
    def sound(self):
        """
        method implementation for cat class
        """
        return (f"Meow")
