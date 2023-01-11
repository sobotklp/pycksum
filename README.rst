pycksum - A Python implementation of the cksum algorithm

|Build|  |PyVersion|  |PyPiVersion|  |License|

The ``cksum`` algorithm generates a checksum for a stream of data. While cksum is not cryptographically strong, it can be used to validate the integrity of transferred files.

Pycksum includes a pure Python implementation of ``cksum`` as well as an efficient C extension that will automatically be used on platforms that support it.

Installation
============

Install from PyPi using pip, a package manager for Python::

    $ pip install pycksum

Examples
========

The simplest way to use pycksum is to just give it a string::

    import pycksum
    ck = pycksum.cksum("Any string")

You can pass in a file or an iterable::

    ck = pycksum.cksum( open("filename"))

    ck = pycksum.cksum( ["This", "love", "is", "taking", "its", "toll", "on me"])

If you have a lot of data to process, it's more memory-efficient to calculate the cksum incrementally::

    c = pycksum.Cksum()
    for data in input_fd:
        c.add(data)
    ck = c.get_cksum()
    sz = c.get_size()


.. |PyPiVersion| image:: https://img.shields.io/pypi/v/pycksum.svg
   :alt: PyPi
   :target: https://pypi.python.org/pypi/pycksum

.. |License| image:: https://img.shields.io/badge/license-MIT-yellow.svg
   :alt:

.. |PyVersion| image:: https://img.shields.io/badge/python-3.7+-blue.svg
   :alt:

.. |Build| image:: https://github.com/sobotklp/pycksum/workflows/CI/badge.svg?branch=master
     :target: https://github.com/sobotklp/pycksum/actions?workflow=CI
     :alt: CI Status
