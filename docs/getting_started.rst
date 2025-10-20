Getting started
===============


This page demonstrates common reStructuredText and Sphinx features: **cross-references**, directives, code blocks, and math.


Section with an internal reference
---------------------------------


See the :ref:`api` page for the project's API documentation.


A note and a warning
--------------------


.. note::
This is a helpful note for readers — use notes to call attention to important but non-critical details.


.. warning::
This is a warning — use sparingly for important cautions.


Code example
------------


.. code-block:: python
:linenos:


def greet(name: str) -> str:
"""Return a greeting message for *name*.


Parameters
----------
name: str
"""
return f"Hello, {name}!"


Cross-references and roles
--------------------------


You can reference Python objects using roles like :py:func:`greet` and modules with :mod:`mypkg.example`.


Math example
------------


Inline math: :math:`E = mc^2`.


Block math:


.. math::


\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0}


Include an image (placed in _static/logo.png)
---------------------------------------------


