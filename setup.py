from setuptools import setup
from setuptools.extension import Extension

from pycksum import __version__

long_description = open("README.rst").read()

setup(
    name="pycksum",
    description="Python implementation of cksum algorithm",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    packages=["pycksum"],
    url="https://github.com/sobotklp/pycksum",
    version=__version__,
    author="Lewis Sobotkiewicz",
    author_email="lewis.sobot@gmail.com",
    ext_modules=[Extension("_pycksum", ["ext/_pycksum.c"])],
    test_suite="tests",
    entry_points={
        "console_scripts": [
            "pycksum = pycksum.main:main",
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
