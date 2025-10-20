"""Example module to be documented by Sphinx autodoc.


Functions
---------


.. autosummary::
:toctree: generated/


add


"""
from typing import Union




def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
"""Add two numbers and return the result.


Parameters
----------
a
First number
b
Second number


Returns
-------
int or float
The sum of ``a`` and ``b``


Examples
--------
>>> add(1, 2)
3
"""
return a + b