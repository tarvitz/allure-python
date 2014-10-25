# encoding: utf-8

"""
Doctest tests

Created on Oct 23, 2014

@author: tarvitz
"""


class Power2Class(object):
    def __init__(self, base):
        self.base = base

    def power2(self):
        """
        returns power for argument of 2

        >>> foo = Power2Class(10)
        >>> foo.power2()
        100
        """
        return self.base ** 2


def power2(base):
    """
    returns power for base of 2

    >>> power2(10)
    100
    >>> power2(1.3)
    1.6900000000000002
    >>> power2(1/2.0)
    0.25
    """
    return base ** 2
